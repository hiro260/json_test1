import json

with open ("data.json", "r") as f:
    data = json.load(f)

print(data["name"])
print(data["address"]["city"])

new_data = {"language": "python", "version": 3.11}
with open("config.json", "w") as f:
    json.dump(new_data, f)
