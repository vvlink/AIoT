# 带窗体的摄像头程序，自动推理
# 模型为80类目标检测预训练模型（SSD_Lite）
import remi
import PySimpleGUIWeb as sg
import BaseDeploy as bd
import cv2  #pip install opencv-python

model_path = 'det.onnx'
model = bd(model_path)

def my_inf(frame):
    global model
    res1, img = model.inference(frame,get_img='cv2')
    # 转化推理结果
    res2 = model.print_result(res1)
    if len(res2) == 0:
        return None,None
    classes = []
    print(res2)
    # 提取预测结果
    for res in res2:
        classes.append(res['预测结果'])
    return str(classes),img

#背景色
sg.theme('LightGreen')
#定义窗口布局
layout = [
  [sg.Image(filename='', key='image',size=(600, 400))],
  [sg.Button('关闭', size=(20, 1))],
  [sg.Text('推理结果：',key='res')]
]

# 建立窗体
window = sg.Window('OpenCV实时图像处理',layout,size=(600, 500))
#打开摄像头
cap = cv2.VideoCapture(0)
while True:
    event, values = window.read(timeout=0, timeout_key='timeout')
    if event in (None, '关闭'):
        break
    #实时读取图像，重设画面大小
    ret, frame = cap.read()
    imgSrc = cv2.resize(frame, (600,400))
    res, img = my_inf(frame)
    # 实时更新画面
    if res:
        window['res'].update('推理结果：'+res)
        imgbytes = cv2.imencode('.png', img)[1].tobytes()
    else:
        imgbytes = cv2.imencode('.png', imgSrc)[1].tobytes()
    window['image'].update(data=imgbytes)
# 退出窗体
cap.release()
window.close()