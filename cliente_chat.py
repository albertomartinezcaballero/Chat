import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port=8087
s.connect(('192.168.1.52',port))
while True :
	message = input("mensaje:")
	s.send(message.encode())

	print("Esperando respuesta")
	reply = s.recv(1024).decode('utf-8')
	print("Recibido: ",str(reply))
	if message == "exit":
		s.close()
		break
	if reply == "exit":
		print("El servidor ha cerrado la conexión")
		s.close()
		break
