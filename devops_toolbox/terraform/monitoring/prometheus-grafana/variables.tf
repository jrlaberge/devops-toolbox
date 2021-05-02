variable "client_id" {}
variable "client_secret" {}

variable "agent_count" {
    default = 1
}

variable "ssh_public_key" {
    default = "~/.ssh/aks_promitor.pub"
}

variable "dns_prefix" {
    default = "promitor"
}

variable cluster_name {
    default = "promitorCluster"
}

variable resource_group_name {
    default = "promitorRG"
}

variable location {
    default = "Canada Central"
}

variable log_analytics_workspace_name {
    default = "promitorLogAnalyticsWorkspace"
}

# refer https://azure.microsoft.com/global-infrastructure/services/?products=monitor for log analytics available regions
variable log_analytics_workspace_location {
    default = "Canada Central"
}

# refer https://azure.microsoft.com/pricing/details/monitor/ for log analytics pricing 
variable log_analytics_workspace_sku {
    default = "Free"
}

variable servicebus_namespace_name {
    default = "promitor-servicebus-jl"
}

variable servicebus_queue_name {
    default = "promitor-queue"
}