import numpy as np
import cv2
def random_img(img):
	temp_img = np.array(np.random.randint(0,256,(img.shape)),dtype='uint8')
	y = cv2.subtract(img,temp_img)
	print y
	return y