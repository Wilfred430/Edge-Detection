import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

img = cv2.imread('D:\Edge Project\Gray Photo\gray_fighter.jpg', cv2.IMREAD_GRAYSCALE)

# Robert kernel
kernelx = np.array([[1, 0], [0, -1]])
kernely = np.array([[0, 1], [-1, 0]])

robertsx = convolve(img, kernelx)
robertsy = convolve(img, kernely)

roberts = np.hypot(robertsx, robertsy)

plt.imshow(roberts, cmap='gray')
plt.title('Roberts Edge Detection')
plt.show()