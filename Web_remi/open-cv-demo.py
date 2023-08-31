# opencv样例

import cv2
import json
import time
import base64
import numpy as np


def b64_to_cvimg(b64):
    try:
        imgData = base64.b64decode(b64)
        nparr = np.frombuffer(imgData, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img
    except Exception as e:
        return "error"

def cvimg_to_b64(img):
    try:
        image = cv2.imencode('.jpg', img)[1]
        base64_data = str(base64.b64encode(image))[2:-1]
        return base64_data
    except Exception as e:
        return "error"


def main():
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        if ret == True:
            frame=cv2.flip(frame,1,dst=None)
            frame=cv2.resize(frame,(1280,800),interpolation=cv2.INTER_LINEAR)                
            # Display the resulting frame
            cv2.imshow('Magic Image',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

main()


