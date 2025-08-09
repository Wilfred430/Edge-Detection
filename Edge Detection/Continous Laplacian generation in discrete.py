import numpy as np
import cv2
import matplotlib.pyplot as plt

# 定義 Laplacian kernel 4-neighbor（離散形式）
laplacian_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float32)

laplacian_kernel_8 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]], dtype=np.float32)

# 讀取灰階影像
image = cv2.imread("D:/Edge Project/Gray Photo/gray_couple.jpg", cv2.IMREAD_GRAYSCALE)

# 套用卷積（convolution）
laplacian_result = cv2.filter2D(image, ddepth=cv2.CV_64F, kernel=laplacian_kernel)

laplacian_result_8 = cv2.filter2D(image, ddepth=cv2.CV_64F, kernel=laplacian_kernel_8)

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title("Original Gray Image")
plt.imshow(image, cmap="gray")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Laplacian Edge Detection (4)")
plt.imshow(np.abs(laplacian_result), cmap="gray")  # 取絕對值避免負數
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Laplacian Edge Detection (8)")
plt.imshow(np.abs(laplacian_result_8), cmap="gray")  # 取絕對值避免負數
plt.axis("off")

plt.tight_layout()
plt.show()
