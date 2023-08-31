import socket

HOST = "127.0.0.1"
PORT = 54321

def enviarMsm(msm):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(msm.encode())  # Enviamos el mensaje como bytes
        data = s.recv(1024).decode()  # Recibimos la respuesta y la convertimos a string
        return data

while True:
    msm = input("Ingrese un mensaje: ")
    if msm.lower() == 'exit':
        break
    response =  enviarMsm(msm)
    print("Respuesta:", response)
