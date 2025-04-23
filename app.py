from pymongo import MongoClient 
from flask import Flask, render_template

#  Sistema do MongoDB
client      = MongoClient("mongodb://localhost:27017/")
db          = client.get_database("sistema")
restaurante = db.get_collection("restaurante")
usuario     = db.get_collection("usuarios")
reservas    = db.get_collection("reserva")

def criar_reserva():
    data = input("Digite a data: ")
    hora = input("Digite a hora: ")
    numero_de_pessoas = int(input("Digite quantas pessoas: "))

    nova_reserva = {
        "data": data,
        "hora": hora,
        "numeroDePessoas":numero_de_pessoas
    }

    reservas.insert_one(nova_reserva)
    print("Reserva criada")

criar_reserva()

# def limpar():
#     resultado = reservas.delete_many({})
#     print(f"🗑️ {resultado.deleted_count} reservas apagadas.")
# limpar()


# filtro = {"status":"livre"}

# vaga_disponivel = reservas.find_one(filtro)

# if vaga_disponivel:
#     print("✅ Sim, há vagas disponíveis!")
# else:
#     print("❌ Não há vagas disponíveis no momento.")


# Interface
# app = Flask(__name__)

# @app.route("/base")
# def exibir_home():
#     # Parte principal no projeto 
#     return render_template("base.html")
  


# if __name__ == "__main__":
#     app.run(debug=True)



'''
1º Implemntar logica para vereficar se ha vagas disponivel 

2º Adicionar filtro para buscar restaurantes por localização ou tipo de cozinha

'''


























# # filtro pra identificar o restaurante
# filtro = {"_id": "67e5f70f4024726cc6ef6aac"}

# #  Atualização
# atualizacao = {"$set": {"numeroDePessoas": 6}}

# resultado = db.restaurantes.update_one(filtro, atualizacao)
# print(f"Documentos modificados: {resultado.modified_count}")


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


