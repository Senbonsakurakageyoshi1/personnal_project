from __future__ import print_function
from matplotlib import pyplot as plt
import argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("original coloured",image)


chans = cv2.split(image)
colors = ("b","g","r")

plt.figure()
plt.title("Flattened' color histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixel")


for (chan,color) in zip(chans,colors):
    hist = cv2.calcHist([chan],[0],None,[256],[0,256])
    plt.plot(hist,color = color)
    plt.xlim([0,256])
plt.show()
cv2.waitkey(0)
