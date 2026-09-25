# Terraform patterns used in this showcase

The production implementation behind this portfolio uses Terraform modules for resource groups, workload identity, container registry, application runtime, secrets management, PostgreSQL, and observability. The public version intentionally documents the patterns without exposing production resource identifiers.

## Provider pinning

```hcl
terraform {
  required_version = ">= 1.6.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  features {}
}
```

## Naming and tags

```hcl
locals {
  prefix = "${var.workload}-${var.environment}"

  common_tags = {
    environment = var.environment
    managed_by  = "terraform"
    portfolio   = "sanitized-showcase"
  }
}
```

## Managed identity-first application runtime

```hcl
resource "azurerm_linux_web_app" "api" {
  name                = "${local.prefix}-api"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  service_plan_id     = azurerm_service_plan.main.id

  identity {
    type = "SystemAssigned"
  }

  site_config {
    always_on = true
  }

  tags = local.common_tags
}
```

## Security posture

Secrets are not embedded in Terraform source. Workloads use managed identity and retrieve permitted values from a secret store at runtime. CI/CD authentication uses federated identity rather than static client secrets.
