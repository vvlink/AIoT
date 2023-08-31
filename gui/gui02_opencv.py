# 带窗体的摄像头程序
import PySimpleGUI as sg  #pip install pysimplegui
import cv2  #pip install opencv-python
import numpy as np #pip install numpy
#背景色
sg.theme('LightGreen')
#定义窗口布局
layout = [
  [sg.Image(filename='', key='image',size=(600, 400))],
  [sg.Button('保存', size=(10, 1))],
  [sg.Button('关闭', size=(10, 1))]
]

#窗口设计
window = sg.Window('OpenCV实时图像处理',layout,size=(600, 500))
#打开内置摄像头
cap = cv2.VideoCapture(0)
while True:
    event, values = window.read(timeout=0, timeout_key='timeout')

    #实时读取图像，重设画面大小
    ret, frame = cap.read()
    imgSrc = cv2.resize(frame,(600, 400))

    #画面实时更新
    imgbytes = cv2.imencode('.png', imgSrc)[1].tobytes()
    window['image'].update(data=imgbytes)
    if event in (None, '保存'):
        cv2.imwrite('test.png', frame)
        print('图片保存成功！')
    if event in (None, '关闭'):
        break
# 推出窗体
cap.release()
window.close()