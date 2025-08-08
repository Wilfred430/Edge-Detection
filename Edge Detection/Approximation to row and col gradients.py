import cv2
import numpy as np
import matplotlib.pyplot as plt

# 讀取灰階影像
image = cv2.imread('D:/Edge Project/Gray Photo/gray_fighter.jpg', cv2.IMREAD_GRAYSCALE)

# 計算 row 和 column 梯度（使用簡單差分）
grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # 水平方向
grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # 垂直方向

# 計算梯度大小
gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)

# 正規化梯度值到 [0, 1]
normalized_gradient = cv2.normalize(gradient_magnitude, None, 0, 1, cv2.NORM_MINMAX)

# 設定閾值 t = 0.05，產生二值圖
t = 0.05
binary_map = (normalized_gradient >= t).astype(np.uint8) * 255  # 轉為 0 或 255

# 顯示結果
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Gray Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title(f"Binary Indicator Map (t = {t})")
plt.imshow(binary_map, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
