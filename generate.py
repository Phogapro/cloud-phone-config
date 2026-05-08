import json
import os

with open("mapping.json", "r") as f:
    data = json.load(f)

template = """
mixed-port: 7890

proxies:
  - name: STATIC
    type: {type}
    server: {proxy}
    port: {port}
    username: {user}
    password: {password}

proxy-groups:
  - name: AUTO
    type: select
    proxies:
      - STATIC

rules:
  - MATCH,AUTO
"""

os.makedirs("configs", exist_ok=True)

for device, cfg in data.items():

    yaml_content = template.format(
        type=cfg["type"],
        proxy=cfg["proxy"],
        port=cfg["port"],
        user=cfg["user"],
        password=cfg["pass"]
    )

    with open(f"configs/{device}.yaml", "w") as f:
        f.write(yaml_content)

print("DONE")