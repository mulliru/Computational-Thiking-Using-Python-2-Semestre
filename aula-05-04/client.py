import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta que o servidor está ouvindo

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Codifique a string 'Olá, servidor!' usando UTF-8 antes de enviá-la
    mensagem = 'Olá, servidor!'.encode('utf-8')
    s.sendall(mensagem)
    data = s.recv(1024)

print(f"Recebido: {data.decode('utf-8')}")