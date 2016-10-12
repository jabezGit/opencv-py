import cv2
import numpy as np
print cv2.__version__

# Load an color image in grayscale
img = cv2.imread('img.jpg',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()