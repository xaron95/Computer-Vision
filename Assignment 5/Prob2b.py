import cv2
import numpy as np
from Prob2a import *

def SpatialPyramidDist(I1,I2,bins):
	sumArray = np.zeros((3,1))
	h1,w1,temp = I1.shape
	# print h1,w1
	# h2,w2,temp = I2.shape
	for i in xrange(3):
		numberOfDivisions = 2**i
		sum = 0
		for j in xrange(numberOfDivisions):
			for k in xrange(numberOfDivisions):
				startRow,startColumn = j*numberOfDivisions,k*numberOfDivisions
				endRow,endColumn = startRow+h1/numberOfDivisions,startColumn+w1/numberOfDivisions
				# print startRow,startColumn,endRow,endColumn
				I1Section = I1[startRow:endRow,startColumn:endColumn]
				I2Section = I2[startRow:endRow,startColumn:endColumn]
				sum+=HistInterDist(I1Section,I2Section,bins)
		sumArray[i] = sum
	return ((sumArray[0]+sumArray[1])*0.25)+(0.5*sumArray[2])

def main():
	filename1 = './logo/logo/data/template.jpg'
	template = cv2.imread(filename1)
	filename2 = './logo/logo/data/starbucks6.jpg'
	img = cv2.imread(filename2)
	# cielab_img = RGB2Lab(img)
	# print cielab_img[:,:,2].mean()
	# print cielab_img
	# hist = Histogram(img,8)
	box = SlidingWindowDetector(template,img,HistInterDist,True,20)
	VisualiseBox(img,box)

if __name__ == '__main__':
	main()