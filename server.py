'''
Server will be receiving connection from 
client 
'''

import socket
import threading
import time


class Server:
	#-------Creating node for TCP communication protocol--------
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#------Default Local host--------
	host = "127.0.0.1"
	#If you want to send over wifi replace host with your IP address
	port = 5050
	#Select random port except those ones set for default functions



	def __init__(self):
		server_config = (self.host, self.port)
		self.server.bind(server_config)
		self.server.listen(5)

		#---------Accepting connection from client---------

		self.clientsocket, self.addr = self.server.accept()
		print("Get connecting from ", self.addr)


	#--------chatting function-----------

	def receive_sms(self):
		''' Receiving connection from the client'''
		try:
			while True:	
				data = self.clientsocket.recv(1024).decode()
				time.sleep(0.001)
				print(data)
		except Exception as ex:
			print("The below error have occured please checkout")
			print(ex)

	def chat(self):
		self.Receiving_ciao = threading.Thread(target = self.receive_sms)
		self.Receiving_ciao.daemon = True
		self.Receiving_ciao.start()
		while True:
			server_message = input()
			server_message = "\nserver:{}\n".format(server_message)
			self.clientsocket.send(server_message.encode())


if __name__ =='__main__':
	Server_m = Server()
	Server_m.chat()
	Server_m.Receiving_ciao.join()
	server.close()