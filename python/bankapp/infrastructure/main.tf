terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# 1. Configure the AWS Provider
provider "aws" {
  region = "us-east-1" # Change to your preferred region
}

# 2. IAM Role for Lambda Execution
resource "aws_iam_role" "lambda_exec_role" {
  name = "student-eric-chen-fastapi-bank-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

# Attach basic execution policy (allows logging to CloudWatch)
resource "aws_iam_role_policy_attachment" "lambda_basic_execution" {
  role       = aws_iam_role.lambda_exec_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# 3. The Lambda Function
resource "aws_lambda_function" "fastapi_backend" {
  function_name = "student-eric-chen-bank-app-backend"
  
  filename         = "../deployment.zip"
  source_code_hash = filebase64sha256("../deployment.zip")

  handler = "main.handler"
  runtime = "python3.12" 

  role = aws_iam_role.lambda_exec_role.arn

  memory_size = 256
  timeout     = 15

  environment {
    variables = {
      MONGODB_URL   = var.mongodb_url
      DATABASE_NAME = var.database_name
    }
  }
}

# 4. Variables for Secrets
variable "mongodb_url" {
  description = "MongoDB Connection String"
  type        = string
  sensitive   = true
}

variable "database_name" {
  description = "MongoDB Database Name"
  type        = string
  default     = "bank_db"
}

# 5. API Gateway (HTTP API v2)
resource "aws_apigatewayv2_api" "http_api" {
  name          = "student-eric-chen-bank-app-api"
  protocol_type = "HTTP"
}

# 6. API Gateway Integration with Lambda
resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id           = aws_apigatewayv2_api.http_api.id
  integration_type = "AWS_PROXY"
  
  integration_uri    = aws_lambda_function.fastapi_backend.invoke_arn
  integration_method = "POST"
  payload_format_version = "2.0" 
}

# 7. Catch-All Route ($default)
resource "aws_apigatewayv2_route" "default_route" {
  api_id    = aws_apigatewayv2_api.http_api.id
  route_key = "$default"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

# 8. API Gateway Stage
# (Note: $default is a reserved AWS keyword for the stage name and routing, 
# so we leave this exactly as "$default" rather than applying the naming convention to it)
resource "aws_apigatewayv2_stage" "default_stage" {
  api_id      = aws_apigatewayv2_api.http_api.id
  name        = "$default"
  auto_deploy = true
}

# 9. Lambda Permission for API Gateway
resource "aws_lambda_permission" "api_gw" {
  statement_id  = "student-eric-chen-AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.fastapi_backend.function_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_apigatewayv2_api.http_api.execution_arn}/*/*"
}

# 10. Output the API URL
output "api_endpoint" {
  description = "The Base URL of your deployed FastAPI app"
  value       = aws_apigatewayv2_api.http_api.api_endpoint
}