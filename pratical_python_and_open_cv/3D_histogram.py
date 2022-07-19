from __future__ import print_function
from matplotlib import pyplot as plt
from matplotlib import *
import argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("original coloured",image)
fig = plt.figure()
hist = cv2.calcHist([image],[0,1,2],None,[8,8,8],[0,256,0,256,0,256])
plt.imshow(hist)
print("3D histogram shape:{},with {} values".format(hist.shape,hist.flatten().shape[0]))
plt.show()