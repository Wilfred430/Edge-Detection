import cv2

# 輸入與輸出影片路徑
input_video_path = 'D:/Edge Project/Video Storage/crowd.mp4'
output_video_path = 'C:/Users/user/Downloads/gray_crowd.mp4'

# 開啟影片
cap = cv2.VideoCapture(input_video_path)

# 取得影片屬性
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# 建立輸出影片物件（灰階影片）
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height), isColor=True)

# 逐幀處理
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 將彩色幀轉為灰階
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_3ch = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

    # 寫入灰階幀
    out.write(gray_frame_3ch)

# 釋放資源
cap.release()
out.release()

print(f"灰階影片已儲存為 {output_video_path}")
