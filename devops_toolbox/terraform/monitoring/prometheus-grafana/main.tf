terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "2.57.0"
    }
  }
}

provider "azurerm" {
  # Configuration options
  features {}
}