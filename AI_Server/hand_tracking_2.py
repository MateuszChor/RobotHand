import cv2
from cvzone.HandTrackingModule import HandDetector
from WIFI_send_serwer import Server_motor
from Secret.Secret import serwer_ip, serwer_ip_laptop, ip_esp

cap = cv2.VideoCapture(0)

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
forefinger_up = True
forefinger_down = True
middlefinger_up = True
middlefinger_down = True
ringfinger_up = True
ringfinger_down = True
littlefinger_up = True
littlefinger_down = True

while cap.isOpened():
    servo_server = Server_motor(serwer_ip_laptop, 80)
    conn, addr = servo_server.accept()
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    if lmList:
        handType = detector.handType()

        # Right hand
        if handType == "Right":
            # Right Thumb
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




        # Left hand
        else:
            # Left Thumb
            if lmList[fingerTip[0]][0] < lmList[fingerTip[0]-1][0]:
                thumb_up = True
                if thumb_down:
                    servo_server.send(conn, "Thumb_Up")
                    thumb_down = False

            else:
                thumb_down = True
                if thumb_up:
                    servo_server.send(conn, "Thumb_Down")
                    thumb_up = False


        # Forefinger
        if lmList[fingerTip[2]][1] < lmList[fingerTip[2] - 2][1]:
            forefinger_up = True
            if forefinger_down:
                servo_server.send(conn, 'Forefinger_Up')
                forefinger_down = False
            else:
                forefinger_down = True
                if forefinger_up:
                    servo_server.send(conn, 'Forefinger_Down')
                    forefinger_up = False

        # Middle Finger
        if lmList[fingerTip[3]][1] < lmList[fingerTip[3] - 2][1]:
            middlefinger_up = True
            if middlefinger_down:
                servo_server.send(conn, 'Middle_Up')
                middlefinger_down = False
            else:
                middlefinger_down = True
                if middlefinger_up:
                    servo_server.send(conn, 'Middle_Down')
                    middlefinger_up = False

        # Ring Finger
        if lmList[fingerTip[4]][1] < lmList[fingerTip[4] - 2][1]:
            ringfinger_up = True
            if ringfinger_down:
                servo_server.send(conn, 'Ring_finger_Up')
                ringfinger_down = False
            else:
                ringfinger_down = True
                if ringfinger_up:
                    servo_server.send(conn, 'Ring_finger_Down')
                    ringfinger_up = False


        # Little Finger
        if lmList[fingerTip[5]][1] < lmList[fingerTip[5] - 2][1]:
            littlefinger_up = True
            if littlefinger_up:
                servo_server.send(conn, 'Little_finger_Up')
                littlefinger_down = False
            else:
                littlefinger_down = True
                if littlefinger_up:
                    servo_server.send(conn, 'Little_finger_Down')
                    littlefinger_up = False

        #     # 4 fingers
        # for i in range(1, 5):
        #     if lmList[fingerTip[i]][1] < lmList[fingerTip[i] - 2][1]:
        #         fingerVal[i] = 1
        #
        #     else:
        #         fingerVal[i] = 0

        #Draw mark
        for i in range(0, 5):
            if fingerVal[i] == 1:
                cv2.circle(img, (lmList[fingerTip[i]][0], lmList[fingerTip[i]][1]), 15,
                           color[i], cv2.FILLED)

        strVal = str(fingerVal[0])+str(fingerVal[1])+str(fingerVal[2])+str(fingerVal[3])+str(fingerVal[4])

    conn.close()
    servo_server.close()

cv2.destroyAllWindows()
