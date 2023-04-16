import cv2
from cvzone.HandTrackingModule import HandDetector

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


while cap.isOpened():
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    if lmList:
        handType = detector.handType()

        print(handType)

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


        # Left hand
        else:
            # Left Thumb
            if lmList[fingerTip[0]][0] < lmList[fingerTip[0]-1][0]:
                fingerVal[0] = 1
            else:
                fingerVal[0] = 0

        print(fingerVal)


        #Draw mark
        for i in range(0, 5):
            if fingerVal[i] == 1:
                cv2.circle(img, (lmList[fingerTip[i]][0], lmList[fingerTip[i]][1]), 15,
                           color[i], cv2.FILLED)

        strVal = str(fingerVal[0])+str(fingerVal[1])+str(fingerVal[2])+str(fingerVal[3])+str(fingerVal[4])
cv2.destroyAllWindows()
