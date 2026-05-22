terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# --------------------------------------------------------------------------
# LOCALS: Centralized Naming Scheme Matching Your Student Account Rules
# --------------------------------------------------------------------------
locals {
  # This builds: student-eric-chen-[type]-bankapp
  # We leave a placeholder token in the middle so each resource can name itself accurately
  name_template = "student-${var.student_name}-%s-${var.project}"

  common_tags = {
    Project     = var.project
    Environment = var.environment
    Owner       = var.student_name
    ManagedBy   = "Terraform"
  }
}

# --------------------------------------------------------------------------
# FRONTEND: S3 Static Storage Bucket
# --------------------------------------------------------------------------
resource "aws_s3_bucket" "frontend" {
  # Resolves to: student-eric-chen-s3-frontend-bankapp
  bucket        = format(local.name_template, "s3-frontend")
  force_destroy = true
  tags          = local.common_tags
}

resource "aws_cloudfront_origin_access_control" "oac" {
  # Resolves to: student-eric-chen-oac-frontend-bankapp
  name                              = format(local.name_template, "oac-frontend")
  description                       = "Origin Access Control for secure S3 frontend exposure"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

# --------------------------------------------------------------------------
# FRONTEND: CloudFront Content Delivery Network (CDN)
# --------------------------------------------------------------------------
resource "aws_cloudfront_distribution" "cdn" {
  enabled             = true
  default_root_object = "index.html"
  tags                = local.common_tags

  origin {
    domain_name              = aws_s3_bucket.frontend.bucket_regional_domain_name
    origin_id                = "S3-${aws_s3_bucket.frontend.id}"
    origin_access_control_id = aws_cloudfront_origin_access_control.oac.id
  }

  default_cache_behavior {
    allowed_methods        = ["GET", "HEAD", "OPTIONS"]
    cached_methods         = ["GET", "HEAD"]
    target_origin_id       = "S3-${aws_s3_bucket.frontend.id}"
    viewer_protocol_policy = "redirect-to-https"

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }
  }

  custom_error_response {
    error_code         = 403
    response_code      = 200
    response_page_path = "/index.html"
  }

  custom_error_response {
    error_code         = 404
    response_code      = 200
    response_page_path = "/index.html"
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }
}

resource "aws_s3_bucket_policy" "cloudfront_s3_access" {
  bucket = aws_s3_bucket.frontend.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "AllowCloudFrontServicePrincipalReadOnly"
        Effect    = "Allow"
        Principal = { Service = "cloudfront.amazonaws.com" }
        Action    = "s3:GetObject"
        Resource  = "${aws_s3_bucket.frontend.arn}/*"
        Condition = {
          StringEquals = {
            "AWS:SourceArn" = aws_cloudfront_distribution.cdn.arn
          }
        }
      }
    ]
  })
}

# --------------------------------------------------------------------------
# BACKEND: IAM Execution Role for Lambda
# --------------------------------------------------------------------------
resource "aws_iam_role" "lambda_exec" {
  # Resolves to: student-eric-chen-iam-lambda-role-bankapp
  name = format(local.name_template, "iam-lambda-role")

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }
    }]
  })
  tags = local.common_tags
}

resource "aws_iam_role_policy_attachment" "lambda_logs" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# --------------------------------------------------------------------------
# BACKEND: Baseline Deployment Placeholder Archive
# --------------------------------------------------------------------------
# Generates a dummy archive on initial creation so your baseline terraform apply succeeds
data "archive_file" "lambda_placeholder" {
  type        = "zip"
  output_path = "${path.module}/lambda_placeholder.zip"
  
  source {
    content  = "def handler(event, context): return {'statusCode': 200}"
    filename = "main.py"
  }
}

# --------------------------------------------------------------------------
# BACKEND: Native Zip-Based AWS Lambda Function
# --------------------------------------------------------------------------
resource "aws_lambda_function" "fastapi_backend" {
  # Resolves to: student-eric-chen-lambda-backend-bankapp
  function_name = format(local.name_template, "lambda-backend")
  role          = aws_iam_role.lambda_exec.arn
  
  # CHANGE: Swap package type from Image to Zip deployment parameters
  package_type     = "Zip"
  runtime          = "python3.12"
  handler          = "main.handler" # Looks for main.py -> handler object instance
  filename         = data.archive_file.lambda_placeholder.output_path
  
  timeout     = 30
  memory_size = 512
  tags        = local.common_tags

  # This lifecycle constraint ensures that future code deployment updates pushed via 
  # GitHub Actions won't cause Terraform to try and overwrite your app back into the placeholder zip state
  lifecycle {
    ignore_changes = [
      filename,
      source_code_hash
    ]
  }

  environment {
    variables = {
      MONGODB_URL   = var.mongodb_url
      DATABASE_NAME = "BankApp-${var.environment}"
      SECRET_KEY    = var.jwt_secret_key
      FRONTEND_URLS = "https://dzfmc2aiqla8u.cloudfront.net"
    }
  }
}
# --------------------------------------------------------------------------
# BACKEND: API Gateway Routing Layer
# --------------------------------------------------------------------------
resource "aws_apigatewayv2_api" "http_api" {
  # Resolves to: student-eric-chen-apigw-router-bankapp
  name          = format(local.name_template, "apigw-router")
  protocol_type = "HTTP"
  tags          = local.common_tags
}

resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id                 = aws_apigatewayv2_api.http_api.id
  integration_type       = "AWS_PROXY"
  connection_type        = "INTERNET"
  integration_method     = "POST"
  integration_uri        = aws_lambda_function.fastapi_backend.arn
  payload_format_version = "2.0"
}

resource "aws_apigatewayv2_route" "api_route" {
  api_id    = aws_apigatewayv2_api.http_api.id
  route_key = "ANY /{proxy+}"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

resource "aws_apigatewayv2_stage" "default_stage" {
  api_id      = aws_apigatewayv2_api.http_api.id
  name        = "$default"
  auto_deploy = true
}

resource "aws_lambda_permission" "apigw_lambda" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.fastapi_backend.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.http_api.execution_arn}/*/*"
}

# --------------------------------------------------------------------------
# OUTPUTS
# --------------------------------------------------------------------------
output "cloudfront_domain_name" {
  value = aws_cloudfront_distribution.cdn.domain_name
}

output "api_gateway_endpoint" {
  value = aws_apigatewayv2_api.http_api.api_endpoint
}