import cv2
def redgreen_swap(img):
	b,g,r = cv2.split(img)
	return cv2.merge([b,r,g])
x = cv2.imread("example2.jpg")
cv2.imwrite("img.png",redgreen_swap(x))
