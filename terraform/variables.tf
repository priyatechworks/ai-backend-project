variable "region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "ami_id" {
  description = "AWS machine image"
  default     = "ami-0c55b159cbfafe1f0"
}

variable "instance_type" {
  description = "Server size"
  default     = "t2.micro"
}