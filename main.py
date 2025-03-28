from pymongo import MongoClient 

con = MongoClient("mongodb://localhost:27017/")
db = con.get_database("sistema")
restaurante = db.get_collection("Restaurante")
usuario = db.get_collection("Usuarios")
reservas = db.get_collection("Reservas")

# filtro pra identificar o restaurante
filtro = {"_id": "67e5f70f4024726cc6ef6aac"}

#  Atualização
atualizacao = {"$set": {"numeroDePessoas": 6}}

resultado = db.restaurantes.update_one(filtro, atualizacao)
print(f"Documentos modificados: {resultado.modified_count}")

# restaurante = {
#     "nome":"Restaurante Delicia",
#     "endereco":"Rua Principal, 123",
#     "capacidade":50
# }

# resultado = db.restaurante.insert_one(restaurante)
# print(f"Restaurante criado com ID:{resultado.inserted_id}") # 

# usuario = {
#     "nome":"Pablo",
#     "contato":"+55 19 99999-9999"
# }

# resultado = db.usuario.insert_one(usuario)
# print(f"Usuario criado com ID: {resultado.inserted_id}") 

# reserva = {
#     "data":"2025-04-28",
#     "hora":"19:00",
#     "numeroDePessoas":4,
#     "restauranteID":resultado.inserted_id,
#     "usuarioID":resultado.inserted_id
# }

# resultado_reserva = db.reserva.insert_one(reserva)
# print(f"Reserva criada com ID: {resultado_reserva.inserted_id}")


