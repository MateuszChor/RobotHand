import socket


HOST = '192.168.8.101'  # pusty string oznacza dowolny adres IP
PORT = 80  # wybrany port


while True:
    
    # Tworzenie gniazda sieciowego
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)


    print('Serwer nasłuchuje na porcie', PORT)

    # Oczekiwanie na połączenie
    conn, addr = s.accept()

    print(conn)

    print('Połączono z', addr)

    wybor = input(" 1 = Thumb_Up ,  2 = Thumb_Down :  ,  3 = Forefinger_Up , 4 = Forefinger_Down , 5 = Middle_Up , 6 = Middle_Down , 7 = Ring_finger_Up , 8 = Ring_finger_Down , 9 = Little_finger_Up , 10 = Little_finger_Down \
                   or exit to exit -- :" )

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

    if wybor == "3":
        # Wysyłanie danych przez gniazdo
        data = str('Forefinger_Up')
        conn.sendall(data.encode())
        # Zamykanie połączenia
        conn.close()
        s.close()

    if wybor == "4":
        # Wysyłanie danych przez gniazdo
        data = str('Forefinger_Down')
        conn.sendall(data.encode())
        # Zamykanie połączenia
        conn.close()
        s.close()

    if wybor == "5":
        # Wysyłanie danych przez gniazdo
        data = str('Middle_Up')
        conn.sendall(data.encode())
        # Zamykanie połączenia
        conn.close()
        s.close()

    if wybor == "6":
        # Wysyłanie danych przez gniazdo
        data = str('Middle_Down')
        conn.sendall(data.encode())
        # Zamykanie połączenia
        conn.close()
        s.close()

    if wybor == "7":
        # Wysyłanie danych przez gniazdo
        data = str('Ring_finger_Up')
        conn.sendall(data.encode())
        # Zamykanie połączenia
        conn.close()
        s.close()

    if wybor == "8":
        # Wysyłanie danych przez gniazdo
        data = str('Ring_finger_Down')
        conn.sendall(data.encode())
        # Zamykanie połączenia
        conn.close()
        s.close()

    if wybor == "9":
        # Wysyłanie danych przez gniazdo
        data = str('Little_finger_Up')
        conn.sendall(data.encode())
        # Zamykanie połączenia
        conn.close()
        s.close()

    if wybor == "10":
        # Wysyłanie danych przez gniazdo
        data = str('Little_finger_Down')
        conn.sendall(data.encode())
        # Zamykanie połączenia
        conn.close()
        s.close()

    if wybor == "exit":
        print("exit")
        break