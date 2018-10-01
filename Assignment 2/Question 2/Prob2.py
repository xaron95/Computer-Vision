import cv2
import numpy as np

def scale(img):
	img -= np.min(img)
	img = np.multiply(255.0/np.max(img),img)
	return np.array(img,dtype = np.uint8)

def convolution(kernel,img):
	new_img = np.zeros((img.shape[0],img.shape[1]))
	temp = np.zeros((kernel.shape[0],img.shape[1]),dtype='uint8')
	img = np.append(temp,img,axis=0)
	img = np.append(img,temp,axis=0)
	temp2 = np.zeros((img.shape[0],kernel.shape[1]),dtype='uint8')
	img = np.append(temp2,img,axis=1)
	img = np.append(img,temp2,axis=1)
	kernel = np.fliplr(np.flipud(kernel))
	#print kernel.shape
	#print img.shape
	window_x = kernel.shape[0]
	window_y = kernel.shape[1]
	x_flag = window_x%2
	y_flag = window_y%2
	#print x_flag
	#print y_flag
	for x in range(kernel.shape[0],img.shape[0]-kernel.shape[0]):
		for y in range(kernel.shape[1],img.shape[1]-kernel.shape[1]):
			a = x-window_x/2
			b = x+window_x/2+x_flag
			c = y-window_y/2
			d = y+window_y/2+y_flag
			temp = img[a:b,c:d]
			new_img[x-kernel.shape[0]][y-kernel.shape[1]] = np.sum(np.multiply(kernel,temp))
			#new_img = scale(new_img)
	return scale(new_img)
#clown = cv2.imread("clown.jpg",0)
#impulse = np.array([[0,0,0],[0,1,0],[0,0,0]])
#convolution(impulse,clown)



