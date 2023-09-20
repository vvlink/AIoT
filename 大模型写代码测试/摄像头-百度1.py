import cv2  
  
# 0代表我们将使用计算机的主摄像头  
cap = cv2.VideoCapture(0)   
  
if not cap.isOpened():  
    print("无法打开摄像头")  
    exit()  
  
# 我们将循环进行捕捉，直到按下 'q'键  
while True:  
    # Capture frame-by-frame  
    ret, frame = cap.read()  
  
    if not ret:  
        print("无法接收帧（Can't receive frame）。")  
        break  
  
    # 显示结果帧  
    cv2.imshow('frame', frame)  
    if cv2.waitKey(1) == ord('q'):  
        break  
  
# 当一切都结束后，关闭摄像头  
cap.release()  
cv2.destroyAllWindows()  
  
# 将帧保存为图片  
cv2.imwrite('test.jpg', frame)