variable "aws_region" {
  description = "AWS region in which to create the demo resources."
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Short prefix used to name project resources."
  type        = string
  default     = "student-platform-mp4"
}

variable "key_name" {
  description = "Name of an existing EC2 key pair in the selected AWS region."
  type        = string
}

variable "admin_cidr" {
  description = "Administrator public IPv4 CIDR allowed to SSH and access direct API port 8080, e.g. 203.0.113.10/32."
  type        = string
  validation {
    condition     = can(cidrnetmask(var.admin_cidr))
    error_message = "admin_cidr must be a valid IPv4 CIDR block."
  }
}

variable "instance_type" {
  description = "EC2 instance type. Check current regional availability and pricing."
  type        = string
  default     = "t2.micro"
}

variable "ami_id" {
  description = "Optional Ubuntu 22.04 AMI ID for the selected region. Leave blank to use the latest Canonical image from SSM."
  type        = string
  default     = ""
}
