variable "vpc_id" {
  description = "VPC ID"
  type        = string
}

variable "public_subnet_ids" {
  description = "List of public subnet IDs"
  type        = list(string)
}

variable "private_subnet_ids" {
  description = "List of private subnet IDs"
  type        = list(string)
}

variable "rds_password" {
  description = "RDS password"
  type        = string
}

variable "s3_bucket_backend" {
  description = "S3 bucket name for backend access"
  type        = string
}
