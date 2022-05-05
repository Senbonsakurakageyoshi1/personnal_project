import cv2

def resize(path):
    image = cv2.imread(path)
    h,w,_ =image.shape
    image= cv2.resize(image,(int(h/2),int(w/2)),interpolation = cv2.INTER_CUBIC)
    cv2.imwrite('resized.png',image)
    cv2.imshow('res',image)
    #cv2.waitKey(0)