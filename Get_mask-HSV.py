import cv2
import numpy as np
def nothing(x):
  pass
cv2.namedWindow('Colorbars')


cv2.createTrackbar("Min_H", "Colorbars",0,255,nothing)
cv2.createTrackbar("Max_H", "Colorbars",0,255,nothing)
cv2.createTrackbar("Min_S", "Colorbars",0,255,nothing)
cv2.createTrackbar("Max_S", "Colorbars",0,255,nothing)
cv2.createTrackbar("Min_V", "Colorbars",0,255,nothing)
cv2.createTrackbar("Max_V", "Colorbars",0,255,nothing)

img=cv2.imread('D:\\Project\\AnalysisOfArchitecturalDrawings\\File_Ban_Ve\\Banvechitiet.JPG')
print(img.shape)
img = cv2.resize(img,None,fx=0.7, fy=0.7, interpolation = cv2.INTER_LINEAR)     #If large image you should resize
cv2.imshow('img', img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
while True:
  Min_H=cv2.getTrackbarPos("Min_H", "Colorbars")
  Max_H=cv2.getTrackbarPos("Max_H", "Colorbars")
  Min_S=cv2.getTrackbarPos("Min_S", "Colorbars")
  Max_S=cv2.getTrackbarPos("Max_S", "Colorbars")
  Min_V=cv2.getTrackbarPos("Min_V", "Colorbars")
  Max_V=cv2.getTrackbarPos("Max_V", "Colorbars")

  lower=np.array([Min_H,Min_S,Min_V])
  upper=np.array([Max_H,Max_S,Max_V])
  
  # cv2.imshow('Colorbars',img)
  mask = cv2.inRange(hsv, lower, upper)
  cv2.imshow('mask',mask)
  # Not_mask = cv2.bitwise_not(mask)
  
  # cv2.imshow('Not_mask',Not_mask)
  kernel = np.ones((1,1),np.uint8)
  erosion = cv2.erode(mask,kernel,iterations = 1)
  # dilation = cv2.dilate(Not_mask,kernel,iterations = 1)
  # cv2.imshow('Erosion',erosion) #You should this mask
  cv2.imshow('erosion',erosion)


  k = cv2.waitKey(1) & 0xFF
  if k == ord('q'):
    break


