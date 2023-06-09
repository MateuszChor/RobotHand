import socket

class server:

    def __init__(self, ip, port):
        self.HOST = ip
        self.PORT = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.HOST, self.PORT))
        self.socket.listen(1)

    def accept(self):
        conn, addr = self.socket.accept()
        return conn, addr

    def receive(self, conn):
        data = conn.recv(1024)
        return data.decode()

    def send(self, conn, data):
        conn.send(data.encode())
    def close(self):
        self.socket.close()

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
