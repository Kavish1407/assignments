variable "region"{
 default = "us-east-1"
}
variable "quantiphi_cidrs" {type = list}
variable "amis" {
	type="map"
	default={
	"us-east-1" = "ami-b374d5a5"
	"us-west-2" = "ami-4b32be2b"
	}

}
variable "instance_type"{
 default=  "t2.micro"

}
variable "Name"        {}
variable "email"       {}
variable "project"     {}
variable "office-time" {}
variable "number_of_instances" {}
variable "publickey" {}
