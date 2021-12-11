import cv2 
import numpy as np

# chapter 7 : color Detection

def empty(a):
    pass

# Here comes stackImages Function

cv2.namedWindow("TrackBars") # Creating window Named Trackbars
cv2.resizeWindow("TrackBars",640,240)

cv2.createTrackbar("Hue Min" , "TrackBars" ,0 ,179,empty)  # in cv2 we have max 179 hue value
cv2.createTrackbar("Hue Max" , "TrackBars" ,179 ,179,empty)
cv2.createTrackbar("Sat Min" , "TrackBars" ,0 ,255,empty)
cv2.createTrackbar("Sat Max" , "TrackBars" ,255,255,empty)
cv2.createTrackbar("Val Min" , "TrackBars" ,0 ,255,empty)
cv2.createTrackbar("Val Max" , "TrackBars" ,255 ,255,empty)

 

while True:
    
    img = cv2.imread("Resources/railway.jpg")

    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min" , "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max" , "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min" , "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max" , "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min" , "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max" , "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)


    lower = np.array( [h_min,s_min,v_min ])
    upper = np.array( [ h_max,s_max,v_max ])

    mask = cv2.inRange(imgHsv,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    # cv2.imshow("Image",img)
    # cv2.imshow("Hsv",imgHsv)
    # cv2.imshow("Mask",mask)
    # cv2.imshow("ImgResult" ,imgResult)

    imgStack = stackImages(0.6, ([img,imgHsv]),(mask,imgResult))
    
    cv2.imshow("Stacked Images",imgStack)

    cv2.waitKey(1)