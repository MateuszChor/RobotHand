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

wybor = input(" 1 = Thumb_Up ,  2 = Thumb_Down : ")

if wybor == "1":
    # Wysyłanie danych przez gniazdo
    data = str('Thumb_Up')
    conn.sendall(data.encode())
    # Zamykanie połączenia
    conn.close()
    s.close()

if wybor == "2":
    # Wysyłanie danych przez gniazdo
    data = str('Thumb_Down')
    conn.sendall(data.encode())
    # Zamykanie połączenia
    conn.close()
    s.close()

else:
    print("exit")