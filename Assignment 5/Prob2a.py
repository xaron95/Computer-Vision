import cv2
import numpy as np
from matplotlib import pyplot as plt

def Histogram(img,bins):
	cielab_img = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
	# cv2.imshow('Inbuilt',cielab_img)
	# cv2.waitKey(0)

	l_hist = cv2.calcHist([cielab_img],[0],None,[bins],[0,256])
	a_hist = cv2.calcHist([cielab_img],[1],None,[bins],[0,256])
	b_hist = cv2.calcHist([cielab_img],[2],None,[bins],[0,256])
	hist = np.concatenate((l_hist.T,a_hist.T,b_hist.T),axis=1)	
	# print hist.shape
	return hist

def SlidingWindowDetector(Template,I,Dist,isMax,bins):
	Ih,Iw,temp = I.shape
	ret = [0,0,0,0]
	min_max = 0
	dist = 0
	
	scaleRange = xrange(3,13)
	for k in scaleRange:
		print k
		T = cv2.resize(Template,None,fx=k/4.0, fy=k/4.0)
		Th,Tw,temp = T.shape
		# if Ih<Th or Iw<Tw:
		# 	break
		# THist = Histogram(T,20)
		for i in xrange(0, Ih - Th):
			for j in xrange(0, Iw - Tw):
				imgSection = I[i:i+Th,j:j+Tw]
				# imgHist = Histogram(imgSection,20)
				dist = Dist(T,imgSection,bins)
				# print dist

				if isMax == True:
					# dist = HistInterDist(THist,imgHist)
					if i==0 and j==0:
						min_max = dist
						ret = [i,j,i+Th,j+Tw]
					elif dist>min_max:
						min_max = dist
						ret = [i,j,i+Th,j+Tw]

				else:
					if i==0 and j==0:
						min_max = dist
						ret = [i,j,i+Th,j+Tw]

					elif dist<min_max:
						min_max = dist
						ret = [i,j,i+Th,j+Tw]
	print ((ret[1],ret[0]),(ret[3],ret[2]))
	return ret

def VisualiseBox(I,box):
	cv2.rectangle(I,(box[1],box[0]),(box[3],box[2]),(0,255,255),3)
	cv2.imshow("Template Matched", I)
	cv2.waitKey(0)



def HistInterDist(I1,I2,bins):
	hist1 = Histogram(I1,bins)
	hist2 = Histogram(I2,bins)
	return np.sum(np.minimum(hist1,hist2))

def ChiSquareDist(I1,I2,bins):
	hist1 = Histogram(I1,bins)
	hist2 = Histogram(I2,bins)
	denomin = np.add(hist1,hist2)
	numer = np.square(hist1-hist2)
	with np.errstate(divide='ignore',invalid='ignore'):
		result = numer / denomin
		result[denomin == 0] = 0
	return np.sum(result)

def main():
	filename1 = 'template.jpg'
	template = cv2.imread(filename1)
	filename2 = 'starbucks2.jpg'
	img = cv2.imread(filename2)
	# cielab_img = RGB2Lab(img)
	# print cielab_img[:,:,2].mean()
	# print cielab_img
	hist = Histogram(img,8)
	box = SlidingWindowDetector(template,img,ChiSquareDist,False,20)
	VisualiseBox(img,box)
	box = SlidingWindowDetector(template,img,HistInterDist,True,20)
	VisualiseBox(img,box)
	# plt.hist(hist.T)
	# plt.title("Small Histogram")
	# plt.xlabel('l-a-b values')
	# plt.ylabel('count')
	# plt.show()
	# cv2.imshow('cielab_image',cielab_img)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

if __name__ == '__main__':
	main()