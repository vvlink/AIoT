# 定时保存摄像头图片
import cv2,time
def getcampic(fname):
    cap = cv2.VideoCapture(0)        # 打开摄像头
    time.sleep(1) # 等待1秒，避免黑屏
    ret, frame = cap.read()       # 读摄像头
    cv2.imwrite(fname,frame)
    cap.release()  
    return True
i = 1
while i<30:
    fname = str(i) + ".jpg"
    getcampic(fname)
    print(fname + "已经保存！")
    time.sleep(10)
    i = i + 1
