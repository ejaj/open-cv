import cv2
import sys

image = cv2.imread('images/219983.png')
if image is None:
    print("Failed to read image from file.")
    sys.exit(1)
cv2.imshow('my image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
