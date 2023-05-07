import cv2

img = cv2.imread("C:\\Users\\sreeh\\Desktop\\OpenCV\\image1.jpg")
blur_image = cv2.GaussianBlur(img,(5,5),0)

cv2.imwrite('blur_image.jpg', blur_image)
