import cv2
import sys

image = cv2.imread('images/219983.png')
if image is None:
    print("Failed to read image from file.")
    sys.exit(1)

convert_img = cv2.imwrite('images/219984.jpg', image)
if not convert_img:
    print("Failed to write image to file.")
    sys.exit(1)
