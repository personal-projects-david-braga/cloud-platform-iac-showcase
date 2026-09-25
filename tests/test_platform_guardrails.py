from tools.platform_guardrails import PlatformResource, validate_resource


def test_valid_resource_passes() -> None:
    resource = PlatformResource(
        name="portfolio-prod-api",
        tags={"environment": "prod", "managed_by": "terraform", "owner": "platform"},
    )
    assert validate_resource(resource) == []


def test_invalid_resource_reports_naming_and_tags() -> None:
    resource = PlatformResource(
        name="Portfolio_API",
        tags={"environment": "prod"},
    )
    errors = validate_resource(resource)
    assert any("lowercase" in error for error in errors)
    assert any("hyphens" in error for error in errors)
    assert any("missing required tags" in error for error in errors)
