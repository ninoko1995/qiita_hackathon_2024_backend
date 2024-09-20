output "frontend_s3_bucket" {
  value = module.frontend.bucket_name
}

output "cloudfront_url" {
  value = module.frontend.cloudfront_domain_name
}

output "rds_endpoint" {
  value = module.backend.rds_endpoint
}
