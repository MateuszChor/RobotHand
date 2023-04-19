import cv2
from cvzone.HandTrackingModule import HandDetector
from MotorServer import server
from Secret.Secret import serwer_ip, serwer_ip_laptop, ip_esp

cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=1, maxHands=1)

fingerTip = [4, 8, 12, 16, 20]
fingerVal = [0, 0, 0, 0, 0]
strVal = "11111"
lastData = "00000"

while cap.isOpened():

    Server = server(serwer_ip_laptop, 80)
    conn, addr = Server.accept()
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
                fingerVal[0] = 1

            else:
                fingerVal[0] = 0

                # 4 fingers
            for i in range(1, 5):
                if lmList[fingerTip[i]][1] < lmList[fingerTip[i] - 2][1]:
                    fingerVal[i] = 1

                else:
                    fingerVal[i] = 0

        else:
            print("Use your right hand !")

        strVal = str(fingerVal[0])+str(fingerVal[1])+str(fingerVal[2])+str(fingerVal[3])+str(fingerVal[4])

        if lastData != strVal:
            Server.send(strVal)
            lastData = strVal
        # TODO add methods to v on esp side

    conn.close()
    Server.close()

cv2.destroyAllWindows()
