# Architecture — Student Record & Academic Management Platform

## Request flow

```text
Browser / API client
        |
        | HTTP :80
        v
AWS Internet Gateway
        |
Public subnet 10.1.0.0/24 in VPC 10.1.0.0/16
        |
EC2 Ubuntu 22.04
        |
Nginx reverse proxy :80
        |
Docker container :5000 -> Flask app :8080
        |
Demo in-memory student and marks data
```

Terraform declares the VPC, public subnet, route table, internet gateway, security group, EC2 instance and S3 bucket. Ansible then configures the operating system, Docker, Nginx and application deployment.

## Network rules

- TCP 22: SSH, restricted to the configured administrator CIDR.
- TCP 80: public HTTP for the assignment demo.
- TCP 8080: direct API testing, restricted to the configured administrator CIDR.
- Outbound: allowed for package and image downloads.

For a production design, remove direct public access to the application port, use HTTPS/TLS, use IAM roles with least privilege, put the app in private subnets, use a managed database, and add monitoring/backups.
