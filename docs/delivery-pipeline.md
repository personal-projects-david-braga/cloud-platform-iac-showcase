# Infrastructure delivery pipeline

A production-grade infrastructure workflow should separate validation from deployment and preserve evidence for every change.

## Pull request

1. Format check
2. Static validation
3. Security/policy checks
4. Plan generation
5. Human review of the plan

## Merge / controlled deployment

1. Authenticate through federated identity
2. Recreate the reviewed plan against the target environment
3. Apply with environment protection
4. Run health checks
5. Emit deployment metadata to the observability platform

## Rollback posture

Infrastructure rollback is not treated as a blind reverse-apply. Data services and stateful workloads require explicit recovery procedures, backups, and compatibility checks.

## Example GitHub Actions shape

```yaml
permissions:
  id-token: write
  contents: read

steps:
  - uses: actions/checkout@v4
  - name: Terraform format
    run: terraform fmt -check -recursive
  - name: Terraform validate
    run: terraform validate
  - name: Terraform plan
    run: terraform plan -out=tfplan
```

Real environment names, subscription identifiers, backend coordinates, and credentials are intentionally excluded from this public repository.
