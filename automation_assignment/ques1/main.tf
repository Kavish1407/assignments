resource "aws_instance" "example" {
 
  ami             = var.amis[var.region]
  instance_type   = var.instance_type
  security_groups = aws_security_group.allow_ssh_http.*.name
  count           = var.number_of_instances
  key_name        = aws_key_pair.deployer.key_name
  tags = {
  Name  = "${var.Name}${count.index+1}" 
  email = var.email
  office-time = var.office-time
  project = var.project		
}

}

resource "aws_key_pair" "deployer" {
  key_name   = "k-tera-key"
  public_key = var.publickey
}

resource "aws_security_group" "allow_ssh_http" {
  name        = "k_allow_ssh_http"
  description = "Allow ssh and http inbound traffic"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = var.quantiphi_cidrs
  }
  ingress {
	from_port   = 80
	to_port     = 80
	protocol    = "tcp"
	cidr_blocks = var.quantiphi_cidrs
	
 }

}
output "ip"{
 value = ["${aws_instance.example.*.public_ip}"]
}

output "security_group_id"{
value=aws_security_group.allow_ssh_http.id
}
