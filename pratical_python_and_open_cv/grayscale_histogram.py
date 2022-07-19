from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
channels = [0,1,2]
mask = None
histSize = [256,32,32]
ranges = [0,256]
cv2.imshow("original coloured",image)
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("original grayscale",image)
hist = cv2.calcHist([image],[channels[0]],mask,[histSize[0]],ranges)

plt.figure()
plt.title("graysacle histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixel")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv2.waitkey(0)
