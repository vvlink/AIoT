import cv2

# 打开默认的摄像头（通常是内置摄像头）
cap = cv2.VideoCapture(0)

while True:
    # 读取每一帧
    ret, frame = cap.read()
    
    if not ret:
        break
        
    # 将当前帧保存为 "test.jpg"
    cv2.imwrite('test.jpg', frame)

# 释放摄像头资源
cap.release()
cv2.destroyAllWindows()
