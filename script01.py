import json

# Load JSON from a file
with open("data.json", "r") as f:
    data = json.load(f)

print(data["name"])  # Hiro