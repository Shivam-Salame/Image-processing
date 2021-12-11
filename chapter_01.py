import cv2

# print("package imported")

## Chapter 1 (Read: Image , video and Webcam)

# Image Capturing

# img = cv2.imread("Resources/ok.jpg") # reading image

# cv2.imshow("Output",img)   # display

# # Without delay our image is open for a fraction of second
# # we need to add delay in order to see the image

# cv2.waitKey(0) # Function for delay ( 0 is used for infinite delay and 1000 ms is used for 1 sec)

# Video Capturing

# video is just a Sequence of images

# cap = cv2.VideoCapture("Resources/vid_1.mp4") #

# while True:  #Loop runs to check every sequence of image
    
#     # to capture image

#     success , img = cap.read() # success works as bool var which shows image is successfull read or not 
#                                # img var store images

#     # to show result

#     cv2.imshow("Output",img) #display

#     # delay

#     if cv2.waitKey(1) & 0xFF == ord('q'): #Stack Overflow
#         break                             # Break loop on q press

# Use a web cam is similar to open a video

cap = cv2.VideoCapture(0) # 0 for default webcam in my case i have only one in my laptop, if you have more give the id of that webcam inside function

# if we want a specific parameter of height and width

# cap is a webcan object

cap.set(3,640) # id of width is 3 and 640 is pixel size
cap.set(4,480) # id of height is 4 and 480 is pixel size
cap.set(10,0) # id of brightness is 10 

while True:
    success , img = cap.read()
    cv2.imshow("Output",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

q





 