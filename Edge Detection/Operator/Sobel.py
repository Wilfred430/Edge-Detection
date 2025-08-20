import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:\Edge Project\Gray Photo\gray_fighter.jpg', cv2.IMREAD_GRAYSCALE)

# Sobel X 和 Y
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# 邊緣強度
sobel = cv2.magnitude(sobelx, sobely)

plt.imshow(sobel, cmap='gray')
plt.title('Sobel Edge Detection')
plt.show()