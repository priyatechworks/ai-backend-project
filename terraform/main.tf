# Tell Terraform to use AWS
provider "aws" {
  region = var.region
}

# Create a server on AWS
resource "aws_instance" "ai_backend" {
  ami           = var.ami_id
  instance_type = var.instance_type

  tags = {
    Name = "ai-backend-server"
  }
}