import cv2
import numpy as np
import imutils

def denoiser(path_to_dirty_image,path_to_clean_image):
    image = cv2.imread(path_to_dirty_image)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image = cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)[1]
    h,w = image.shape
    cv2.imwrite('/home/paindr/Desktop/Personnal_project/Mastering_ocr/cleaned_images/cleaned1.png',image)
    dist = cv2.distanceTransform(image,cv2.DIST_L2,5)
    cv2.imshow('dist1', dist)
    dist1 = np.zeros((h,w))
    dist = cv2.normalize(dist,dist1,0,100,cv2.NORM_MINMAX)
    cv2.imshow('dist2 normalise betwn 0,60',dist)
    dist = (dist*255).astype("uint8")
    cv2.imshow('dist3 *255',dist)
    dist = cv2.threshold(dist,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]
    cv2.imshow('dist_otsu',dist)
    cv2.waitKey(0)