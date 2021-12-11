import cv2
import numpy as np
from numpy.lib.type_check import _imag_dispatcher

# chapter 4: Shapes and texts

# 0=black and 1=white
# img = np.zeros( (512,512), np.uint8)   # without channel
img = np.zeros( (512,512,3), np.uint8) # if we want to give it color we have to provide channel
# This gives values from 0-255
# print(img)

# img[:] = 0,0,0 #(BGR in whole image)
# img[50:100,100:150] = 50,200,150 #(BGR in whole image)
# image array can have height and width as parameter

# if we want to draw a line in an image

# cv2.line(img,(0,0) , (400,400), (0,0,0),2) #source  , width ,height ,color, thickness
# cv2.line(img,(0,0) , (img.shape[1],img.shape[0]), (0,0,0),2) #img.shape return 3 value in a list we a re fetching 1 and second value of list as height and width

# cv2.rectangle(img,(0,0) , (250,350) , (0,0,255),2) # hollow diagonal
# cv2.rectangle(img,(0,0) , (250,350) , (0,0,255),cv2.FILLED) # Color filled diagonal

# cv2.circle(img,(150,300),100,(0,0,255),2) # img, centre of circle(width,height) ,radius , color , thickness 

cv2.putText(img,"shivam_coder",(200,400),cv2.FONT_HERSHEY_PLAIN,2 ,(0,0,255),1) #img, String , origin ,font_face, font scale, color , thickness

cv2.imshow("Image",img)
cv2.waitKey(0)