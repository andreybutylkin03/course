import json

dbname = input("dbname: ")
user = input("username: ")
port = int(input("port: "))
host = input("host: ")
password = input("password: ")

data = {
    "dbname": dbname,
    "user": user,
    "port": port,
    "host": host,
    "password": password
}

with open('db_name.json', 'w') as file:
    json.dump(data, file)
