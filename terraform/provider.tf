terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  backend "s3" {
    bucket = "kosugiiz-tf-state"
    key    = "terraform.tfstate"
    region = "ap-northeast-1"
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  profile = "ninomiya"
  region = "ap-northeast-1"

  default_tags {
    tags = {
      Project = "kosugiiz"
    }
  }
}
