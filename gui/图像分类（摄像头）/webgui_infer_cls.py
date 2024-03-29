'''
带窗体的摄像头程序，用按钮保存后推理，模型为1000分类预训练模型（MobielNet）。
将“import PySimpleGUIWeb as sg”改为“import PySimpleGUI as sg”即可使用TK的界面
'''
import PySimpleGUIWeb as sg
import BaseDeploy as bd
import cv2  #pip install opencv-python

def my_inf(frame):
    model_path = 'cls_imagenet.onnx'
    model = bd(model_path)
    result1 = model.inference(frame)
    result2 = model.print_result(result1)
    return result2

#背景色
sg.theme('LightGreen')
#定义窗口布局
layout = [
  [sg.Image(filename='', key='image',size=(600, 400))],
  [sg.Button('保存并推理', size=(20, 1))],
  [sg.Button('关闭', size=(20, 1))],
  [sg.Text('推理结果：',key='res')]
]

#窗口设计
window = sg.Window('OpenCV实时图像处理',layout,size=(600, 500))
#打开内置摄像头
cap = cv2.VideoCapture(1)
while True:
    event, values = window.read(timeout=0, timeout_key='timeout')
    #实时读取图像，重设画面大小
    ret, frame = cap.read()
    imgSrc = cv2.resize(frame, (600,400))

    #画面实时更新
    imgbytes = cv2.imencode('.png', imgSrc)[1].tobytes()
    window['image'].update(data=imgbytes)
    if event in (None, '保存并推理'):
        cv2.imwrite('test.png', frame)
        print('图片保存成功！')
        res=my_inf(frame)
        print('推理结果为：',res)
        window['res'].update('推理结果：'+res['预测结果'])
    if event in (None, '关闭'):
        break
# 关闭窗体
cap.release()
window.close()