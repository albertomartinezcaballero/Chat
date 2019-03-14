import socket

def clientHandler(connection, client_address):
    print ('connected by',client_address)
    while True :
        data = (connection.recv(1024)).decode('utf-8')

        if data == "exit":
            reply = "Gracias por todo"
            connection.sendall(reply.encode())
            connection.close()
            print("Conexion con ", client_address," cerrada")
            break

        print ("Recibido: ", str(data))
        reply = input("Respuesta: ")
        connection.sendall(reply.encode())
        if reply == "exit":
            print("Cerrando conexión con el cliente",client_address)
            connection.close()
            break

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host= socket.gethostname()
port=8087

s.bind(('192.168.1.52',port))

s.listen()

print("server is running")
while True:
    connection, client_address=s.accept()
    clientHandler(connection, client_address)
s.close()
