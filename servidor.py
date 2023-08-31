import socket

HOST = "127.0.0.1"
PORT = 54321

def comandos(data):
    if data.startswith('/'):
        return "comando recibido"
    return "mensaje recibido: " + data

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Conectado desde {addr}")
        while True:
            data = conn.recv(1024).decode()  
            if not data:
                break
            response = comandos(data)
            conn.sendall(response.encode()) 
            if response == "comando recibido":
                new_data = conn.recv(1024).decode()  
                conn.sendall(b"/")  
                print(f"Nuevo mensaje recibido del cliente: {new_data}")
