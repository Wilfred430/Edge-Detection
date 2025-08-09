import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
from PIL import Image

# Step 1: 建立 5x5 的 x 和 y 階梯矩陣
x = np.tile(np.arange(-2, 3), (5, 1))  # 每列為 [-2, -1, 0, 1, 2]
y = np.tile(np.arange(-2, 3).reshape(5, 1), (1, 5))  # 每行為 [-2, -1, 0, 1, 2]

# Step 2: 根據 θ 建立 edge fitting matrix
theta = np.pi / 4  # 45 度方向
theta_2 = -np.pi / 4
s = (x * np.cos(theta) + y * np.sin(theta)) < 0
s_2 = (x * np.cos(theta_2) + y * np.sin(theta_2)) < 0
s = s.astype(float)
s_2 = s_2.astype(float)

# Step 3: 載入灰階影象
image = Image.open("D:/Edge Project/Gray Photo/gray_couple.jpg").convert("L")
image_np = np.array(image)
# Step 4: 對影像進行卷積
edge_image = convolve(image_np, s)
edge_image_2 = convolve(image_np, s_2)
# Step 5: 顯示結果
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(image_np, cmap="gray")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Edge Detection Result (45)")
plt.imshow(edge_image, cmap="gray")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Edge Detection Result (-45)")
plt.imshow(edge_image_2, cmap="gray")
plt.axis("off")
plt.tight_layout()
plt.show()
