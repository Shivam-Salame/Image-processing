import cv2
import numpy as np

#chapter 3: Resizing and cropping

img = cv2.imread("Resources/bug.jpg")

print(img.shape) # To check shape of our image
                 # returns (height,width,channel=BGR)

imgResize = cv2.resize(img,(400,400)) # para_2 : width,height
print(imgResize.shape)

imgResize_stretched = cv2.resize(img,(700,700)) # para_2 : width,height
print(imgResize_stretched.shape)

imageCropped = img[0:200 , 200:400] # original image is an array of pixels ,parameter height,width
cv2.imshow("Image",img)
cv2.imshow("Resized",imgResize)
cv2.imshow("Stretched",imgResize_stretched)
cv2.imshow("cropped",imageCropped)
cv2.waitKey(0)