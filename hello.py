from pathlib import Path
import os

# Load the local .env file (dummy data only)
env_path = Path(__file__).with_name(".env")
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key, value)

print(os.getenv("EXAMPLE_ONLY", "hello"))
