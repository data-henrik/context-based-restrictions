variable "ibmcloud_api_key" {}

variable "region" {}

variable "cos_instance_name" {}

variable "ibmcloud_timeout" {
  description = "Timeout for API operations in seconds."
  default     = 900
}