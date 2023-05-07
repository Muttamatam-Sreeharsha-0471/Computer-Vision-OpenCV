import cv2

img = cv2.imread("C:\\Users\\sreeh\\Desktop\\OpenCV\\image1.jpg",0)
edges = cv2.Canny(img,100,200)

cv2.imwrite('edges_image.jpg', edges)