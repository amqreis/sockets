#!/usr/bin/env python3

import socket

# Criamos o socket usando um nome diferente da biblioteca (server_socket)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Evita o erro de "Porta já em uso" se você reiniciar o servidor rápido
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(("localhost", 9473))
server_socket.listen()

print("Aguardando conexão...")
conn, addr = server_socket.accept()
print(f"Conectado com sucesso por: {addr}")

while True:
    data = conn.recv(43444)
    if not data:
        print("Cliente desconectou.")
        break
    print("Nova mensagem do host %s: %s" % (addr, data.decode()))

# O close agora fica FORA do while. Só fecha quando o loop terminar!
conn.close()
server_socket.close()
    
