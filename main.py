from pymongo import MongoClient 

con = MongoClient("mongodb://localhost:27017/")

db = con.get_database("sistema")

restaurante = db.get_collection("Restaurante")

usuario = db.get_collection("Usuarios")

reservas = db.get_collection("Reservas")


re = {
    "_id":1,
    "nome":"São Fogos",
    "endereço":"Rua Borges, 1200, Ferro até Tupi",
    "capacidade": 200
}

restaurante.insert_one(re)

usu = {
    "_id":1,
    "nome":"Dudu",
    "contato": 33390034
}

usuario.insert_one(usu)

res = {
    "data": 12/2,
    "hora": "20:00",
    "nº de pessoas": 40,
    "ID do restaurante":1,
    "ID do usuario":1,
}

reservas.insert_one(res)


#  id faço a mennor ideia de como faz :)