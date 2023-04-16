import cv2
from cvzone.HandTrackingModule import HandDetector
from WIFI_send_serwer import Server_motor
from Secret.Secret import serwer_ip, serwer_ip_laptop, ip_esp

cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=1)

fingerTip = [4, 8, 12, 16, 20]
fingerVal = [0, 0, 0, 0, 0]
lastData = 00000

red = (0, 0, 255)
yellow = (0, 255, 255)
blue = (255, 0, 0)
green = (0, 255, 0)
purple = (255, 0, 255)

color = [red, yellow, blue, green, purple]

servo_server = Server_motor(serwer_ip, 80)
conn, addr = servo_server.accept()


while cap.isOpened():
    success, img = cap.read()
    img - detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=False)

    if lmList:
        # Thumb
        handType = detector.handType()
        if handType == "Right":
            if lmList[fingerTip[0]][0] > lmList[fingerTip[0]-1][0]:
                servo_server.send("Thumb_Up")
                conn.close()
                servo_server.close()
            else:
                servo_server.send("Thumb_Down")
                conn.close()
                servo_server.close()
        else:
            if lmList[fingerTip[0]][0] < lmList[fingerTip[0]-1][0]:
                servo_server.send("Thumb_Up")
                conn.close()
                servo_server.close()
            else:
                servo_server.send("Thumb_Down")
                conn.close()
                servo_server.close()

                #4 fingers
        for i in range(1, 5):
            if lmList[fingerTip[i]][1] < lmList[fingerTip[i]-2][1]:
                fingerVal[i] = 1
            else:
                fingerVal[i] = 0

        #Draw mark
        for i in range(0, 5):
            if fingerVal[i] == 1:
                cv2.circle(img, (lmList[fingerTip[i]][0], lmList[fingerTip[i]][1]), 15,
                           color[i], cv2.FILLED)

        strVal = str(fingerVal[0])+str(fingerVal[1])+str(fingerVal[2])+str(fingerVal[3])+str(fingerVal[4])



    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
