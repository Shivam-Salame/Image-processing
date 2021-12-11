import cv2
import numpy as np

# chapter 12:Number plate detection project 3
noPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

cap.set(3,640) # id of width is 3 and 640 is pixel size
cap.set(4,480) # id of height is 4 and 480 is pixel size
cap.set(10,50) # id of brightness is 10 
count = 0
while True:
    success , img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    numberPlate = noPlateCascade.detectMultiScale(imgGray,1.1,4)

    for (x,y,w,h) in numberPlate:
        area = w*h
        if area>500: #500 as min area
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("Roi",imgRoi)

    cv2.imshow("Output",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("Resources/scanned/NoPlate_"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count +=1
        