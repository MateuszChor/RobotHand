import socket
from Secret.Secret import serwer_ip, serwer_ip_laptop

HOST = serwer_ip_laptop
PORT = 80

while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)


    print('Lisening on port :', PORT)

    conn, addr = s.accept()

    print(conn)

    print('Connected with', addr)

    choice = input(" 1 = Thumb_Up ,  2 = Thumb_Down :  ,  3 = Forefinger_Up , 4 = Forefinger_Down , 5 = Middle_Up , 6 = Middle_Down , 7 = Ring_finger_Up , 8 = Ring_finger_Down , 9 = Little_finger_Up , 10 = Little_finger_Down \
                   or exit to exit -- :")

    if choice == "1":
        data = str('Thumb_Up')
        conn.sendall(data.encode())
        conn.close()
        s.close()

    elif choice == "2":
        data = str('Thumb_Down')
        conn.sendall(data.encode())
        conn.close()
        s.close()

    elif choice == "3":
        data = str('Forefinger_Up')
        conn.sendall(data.encode())
        conn.close()
        s.close()

    elif choice == "4":
        data = str('Forefinger_Down')
        conn.sendall(data.encode())
        conn.close()
        s.close()

    elif choice == "5":
        data = str('Middle_Up')
        conn.sendall(data.encode())
        conn.close()
        s.close()

    elif choice == "6":
        data = str('Middle_Down')
        conn.sendall(data.encode())
        conn.close()
        s.close()

    elif choice == "7":
        data = str('Ring_finger_Up')
        conn.sendall(data.encode())
        conn.close()
        s.close()

    elif choice == "8":
        data = str('Ring_finger_Down')
        conn.sendall(data.encode())
        conn.close()
        s.close()

    elif choice == "9":
        data = str('Little_finger_Up')
        conn.sendall(data.encode())
        conn.close()
        s.close()

    elif choice == "10":
        data = str('Little_finger_Down')
        conn.sendall(data.encode())
        conn.close()
        s.close()

    else:
        print("exit")   
        break