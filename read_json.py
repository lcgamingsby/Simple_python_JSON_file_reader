import json

file_json = open("data.json")

data = json.loads(file_json.read())

print(f"Nama: {data['name']}")
print(f"Website: {data['web']}")
print("Sosial Media:")
print(f"- Facebook: {data['social_media']['facebook']}")
print(f"- Twitter: {data['social_media']['twitter']}")