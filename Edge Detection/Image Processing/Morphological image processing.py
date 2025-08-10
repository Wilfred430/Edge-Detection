import cv2
import numpy as np
import matplotlib.pyplot as plt

# 讀取灰階影像
image = cv2.imread('D:/Edge Project/Processed Image/prcess_couple.jpg', cv2.IMREAD_GRAYSCALE)

# 二值化（確保只有 0 與 255）
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 定義 3×3 核（全部 1）
kernel = np.ones((3, 3), np.uint8)

# Morph1：先腐蝕再膨脹（Opening），移除孤立小白點
morph1_result = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# 顯示結果
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Binary")
plt.imshow(binary, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Morph1 (Remove Isolated Pixels)")
plt.imshow(morph1_result, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
