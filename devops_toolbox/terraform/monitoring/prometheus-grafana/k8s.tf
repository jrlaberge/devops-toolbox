resource "azurerm_resource_group" "k8s" {
    name     = var.resource_group_name
    location = var.location
}

resource "azurerm_servicebus_namespace" "k8s_ns" {
    name                = var.servicebus_namespace_name
    location            = azurerm_resource_group.k8s.location
    resource_group_name = azurerm_resource_group.k8s.name
    sku                 = "Standard"

    tags = {
        source = "terraform"
    }
}

resource "azurerm_servicebus_queue" "k8s_sbus_queue" {
    name                = var.servicebus_queue_name
    resource_group_name = azurerm_resource_group.k8s.name
    namespace_name      = azurerm_servicebus_namespace.k8s_ns.name
}

resource "random_id" "log_analytics_workspace_name_suffix" {
    byte_length = 8
}

resource "azurerm_log_analytics_workspace" "test" {
    # Workspace name must be globally unique across all of Azure
    name                = "${var.log_analytics_workspace_name}-${random_id.log_analytics_workspace_name_suffix.dec}"
    location            = var.log_analytics_workspace_location
    resource_group_name = azurerm_resource_group.k8s.name
    sku                 = var.log_analytics_workspace_sku
}



resource "azurerm_kubernetes_cluster" "k8s" {
    name                = var.cluster_name
    location            = azurerm_resource_group.k8s.location
    resource_group_name = azurerm_resource_group.k8s.name
    dns_prefix          = var.dns_prefix

    linux_profile {
        admin_username = "aks_user"

        ssh_key {
            key_data = file(var.ssh_public_key)
        }
    }

    default_node_pool {
        name       = "agentpool"
        node_count = var.agent_count
        vm_size    = "Standard_D2_V2"
    }

    service_principal {
        client_id     = var.client_id
        client_secret = var.client_secret
    }

    addon_profile {
        oms_agent {
            enabled                    = true
            log_analytics_workspace_id = azurerm_log_analytics_workspace.test.id
        }
    }

    network_profile {
        load_balancer_sku = "Standard"
        network_plugin    = "kubenet"
    }

    tags = {
        Environment = "Development"
    }
}

