# Echo server program
import socket

HOST = '192.168.31.215'                 # Symbolic name meaning all available interfaces
PORT = 7005              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print("recv :",data)
            if not data: break
            print("sent back ...")
            conn.sendall(data)