# Deployment Checklist

## Before provisioning
- [ ] AWS CLI credentials configured outside the repository
- [ ] Correct AWS region selected
- [ ] Existing EC2 key pair name configured
- [ ] `admin_cidr` set to administrator public IP `/32`
- [ ] Terraform files formatted, validated, and plan reviewed
- [ ] Budget/cost implications reviewed

## After provisioning
- [ ] EC2 public IP captured from Terraform output
- [ ] SSH connectivity verified
- [ ] Ansible ping succeeded
- [ ] Ansible playbook completed
- [ ] HTTP port 80 reachable
- [ ] API health, students, and marks endpoints smoke-tested
- [ ] Screenshots/logs captured for report

## Cleanup
- [ ] `terraform destroy` plan reviewed
- [ ] Resources no longer needed have been deleted
- [ ] No credentials, private keys, state files, or real student records committed
