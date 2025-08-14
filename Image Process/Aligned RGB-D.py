
import depthai as dai
import cv2
import numpy as np

# 建立管線
pipeline = dai.Pipeline()

# 建立 RGB 相機節點
cam_rgb = pipeline.createColorCamera()
cam_rgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
cam_rgb.setInterleaved(False)

# 建立立體相機節點（用於深度）
stereo = pipeline.createStereoDepth()
stereo.setConfidenceThreshold(200)

# 建立 XLink 輸出節點
xout_rgb = pipeline.createXLinkOut()
xout_rgb.setStreamName("rgb")
cam_rgb.video.link(xout_rgb.input)

xout_depth = pipeline.createXLinkOut()
xout_depth.setStreamName("depth")
stereo.depth.link(xout_depth.input)

# 連接左右相機到立體節點
mono_left = pipeline.createMonoCamera()
mono_right = pipeline.createMonoCamera()
mono_left.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
mono_right.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
mono_left.setBoardSocket(dai.CameraBoardSocket.LEFT)
mono_right.setBoardSocket(dai.CameraBoardSocket.RIGHT)
mono_left.out.link(stereo.left)
mono_right.out.link(stereo.right)

# 啟動裝置
with dai.Device(pipeline) as device:
    rgb_queue = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)
    depth_queue = device.getOutputQueue(name="depth", maxSize=4, blocking=False)

    while True:
        rgb_frame = rgb_queue.get().getCvFrame()
        depth_frame = depth_queue.get().getFrame()

        # 將深度影像轉換為可視化格式
        depth_vis = cv2.normalize(depth_frame, None, 0, 255, cv2.NORM_MINMAX)
        depth_vis = cv2.applyColorMap(depth_vis.astype(np.uint8), cv2.COLORMAP_JET)

        # 顯示影像
        cv2.imshow("RGB", rgb_frame)
        cv2.imshow("Depth", depth_vis)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()
