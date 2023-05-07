import cv2

img = cv2.imread('C:\\Users\\sreeh\\Desktop\\OpenCV\\image1.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('gray_image.jpg', gray_img)
