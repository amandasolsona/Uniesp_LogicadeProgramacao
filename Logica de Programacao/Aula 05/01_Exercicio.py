import json

json_data = '{"nome": "Amanda", "id": 1, "saldo": 5000}'
data = json.loads(json_data)

print(data["nome"])
print(data["id"])
print(data["saldo"])

#Abastecer o JSON através do input do usuário.
#Características é igual a atributos;