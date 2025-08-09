import cv2
import numpy as np
import matplotlib.pyplot as plt

# 讀取灰階影像
image = cv2.imread("D:/Edge Project/Gray Photo/gray_couple.jpg", cv2.IMREAD_GRAYSCALE)
image = image.astype(np.float64)  # 為了避免溢位，轉成 float64

# 建立與原圖大小相同的空陣列
G1 = np.zeros_like(image)
G2 = np.zeros_like(image)

# 主對角線方向梯度：F(j+1, k+1) - F(j, k)
G1[:-1, :-1] = image[1:, 1:] - image[:-1, :-1]

# 副對角線方向梯度：F(j, k+1) - F(j+1, k)
G2[:-1, :-1] = image[:-1, 1:] - image[1:, :-1]

# 計算對角線方向的綜合梯度大小
gradient_magnitude = np.sqrt(G1**2 + G2**2)

# 正規化
normalized_gradient = cv2.normalize(gradient_magnitude, None, 0, 1, cv2.NORM_MINMAX)

# 閾值處理
t = 0.045
binary_map = (normalized_gradient >= t).astype(np.uint8) * 255

# 顯示結果
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Gray Image")
plt.imshow(image, cmap="gray")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title(f"Diagonal Edge Map (t = {t})")
plt.imshow(binary_map, cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.show()
