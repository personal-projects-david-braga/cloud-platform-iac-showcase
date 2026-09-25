# Security baseline

This public showcase documents the security controls used in the production-oriented platform pattern without exposing any real environment identifiers.

## Identity

- CI/CD uses federated workload identity instead of long-lived client secrets.
- Application workloads use managed identity where the target service supports it.
- Access is granted at the narrowest practical scope.
- Human and workload identities are separated.

## Secrets

- Secrets are not committed to Git.
- Runtime configuration contains secret references, not secret values.
- Rotation is handled independently from application builds.
- Local examples use placeholders only.

## Network and runtime

Typical production controls include HTTPS-only endpoints, minimum TLS versions, restricted ingress, private connectivity for data services where appropriate, container image provenance, health checks, and centralized diagnostics.

## Observability

The platform provisions logs and application telemetry together with the workload so operational evidence is available from the first deployment. Production environments should define retention, alerting, access controls, and cost limits explicitly.

## Delivery

Infrastructure changes follow pull-request review, static validation, plan review, controlled apply, post-deployment health validation, and documented rollback procedures.
