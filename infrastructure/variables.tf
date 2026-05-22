variable "aws_region" {
  type        = string
  description = "The AWS region to deploy all resources into"
  default     = "us-east-1"
}

variable "project" {
  type        = string
  description = "The name of the project, used for resource naming"
  default     = "bankapp"
}

variable "environment" {
  type        = string
  description = "The deployment stage (e.g., dev, staging, prod)"
  default     = "prod"
}

variable "mongodb_url" {
  type        = string
  description = "The connection string for your MongoDB Atlas or DocumentDB cluster"
  sensitive   = true # Hides the value from showing up in plaintext console logs
}

variable "jwt_secret_key" {
  type        = string
  description = "The master secret key used to cryptographically sign your backend JWT tokens"
  sensitive   = true
}

variable "student_name" {
  type        = string
  description = "The student identity string required for AWS resource naming compliance"
  default     = "eric-chen"
}