import socket

def cliente() -> None:
  msg = ""
  sock = socket.socket()
  sock.connect(('localhost', 6669))
  while True:
      msg_send = input("You: ").encode('utf-8')
      sock.send(msg_send)
      msg = sock.recv(2048)
      print(f"Server :", msg.decode('utf-8'))
if __name__ == '__main__':
  cliente()