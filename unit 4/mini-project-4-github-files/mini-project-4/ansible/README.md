# Ansible

Install the required collection first:

```bash
ansible-galaxy collection install -r ansible/requirements.yml
```

Copy `inventory.ini.example` to `inventory.ini`, then replace the example IP and key path. From the project root, run:

```bash
ansible -i ansible/inventory.ini student_servers -m ping
ansible-playbook -i ansible/inventory.ini ansible/site.yml
```

The playbook uses reusable roles: `common`, `docker`, `nginx`, and `student_app`. Ansible communicates over SSH and should be safe to rerun; review task output for changes and failures.
