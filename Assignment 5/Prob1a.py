import cv2
import numpy as np

def isInImage(img,i,j):
	if (i<0 or i>=img.shape[0] or j<0 or j>=img.shape[1]):
		return False
	return True

def isRedCircle(img,circle,threshold):
	total_count = 0
	area = np.pi*circle[2]*circle[2]
	for i in xrange(circle[1]-circle[2],circle[1]+circle[2]):
		for j in xrange(circle[0]-circle[2],circle[0]+circle[2]):
			if isInImage(img,i,j):
				if ((i-circle[1])**2 + (j-circle[0])**2) <= area:
					if 2*img[i,j,2]-img[i,j,0]-img[i,j,1]>0:
						total_count+=1

	if total_count>= threshold*area:
		return True
	return False


def main():
	filename = 'redeye.jpeg'
	cimg = cv2.imread(filename)
	# cimg = cv2.medianBlur(cimg,3)
	# hsv_image = cv2.cvtColor(c2img,cv2.COLOR_BGR2HSV)

	img = cv2.cvtColor(cimg,cv2.COLOR_BGR2GRAY)
	h,w = img.shape
	minDist = int(round(min(0.1*h,0.1*w)))
	print h,w
	# circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,minDist,np.array([]),
                            # param1=100,param2=15,minRadius=0,maxRadius=minDist)
	circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1, minDist*2, np.array([]), 100, 20, 0, minDist)
	# print circles
	if circles!= None :
		circles = np.uint16(np.round(circles))
		for i in circles[0,:]:
			# draw the outer circle
			area = np.pi*i[2]*i[2]
			print 'area: '+str(area)
			# if(coords[3]>=img.shape[0]):
			# 	coords[3] = img.shape[0]
			# if(coords[2]>=img.shape[1]):
			# 	coords[2] = img.shape[2]
			if isRedCircle(cimg, i,0.5):
				# print 'here'
				cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),1)
			# else:
				# cv2.circle(cimg,(i[0],i[1]),i[2],(0,0,255),1)

			# draw the center of the circle
			# cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
	cv2.imshow('detected circles',cimg)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()