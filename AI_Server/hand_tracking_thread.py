import socket
import threading


class Server_motor:
    def __init__(self, ip, port):
        self.HOST = ip
        self.PORT = port
        # Tworzenie gniazda sieciowego
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.HOST, self.PORT))
        self.sock.listen(1)

        print('Serwer nasłuchuje na porcie', self.PORT)
        self.thread = threading.Thread(target=self.run_server)

    def start(self):
        self.thread.start()

    def run_server(self):
        while True:
            conn, addr = self.socket.accept()
            print(f"New connection from {addr}")
            message = 'Forefinger_Down'
            conn.send(message.encode())
            conn.close()


    def accept(self):
        conn, addr = self.s.accept()
        return conn, addr

    def receive(self, conn):
        data = conn.recv(1024)
        return data.decode()

    def send(self, conn, data):
        conn.send(data.encode())
    def close(self):
        self.socket.close()
        self.thread.join()

# 'Thumb_Up'
#
# 'Thumb_Down'
#
# 'Forefinger_Up'
#
# 'Forefinger_Down'
#
# 'Middle_Up'
#
# 'Middle_Down'
#
# 'Ring_finger_Up'
#
# 'Ring_finger_Down'
#
# 'Little_finger_Up'
#
# 'Little_finger_Down'
