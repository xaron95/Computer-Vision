import numpy as np
def avg_mirror(img):
	x = np.fliplr(img)
	return (img/2)+(x/2)