import cv2

img = cv2.imread('C:\\Users\\ghant\\OneDrive\\Desktop\\shinchan.jpg')

watermark = cv2.imread('C:\\Users\\ghant\\OneDrive\\Desktop\\dora.jpg')

watermark = cv2.resize(watermark, (img.shape[1], img.shape[0]))

result = cv2.addWeighted(img, 1, watermark, 0.3, 0)

cv2.imwrite("water.jpg", result)
