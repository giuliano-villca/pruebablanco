import socket
import requests

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("nombre de la computadora (servidor): " + hostname)
print("dirección IP: " + ip)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip, 12345))
server_socket.listen(1)  

print("Servidor escuchando en el puerto 12345...")

while True:
    client_socket, address = server_socket.accept()
    print("Se conecto un cliente desde: " + str(address))
    
    client_socket.send("Hola we, pon tu nombre: ".encode())

    username = client_socket.recv(1024).decode().strip()
    print("Usuario recibido: " + username)

    while True:
 
        client_socket.send("Escribe  (/repos o /adios): ".encode())

        comando = client_socket.recv(1024).decode().strip()

        if comando == "/repos":
            try:
                r = requests.get("https://valorant-api.com/v1/agents?isPlayableCharacter=true")
                data = r.json()
                agentes = [a["displayName"] for a in data["data"]]
                mensaje = f"Hola {username}, estos son los agentes de Valorant (no me gusta el juego):\n" + "\n".join(agentes)
            except Exception as e:
                mensaje = "Error."

            client_socket.send(mensaje.encode())

        elif comando == "/adios":
            adios  = f"chau, {username}."
            client_socket.send(adios.encode())
            print(f"Cliente {username} se desconectp.")
            break
        else:
            client_socket.send("Comando no esta mal. /repos o /adios\n".encode())

    client_socket.close()
