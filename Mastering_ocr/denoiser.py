import cv2
import numpy as np
import imutils

def denoiser(path_to_dirty_image,path_to_clean_image):
    image = cv2.imread(path_to_dirty_image)

    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image = cv2.threshold(image,0,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)[1]
    cv2.imshow('first image threshold',image)
    h,w = image.shape
    cv2.imwrite('/home/paindr/Desktop/Personnal_project/Mastering_ocr/cleaned_images/cleaned1.png',image)
    dist = cv2.distanceTransform(image,cv2.DIST_L2,5)
    #cv2.imshow('dist1', dist)
    dist = cv2.normalize(dist,dist,0,100,cv2.NORM_MINMAX)
    #cv2.imshow('dist2 normalise betwn 0,60',dist)
    dist = (dist*255).astype("uint8")
    #cv2.imshow('dist3 *255',dist)
    dist = cv2.threshold(dist,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]
    #cv2.imshow('dist_otsu',dist)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    opening = cv2.morphologyEx(dist, cv2.MORPH_OPEN, kernel)
    #cv2.imshow("Opening", opening)

    cnts = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    chars = []
    for c in cnts:
    # compute the bounding box of the contour
        (x, y, w, h) = cv2.boundingRect(c)
        if w <=35 and h <= 100:
            chars.append(c)
    print(cnts)

    image2 = cv2.imread(path_to_dirty_image)
    gray = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 1000, 520)
    contours, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


    cv2.drawContours(image2, contours, -1, (0, 255, 0), 3)

    cv2.imshow('image contours',image2)

