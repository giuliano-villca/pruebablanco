import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, 12345))


mensaje = client_socket.recv(1024).decode()
print(mensaje, end="")


usuario = input()
client_socket.send(usuario.encode())

while True:
    mensaje = client_socket.recv(1024).decode()
    print(mensaje, end="")
    comando = input()
    client_socket.send(comando.encode())
    respuesta = client_socket.recv(4096).decode()
    print(respuesta)
    if comando.strip() == "/adios":
        break

client_socket.close()
