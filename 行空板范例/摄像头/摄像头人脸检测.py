# 将保存摄像头画面，如果发现人脸则框出
import cv2
def faceDetect(img, face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")):
    size = img.shape[:2]
    divisor = 8
    h, w = size
    minSize = (w // divisor, h // divisor)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 1, cv2.CASCADE_SCALE_IMAGE, minSize)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return img, len(faces)

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if ret:
    frame1, face_num = faceDetect(frame)
    print("发现人脸数量：" + str(face_num))
    img=frame1[:,:,::-1]
    cv2.imwrite('face.jpg',img)
else:
    print("没有接摄像头或者摄像头被占用！")
cap.release()