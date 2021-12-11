import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands #formality for using this model
hands = mpHands.Hands() #object of hand (if we intialize the static parameter as true then it will detect only if it has good tracking confidance then it keeps tracking otherwise detection takes place)
# max hands default is 2
mpDraw = mp.solutions.drawing_utils

 
while True:
    success, img = cap.read() 
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    # print(result.multi_hand_landmarks) # if hand is placed in range of camera then it will show x,y,z 
    
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break