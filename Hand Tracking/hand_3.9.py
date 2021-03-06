import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read() 
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    # print(result.multi_hand_landmarks) # if hand is placed in range of camera then it will show x,y,z 
    
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,"\n", lm)
                h, w, c = img.shape #height ,width , channels
                cx, cy =  int(lm.x*w), int(lm.y*h)  #centre points
                print(id,cx,cy)

                # if id==0: #0-20 are finger points
                cv2.circle(img, (cx,cy), 8 , (0,0,0),cv2.FILLED )
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)


    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break