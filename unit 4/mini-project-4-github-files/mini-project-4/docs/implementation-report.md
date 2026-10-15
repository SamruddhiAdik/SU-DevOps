# Mini Project 4 — Implementation Report

## 1. Objective
Automate cloud infrastructure provisioning and application configuration for the Student Record & Academic Management Platform using Terraform and Ansible on AWS.

## 2. Tools
- AWS: VPC, subnet, internet gateway, route table, security group, EC2, S3
- Terraform: declarative Infrastructure as Code
- Ansible: agentless, idempotent configuration management over SSH
- Docker: packages the Flask API
- Nginx: reverse proxy on port 80
- Flask/Pytest: demo API and automated tests

## 3. Terraform implementation
Describe the resources in `terraform/`, summarize the `terraform validate` and `terraform plan` output, and attach screenshots of the successful deployment.

## 4. Ansible implementation
Describe the `common`, `docker`, `nginx`, and `student_app` roles. Include output from `ansible-playbook` and explain why rerunning an idempotent playbook should not repeat unnecessary changes.

## 5. Validation
Record the results of:
- Network/SSH reachability
- Docker and Nginx service status
- Application container status
- `GET /api/health`
- `GET /api/students`
- `POST /api/marks`

## 6. Results and limitations
Document what worked, any errors, and any changes made. The included API stores demo records in memory and is not intended for real student data.

## 7. GitHub repository
Paste the repository URL here: `https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`

## 8. Cleanup
Confirm whether `terraform destroy` was run and that no unneeded AWS resources remain.
