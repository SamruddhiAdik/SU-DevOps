# Terraform

This module creates a demo VPC (`10.1.0.0/16`), public subnet (`10.1.0.0/24`), internet gateway, route table, security group, Ubuntu EC2 instance and private encrypted/versioned S3 bucket.

## Usage
1. Copy `terraform.tfvars.example` to `terraform.tfvars`.
2. Set `key_name` to an existing EC2 key pair and `admin_cidr` to your IP `/32`.
3. Configure AWS credentials outside this folder.
4. Run `terraform init`, `terraform fmt -recursive`, `terraform validate`, `terraform plan`.
5. Apply only after reviewing the plan. Destroy resources when done.

The S3 bucket name includes a generated suffix. The bucket is not public and `force_destroy` is disabled. Terraform state may contain sensitive metadata; do not commit it.
