import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="Desktop/OpenCV/image1.jpg")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

rotated = imutils.rotate(image, 180)

cv2.imshow("Original", image)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
