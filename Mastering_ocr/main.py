import cv2
import pytesseract
import argparse
from denoiser import denoiser
from read import read
from segment_vertical import segment_vertical
from resize import resize


path_to_dirty_image='/home/paindr/Desktop/Personnal_project/Mastering_ocr/images/page-0-1651657651.9124749.jpg'
path_to_clean_image = '/home/paindr/Desktop/Personnal_project/Mastering_ocr/cleaned_images'
path_to_image_to_read = '/home/paindr/Desktop/Personnal_project/Mastering_ocr/images/page-0-1651657651.9124749.jpg'




denoiser(path_to_dirty_image,path_to_clean_image)

#segment_vertical(path_to_dirty_image)
#resize(path_to_dirty_image)

text = read('/home/paindr/Desktop/Personnal_project/Mastering_ocr/Screenshot at 2022-04-29 17-41-15.png')

print(text)
