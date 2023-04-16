import cv2
from cvzone.HandTrackingModule import HandDetector
from WIFI_send_serwer import Server_motor
from Secret.Secret import serwer_ip, serwer_ip_laptop, ip_esp
import threading

class DisplayThread(threading.Thread):
    def __init__(self, frame):
        threading.Thread.__init__(self)
        self.frame = frame

    def run(self):
        cv2.imshow("Frame", self.frame)
        key = cv2.waitKey(1)
        while key != 27:  # czekaj na naciśnięcie klawisza ESC
            key = cv2.waitKey(1)
        cv2.destroyAllWindows()

class ProcessThread(threading.Thread):
    def __init__(self, cap, lock):
        threading.Thread.__init__(self)
        self.cap = cap
        self.lock = lock

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            with self.lock:
                self.frame = frame

    def get_frame(self):
        with self.lock:
            return self.frame

cap = cv2.VideoCapture(0)
lock = threading.Lock()
process_thread = ProcessThread(cap, lock)
process_thread.start()

detector = HandDetector(detectionCon=1, maxHands=1)

fingerTip = [4, 8, 12, 16, 20]
fingerVal = [0, 0, 0, 0, 0]
lastData = 00000

red = (0, 0, 255)
yellow = (0, 255, 255)
blue = (255, 0, 0)
green = (0, 255, 0)
purple = (255, 0, 255)

color = [red, yellow, blue, green, purple]
thumb_up = True
thumb_down = True

while cap.isOpened():
    frame = process_thread.get_frame()

    servo_server = Server_motor(serwer_ip_laptop, 80)
    conn, addr = servo_server.accept()
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if frame is None:
        break

    display_thread = DisplayThread(img)
    display_thread.start()
    display_thread.join()

    if lmList:
        handType = detector.handType()
        print(handType)

        # right hand
        if handType == "Right":
            # Thumb
            if lmList[fingerTip[0]][0] > lmList[fingerTip[0]-1][0]:
                thumb_up = True
                if thumb_down:
                    servo_server.send(conn, "Thumb_Up")
                    thumb_down = False

            else:
                thumb_down = True
                if thumb_up:
                    servo_server.send(conn, "Thumb_Down")
                    thumb_up = False

            # 4 fingers
            for i in range(1, 5):
                if lmList[fingerTip[i]][1] < lmList[fingerTip[i] - 2][1]:
                    fingerVal[i] = 1
                else:
                    fingerVal[i] = 0

        # left hand
        else:
            if lmList[fingerTip[0]][0] < lmList[fingerTip[0]-1][0]:
                servo_server.send(conn, "Thumb_Up")

            else:
                servo_server.send(conn, "Thumb_Down")

            # 4 fingers
            for i in range(1, 5):
                if lmList[fingerTip[i]][1] > lmList[fingerTip[i] - 2][1]:
                    fingerVal[i] = 1
                else:
                    fingerVal[i] = 0

        #Draw mark
        for i in range(0, 5):
            if fingerVal[i] == 1:
                cv2.circle(img, (lmList[fingerTip[i]][0], lmList[fingerTip[i]][1]), 15,
                           color[i], cv2.FILLED)

        strVal = str(fingerVal[0])+str(fingerVal[1])+str(fingerVal[2])+str(fingerVal[3])+str(fingerVal[4])

    conn.close()
    servo_server.close()

process_thread.join()
cap.release()
