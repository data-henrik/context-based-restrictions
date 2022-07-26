# retrieve default resource group
data "ibm_resource_group" "group" {
  name = "default"
}

# retrieve data for the Cloud Object Storage instance
data "ibm_resource_instance" "COS_instance" {
  name              = var.cos_instance_name
  location          = "global"
  resource_group_id = data.ibm_resource_group.group.id
  service           = "cloud-object-storage"
}

# retrieve account settings, especially the current account_id
data "ibm_iam_account_settings" "iam_account_settings" {
}

# create a network zone for Code Engine
resource "ibm_cbr_zone" "cbr_zone_CE" {
  account_id = data.ibm_iam_account_settings.iam_account_settings.account_id

  description = "TF-defined zone based for Code Engine"
  name        = "CodeEngine_Zone"
  addresses {
    type = "serviceRef"
    ref {
      account_id   = data.ibm_iam_account_settings.iam_account_settings.account_id
      service_name = "codeengine"
    }
  }
}

# create a rule that brings together 
# - the COS instance with the bucket "cbrbucket"
# - the Code Engine network zone
# - and the account_id
resource "ibm_cbr_rule" "cbr_rule_COS" {
  contexts {
    attributes {
      name  = "networkZoneId"
      value = ibm_cbr_zone.cbr_zone_CE.id
    }
  }
  description      = "TF-defined rule for CE to COS"
  enforcement_mode = "enabled"
  resources {
    attributes {
      name  = "accountId"
      value = data.ibm_iam_account_settings.iam_account_settings.account_id
    }
    attributes {
      name     = "resource"
      operator = "stringEquals"
      value    = "cbrbucket"
    }
    attributes {
      name     = "serviceInstance"
      operator = "stringEquals"
      value    = data.ibm_resource_instance.COS_instance.guid
    }
    attributes {
      name     = "serviceName"
      operator = ""
      value    = "cloud-object-storage"
    }
  }
}
