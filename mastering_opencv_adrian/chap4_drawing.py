from __future__ import print_function
import argparse
import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype = "uint8")
green = (0,255,0)
cv2.line(canvas,(10,100),(300,300),green)
cv2.imshow("canvas",canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


cv2.rectangle(canvas,(0,0),(50,50),green,-5)
cv2.imshow("senbon",canvas)
cv2.waitKey((0))

white = (2555,255,255)
(centerx,centery)=(canvas.shape[1]//2,canvas.shape[0]//2)
for r in range (0,175,25):
  cv2.circle(canvas,(centerx,centery),r,white)


cv2.imshow('circle',canvas)
cv2.waitKey(0)


for i in range(0, 25):
   radius = np.random.randint(5, high = 200)
   color = np.random.randint(0, high = 256, size = (4,)).tolist()
   pt = np.random.randint(0, high = 300, size = (2,))

   cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("pain", canvas)
cv2.waitKey(0)