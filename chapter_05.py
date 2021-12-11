import cv2
import numpy as np

# chapter 5: Warp prespective

img = cv2.imread("Resources/bug.jpg")

width ,height =250,350 #2.5 inch and 3.5 inch size of a playing card

pts1= np.float32( [ [111,219] , [287,188] , [154,482] , [352,440] ] )

pts2 = np.float32( [ [0,0] , [width,0] , [0,height] , [width,height] ])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)