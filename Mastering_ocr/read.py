import cv2
import pytesseract

def read(path_to_image_to_read):

    image = cv2.imread(path_to_image_to_read)
    #image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

    text = pytesseract.image_to_string(path_to_image_to_read)

    return text

