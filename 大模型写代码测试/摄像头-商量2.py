import cv2

def press_key():
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            return False
        elif key == ord('a'):
            print("Saving image...")
            cv2.imwrite('test.jpg', img)
            
cam = cv2.VideoCapture(0)
if cam is None or not press_key():
    exit()

while True:
    _, img = cam.read()
    cv2.imshow('Camera Feed', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:   # 按 'ESC' 键退出
        break
else:
    pass

print("\nExiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
exit()