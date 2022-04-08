import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://lowcke:Raposa12@minerva01.ct8ft.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
global mydb
mydb = client.MercadoDitadura

def findSort():
    #Sort
    global mydb
    mycol = mydb.usuario
    print("\n####SORT####")
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        print(x)

def findQuery():
    #Query
    global mydb
    mycol = mydb.usuario
    print("\n####QUERY####")
    myquery = { "nome": "Rafinha Bastos" }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)

def insert():
    #Insert
    global mydb
    mycol = mydb.usuario
    print("\n####INSERT####")
    mydict = { "nome": "Nathan da Motta Truyts" ,"cpf":"006.126-53.45", "email":"Nathan da Motta Truyts", "endereco":"Rua padre eugenio"}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def delete():
    #Delete
    global mydb
    mycol = mydb.Cupons
    print("\n####DELETE####")
    myquery = { "nome": "Heat30" }
    mycol.delete_one(myquery)
    for x in mycol.find():
     print(x)

def Update():
    #Update
    global mydb
    mycol = mydb.usuario
    print("\n####UPDATE####")
    myquery = { "nome": "Rafinha Bastos" }
    newvalues = { "$set": { "nome": "Rafael Bastos Hocsman" } }
    mycol.update_one(myquery, newvalues)
    for x in mycol.find():
     print(x) 



#main
findSort()
findQuery()
insert()
delete()
Update()
