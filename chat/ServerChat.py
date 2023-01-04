import socket
from threading import Thread
import threading


def server(ip: str, port: int) -> None: 
  
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #conexao tcp
  sock.bind((ip, port)) #atribui ao meu servidor um ip e porta #reaproveito endereco
  sock.listen() # passou nada, atribui valor mais alto
  print(f"Server started at {ip, port}")
  while True:
    threading.Thread(target = response_to_clients, args = (sock, )).start()
    #threading.Thread(target = treat_client, args = (sock, )).start()
    
def response_to_clients(clienteSocket) -> None:
  client, client_adress = clienteSocket.accept()
  while True: 
    #client, client_adress = sock.accept()
    print(f" Client {client_adress}")
    print(f" Client say: {client.recv(2048).decode()}")
    response = input("Send: ").encode() #le a entrada pelo teclado e comenta como byte
    client.send(response)
    
#def treat_client(cliente):
   
if __name__ == '__main__':
  IP = 'localhost'
  PORT = 6669
  server(IP, PORT)