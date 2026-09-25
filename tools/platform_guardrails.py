from dataclasses import dataclass


REQUIRED_TAGS = {"environment", "managed_by", "owner"}


@dataclass(frozen=True)
class PlatformResource:
    name: str
    tags: dict[str, str]


def validate_resource(resource: PlatformResource) -> list[str]:
    errors: list[str] = []

    if resource.name != resource.name.lower():
        errors.append("resource name must be lowercase")

    if " " in resource.name or "_" in resource.name:
        errors.append("resource name must use hyphens instead of spaces/underscores")

    missing = REQUIRED_TAGS.difference(resource.tags)
    if missing:
        errors.append("missing required tags: " + ", ".join(sorted(missing)))

    return errors
