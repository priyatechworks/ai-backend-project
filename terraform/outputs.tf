output "server_ip" {
  description = "Public IP of server"
  value       = aws_instance.ai_backend.public_ip
}