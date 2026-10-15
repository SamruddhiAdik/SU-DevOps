output "app_server_public_ip" {
  description = "Public IP of the EC2 instance; use in Ansible inventory."
  value       = aws_instance.app.public_ip
}

output "app_url" {
  description = "HTTP URL for the deployed application after Ansible completes."
  value       = "http://${aws_instance.app.public_ip}"
}

output "backup_bucket_name" {
  description = "Private S3 bucket with encryption and versioning enabled."
  value       = aws_s3_bucket.backup.bucket
}
