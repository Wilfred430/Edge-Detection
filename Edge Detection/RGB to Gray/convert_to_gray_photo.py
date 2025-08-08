import cv2

# 讀取彩色影像
image = cv2.imread("D:/Edge Project/Photo Storage/fighter.jpg")

# 轉換為灰階影像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 儲存灰階影像
cv2.imwrite("D:/Edge Project/Gray Item/gray_fighter.jpg", gray_image)

# 顯示影像（可選）
cv2.imshow("Gray Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()