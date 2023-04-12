import socket

HOST = '192.168.8.101'  # pusty string oznacza dowolny adres IP
PORT = 80  # wybrany port

# Tworzenie gniazda sieciowego
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print('Serwer nasłuchuje na porcie', PORT)

# Oczekiwanie na połączenie
conn, addr = s.accept()

print(conn)

print('Połączono z', addr)

# Wysyłanie danych przez gniazdo
data = str('two')
conn.sendall(data.encode())

# Zamykanie połączenia
conn.close()
s.close()