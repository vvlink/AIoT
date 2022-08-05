import cv2

screen_rotation = True
#False:不旋转屏幕（竖屏显示，上下会有白边）
#True：旋转屏幕（横屏显示）

cap = cv2.VideoCapture(0)   #设置摄像头编号，如果只插了一个USB摄像头，基本上都是0
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  #设置摄像头图像宽度
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240) #设置摄像头图像高度
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)     #设置OpenCV内部的图像缓存，可以极大提高图像的实时性。

cv2.namedWindow('camera',cv2.WND_PROP_FULLSCREEN)    #窗口全屏
cv2.setWindowProperty('camera', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)   #窗口全屏

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue
    if screen_rotation: #是否要旋转屏幕
        image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE) #旋转屏幕
    cv2.imshow('camera', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()