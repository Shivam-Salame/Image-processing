import cv2
import numpy as np

## Chapter 2: Basic Functions 

img = cv2.imread("Resources/bug.jpg")

kernel = np.ones( (5,5), np.uint8 ) # para_1 is size of matrix and para_2 is type of object
# uint8 = unsigned int of 8 bit, This means value can ranges from 0-255

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # The function converts an input image from one color space to another
                         #  Note that the default color format in OpenCV is often referred to as RGB but it is actually BGR (the bytes are reversed)
# first parameter is source and second is color change

# we can use Gaussian blur to our image using original colored or gray scale image

imgBlur = cv2.GaussianBlur(imgGray , (7,7) , 0) # parameters source , gaussian kernel , sigma

# to find edges in image

imgCanny = cv2.Canny(img,100,100) # It takes threshold values as parameter

# to increase the thickness of image

imgDialtion = cv2.dilate(imgCanny, kernel , iterations=1)
# The function supports the in-place mode. Dilation can be applied several ( iterations ) times.
# In case of multi-channel images, each channel is processed independently.

# here we take imgCanny because we are dealing with edges
# 2nd parameter is kernel which is a matrix (sizeOf , valueOf) 
# numpy is useful for deal with matrix  

# Eroded is oposite to Dialtion 
# In dialtion we get thick edges in this we get thin edges

imgEroded = cv2.erode(imgDialtion,kernel,iterations=1)

cv2.imshow(" Gray",imgGray)
# cv2.imshow(" Blur",imgBlur)
# cv2.imshow(" Canny",imgCanny)
# cv2.imshow(" Dialation",imgDialtion)
# cv2.imshow(" Eroded",imgEroded)
cv2.waitKey(0)