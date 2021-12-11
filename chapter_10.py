import cv2
import numpy as np

# Virtual Paint project(1)
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth) # id of width is 3 and 640 is pixel size
cap.set(4,frameHeight) # id of height is 4 and 480 is pixel size
cap.set(10,10) # id of brightness is 10 

myColors = [[5,107,0,19,255,255],
            [133,56,0,159,156,255],
            [57,76,0,100,255,255]]

myColorValues = [[51,153,255],     #BGR format
                [255,0,255],
                [0,255,0]]

myPoints = []   # [x,y,colorId]


def findColor(img,myColors,myColorValues): 
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0 #for my color values
    newPoints = []
    for color in myColors:
        lower = np.array( color[:3])
        upper = np.array( color[3:])

        mask = cv2.inRange(imgHsv,lower,upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x and y !=0:
            newPoints.append([x,y,count])
        count +=1
        # cv2.imshow(str(color[0]),mask)
    return newPoints  

def getContours(img):
    contours , hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt) #find area of shapes
        # setmin threshold for so it doesn't detect any noise
        if area>500: #500px
            # cv2.drawContours(imgResult,cnt,-1 ,(0,0,255),3) #-1 for draw the all contours,drawing contour on original image
            peri = cv2.arcLength(cnt,True) #arclength,perimeter,contourPerimeter
            # print(peri)
            apporx = cv2.approxPolyDP(cnt,0.02*peri,True)
           # We are creating a bounding box around shape for this we need x,y,width,height
            x,y,w,h = cv2.boundingRect(apporx)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),10,myColorValues[point[2]],cv2.FILLED)
        

while True:
    success , img = cap.read()
    imgResult = img.copy( )
    newPoints = findColor(img,myColors,myColorValues)
    if len(newPoints)!=0:
        for  newP in newPoints:  #new points is a list and we are breaking into to points otherwise this becomes a list inside a list
            myPoints.append(newP)
    
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
    cv2.imshow("Output",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break