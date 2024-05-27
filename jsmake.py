import json

ip = input("ip: ")
username = input("uesrname: ")
port = int(input("port: "))
key = input("path to key: ")
password = input("path to password file: ")
server_name = input("server name: ") + ".json"

data = {
    "ip": ip,
    "username": username,
    "port": port,
    "key": key,
    "password": password
}

with open(server_name, 'w') as file:
    json.dump(data, file)
