from AI_Server.WIFI_send_serwer import Server_motor
from Secret.Secret import serwer_ip, serwer_ip_laptop, ip_esp

servo = Server_motor(serwer_ip, 80)


conn, addr = servo.accept()

servo.send(conn, "Middle_Down")

conn.close()
servo.close()
