from dataclasses import dataclass


@dataclass(frozen=True)
class ResourceName:
    workload: str
    environment: str
    component: str

    def render(self) -> str:
        parts = (self.workload, self.environment, self.component)
        return "-".join(part.strip().lower().replace("_", "-") for part in parts)


if __name__ == "__main__":
    print(ResourceName("portfolio", "prod", "api").render())
