import cv2 #as cv
from matplotlib import pyplot as plt 


cap = cv2.VideoCapture(0)
ret, frame = cap.read()
print(ret) 
if ret:
    plt.imshow(frame)
cap.release() 

#img = cv.imread("test.jpg") 

#cv.imshow("Display window", img) 
#k = cv.waitKey(0) # Wait for a keystroke in the window 