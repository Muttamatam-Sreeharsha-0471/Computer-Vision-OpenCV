import cv2
import numpy as np

img = cv2.imread("C:\\Users\\sreeh\\Desktop\\OpenCV\\image1.jpg")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
eroded_image = cv2.erode(gray_image, kernel, iterations=1)
cv2.imwrite("eroded_image.jpg",eroded_image)
