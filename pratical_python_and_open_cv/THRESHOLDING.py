import numpy as np
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("image",image)


#simple_thresholding

(T,thresh)=cv2.threshold(blurred,155,255,cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary",thresh)

(T,threshInv)=cv2.threshold(blurred,185,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold binary inverse",threshInv)

cv2.imshow("CNI masked",cv2.bitwise_and(image,image,mask=threshInv))



thresh=cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,20)
cv2.imshow("Mean thresh",thresh)

thresh=cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,15,20)
cv2.imshow("Gaussian Thresh",thresh)
cv2.imshow("CNI masked adaptative",cv2.bitwise_and(image,image,mask=thresh))

cv2.waitKey(0)

