import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta que o servidor está ouvindo

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Servidor escutando...")
    conn, addr = s.accept()
    with conn:
        print(f"Conectado por {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Recebido: {data.decode('utf-8')}")
            conn.sendall(data) 