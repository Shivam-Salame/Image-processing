import cv2

# chapter 9: Face detection
# First Real=Time detection method Viola and Jones(2001)

# using positive = images of faces
#       negatives = image of anything but not faces

# then we train and create a cascade file(xml file) which will help us to find faces

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread("Resources/demo.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)
