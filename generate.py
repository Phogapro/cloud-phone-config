import json
import os

<<<<<<< HEAD
with open("mapping.json", "r") as f:
=======
CONFIG_DIR = "configs"

with open("mapping.json", "r", encoding="utf-8") as f:
>>>>>>> c5cbd36 (update)
    data = json.load(f)

template = """
mixed-port: 7890
<<<<<<< HEAD
=======
allow-lan: false
mode: rule
log-level: info
>>>>>>> c5cbd36 (update)

proxies:
  - name: STATIC
    type: "{type}"
    server: "{proxy}"
    port: {port}
    username: "{user}"
    password: "{password}"
    udp: false

proxy-groups:
  - name: AUTO
    type: select
    proxies:
      - STATIC

rules:
  - MATCH,AUTO
"""

<<<<<<< HEAD
os.makedirs("configs", exist_ok=True)

for device, cfg in data.items():

=======
os.makedirs(CONFIG_DIR, exist_ok=True)

# ===== CREATE / UPDATE YAML =====

valid_files = set()

for device, cfg in data.items():

    filename = f"{device}.yaml"
    filepath = os.path.join(CONFIG_DIR, filename)

    valid_files.add(filename)

>>>>>>> c5cbd36 (update)
    yaml_content = template.format(
        type=cfg["type"],
        proxy=cfg["proxy"],
        port=cfg["port"],
        user=cfg["user"],
        password=cfg["pass"]
    )

<<<<<<< HEAD
    with open(f"configs/{device}.yaml", "w", encoding="utf-8") as f:
        f.write(yaml_content)

=======
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(yaml_content)

    print(f"[UPDATED] {filename}")

# ===== DELETE UNUSED YAML =====

for filename in os.listdir(CONFIG_DIR):

    if filename.endswith(".yaml"):

        if filename not in valid_files:

            filepath = os.path.join(CONFIG_DIR, filename)

            os.remove(filepath)

            print(f"[DELETED] {filename}")

>>>>>>> c5cbd36 (update)
print("DONE")