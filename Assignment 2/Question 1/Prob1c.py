import cv2
import numpy as np

def scale(img):
	img -= np.min(img)
	img = np.multiply(255.0/np.max(img),img)
	return np.array(img,dtype = np.uint8)

def NCC(template,img):
	new_img = np.zeros((img.shape[0],img.shape[1]))
	temp = np.zeros((template.shape[0],img.shape[1]),dtype='uint8')
	img = np.append(temp,img,axis=0)
	img = np.append(img,temp,axis=0)
	temp2 = np.zeros((img.shape[0],template.shape[1]),dtype='uint8')
	img = np.append(temp2,img,axis=1)
	img = np.append(img,temp2,axis=1)
	#print template.shape
	#print img.shape
	window_x = template.shape[0]
	window_y = template.shape[1]
	x_flag = window_x%2
	y_flag = window_y%2
	#print x_flag
	#print y_flag
	for x in range(template.shape[0],img.shape[0]-template.shape[0]):
		for y in range(template.shape[1],img.shape[1]-template.shape[1]):
			a = x-window_x/2
			b = x+window_x/2+x_flag
			#print b-a
			c = y-window_y/2
			d = y+window_y/2+y_flag

			temp = img[a:b,c:d]
			temp = temp-np.mean(temp)
			if np.std(temp) != 0:
				temp = temp/np.std(temp)
			#print temp
			#print a,b,c,d,x,y
			#print img.shape
			new_img[x-template.shape[0]][y-template.shape[1]] = np.sum(np.multiply(template,temp))
			#new_img = scale(new_img)
	new_img = scale(new_img)
	cv2.imwrite("NCC_big.png",new_img)
	(i,j)=np.unravel_index(np.argmax(new_img,axis=None),new_img.shape)
	print "Max intensity location:("+str(i)+","+str(j)+")"
cuba = cv2.imread("u2cuba.jpg",0)
trailer = cv2.imread("trailerSlightlyBigger.png",0)
NCC(trailer,cuba)

#Max intensity at (715,419)

