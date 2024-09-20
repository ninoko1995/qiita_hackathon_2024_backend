module "network" {
  source = "./network"
}

module "frontend" {
  source = "./frontend"
  bucket_name = "kosugiiz-frontend-bucket"
}

module "backend" {
  source = "./backend"
  vpc_id               = module.network.vpc_id
  public_subnet_ids    = module.network.public_subnet_ids
  private_subnet_ids   = module.network.private_subnet_ids
  rds_password         = var.rds_password
  s3_bucket_backend    = module.frontend.bucket_name
}

variable "rds_password" {
  description = "The password for the RDS database"
  type        = string
}
