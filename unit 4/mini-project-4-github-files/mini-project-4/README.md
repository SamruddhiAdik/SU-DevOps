# Mini Project 4 — Student Record & Academic Management Platform
## Infrastructure Automation using Terraform, Ansible and AWS

This repository is a student-friendly starter implementation based on the Unit 4 assignment. It demonstrates:
- **Terraform**: AWS VPC, public subnet, route table, security group, EC2 and encrypted/versioned S3 bucket.
- **Ansible**: common system setup, Docker, Nginx reverse proxy and application deployment roles.
- **Flask API**: `/api/health`, `/api/students`, and `POST /api/marks`.
- **Validation**: smoke-test script and a technical report template.

> **Important:** This is an educational starter, not a production-ready system. AWS resources can incur charges. Review the Terraform plan and AWS pricing before applying. Never commit AWS keys, SSH private keys, passwords, Terraform state, or real student data.

## Repository structure

```text
mini-project-4/
├── .gitignore
├── README.md
├── requirements.txt
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── tests/
│   └── test_app.py
├── scripts/
│   └── smoke-test.sh
├── docs/
│   ├── architecture.md
│   ├── implementation-report.md
│   └── deployment-checklist.md
├── terraform/
│   ├── versions.tf
│   ├── variables.tf
│   ├── main.tf
│   ├── outputs.tf
│   └── terraform.tfvars.example
└── ansible/
    ├── ansible.cfg
    ├── inventory.ini.example
    ├── site.yml
    ├── group_vars/all.yml
    └── roles/
        ├── common/tasks/main.yml
        ├── docker/tasks/main.yml
        ├── nginx/tasks/main.yml
        ├── nginx/templates/student-platform.conf.j2
        └── student_app/tasks/main.yml
```

## Prerequisites

- Git and a GitHub account
- Python 3.10+ for local API testing
- Docker (optional for local container run)
- Terraform 1.7+
- Ansible 2.16+
- An AWS account with permissions to create EC2, VPC, security groups and S3 resources
- An SSH key pair for the target EC2 instance

## 1. Run the API locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python app/app.py
```

In another terminal:
```bash
curl http://127.0.0.1:8080/api/health
curl http://127.0.0.1:8080/api/students
curl -X POST http://127.0.0.1:8080/api/marks \
  -H "Content-Type: application/json" \
  -d '{"student_id": 1, "course": "Cloud Computing", "marks": 88}'
```

The sample uses an in-memory dataset for easy demonstrations. Data resets when the app restarts; do not use real student data.

## 2. Configure AWS and Terraform

Configure AWS credentials using your normal AWS CLI profile or environment variables. **Do not put access keys in Terraform files.**

```bash
cd terraform
cp terraform.tfvars.example terraform.tfvars
```

Edit `terraform.tfvars`:
- Set `key_name` to an existing EC2 key pair in your AWS region.
- Set `admin_cidr` to your public IP followed by `/32` (example format: `203.0.113.10/32`; replace with your actual IP).
- Keep the region and instance settings appropriate for your account.

Then:
```bash
terraform init
terraform fmt -recursive
terraform validate
terraform plan
```

Review the plan carefully before creating anything:
```bash
terraform apply
```

Copy the output `app_server_public_ip`. **The example security group intentionally limits SSH to `admin_cidr`; do not open SSH to the whole internet.** Port 8080 is also available for the API demo and should be restricted further for real deployments.

## 3. Configure Ansible and deploy

From the project root:
```bash
cp ansible/inventory.ini.example ansible/inventory.ini
```
Edit `ansible/inventory.ini` with the Terraform public IP, the matching private-key path, and the correct SSH user (`ubuntu` for the selected Ubuntu AMI).

Check connectivity:
```bash
ansible -i ansible/inventory.ini student_servers -m ping
```

Run the playbook:
```bash
ansible-playbook -i ansible/inventory.ini ansible/site.yml
```

The playbook installs Docker and Nginx, builds the application image on the EC2 host, runs the app on internal port 5000, and configures Nginx on port 80 to proxy to it.

## 4. Verify deployment

```bash
bash scripts/smoke-test.sh http://YOUR_EC2_PUBLIC_IP
```

Expected endpoints:
- `GET /api/health` → JSON status `UP`
- `GET /api/students` → sample student list
- `POST /api/marks` → saved sample mark response

## 5. Clean up AWS resources

When you have finished and saved any required evidence:
```bash
cd terraform
terraform destroy
```
Read the destroy plan before confirming. The S3 bucket is configured to allow safe destruction only when empty. If you put files into it, remove them deliberately after confirming they are not needed.

## Assignment deliverables checklist

- [ ] Terraform HCL for VPC, subnet, security group, EC2 and S3
- [ ] Modular Ansible roles for common setup, Docker, Nginx and app deployment
- [ ] Deployed application reachable through EC2 public IP on port 80
- [ ] Smoke-test output and architecture notes
- [ ] GitHub repository URL included in report
