import cv2


def segment_vertical(path):
    image = cv2.imread(path)
    h,w,_=image.shape

    image = image[0:h,0:int(w//2.5)]

    cv2.imwrite('pain.png',image)
    cv2.imshow('pain', image)
    cv2.waitKey(0)
