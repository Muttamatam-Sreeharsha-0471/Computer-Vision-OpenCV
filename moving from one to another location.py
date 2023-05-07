import cv2

img = cv2.imread('image.jpg')

# Show the image
cv2.imshow('Image', img)

# Move the window to a new location
cv2.moveWindow('Image', 100, 100)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()