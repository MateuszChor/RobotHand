from Conntrol_server.MotorServer import Server
from Secret.Secret import serwer_ip, serwer_ip_laptop, ip_esp

servo = Server(serwer_ip, 80)


conn, addr = servo.accept()

servo.send(conn, "Middle_Down")

conn.close()
servo.close()
