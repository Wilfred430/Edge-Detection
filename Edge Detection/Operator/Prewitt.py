import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

img = cv2.imread('D:\Edge Project\Gray Photo\gray_fighter.jpg', cv2.IMREAD_GRAYSCALE)

# Prewitt kernel
kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

prewittx = convolve(img, kernelx)
prewitty = convolve(img, kernely)

prewitt = np.hypot(prewittx, prewitty)

plt.imshow(prewitt, cmap='gray')
plt.title('Prewitt Edge Detection')
plt.show()