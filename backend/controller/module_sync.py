from pathlib import Path

ROUTERS_PATH = Path("routes")

SKIP_MODULES = {
    "auth_routes",
    "__init__",
}


def get_router_modules():
    modules = []

    for file in ROUTERS_PATH.glob("*.py"):
        module_name = file.stem.replace("_routes", "")

        if module_name in SKIP_MODULES:
            continue

        modules.append(module_name)

    return modules
if __name__ == "__main__":
    print(get_router_modules())