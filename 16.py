#16
import cv2
import numpy as np

img = cv2.imread('C:\\Users\\ghant\\OneDrive\\Desktop\\shin.jpg',0)

edges = cv2.Canny(img,100,200)

cv2.imshow('Edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()