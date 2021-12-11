import cv2
import numpy as np

# chapter 6 :  Joining Images (putting multiple image in one window)

img = cv2.imread("Resources/bug.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Here comes murtaza stack() function which creates a vertical and horizontal image stack

hor = np.hstack((img,img)) #numpy function to put image in horizontal

ver = np.vstack((img,img))

# imgStack = stack( 0.5 ,( [ img, imgGray, img ] , [ img, imgGray, img ] ) ) # Parameter  : scale , Horizontal stack row 1 , Horizontal stack row 2  

cv2.imshow("Horizontal",hor)
cv2.imshow("Vertical",ver)
# cv2.imshow("Image Stacked",imgStack)
#both images must have same channel bcoz we are talking about matrices
# In our case our image is color ful and having 3 channel BGR
cv2.waitKey(0)