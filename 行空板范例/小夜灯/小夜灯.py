from unihiker import GUI  # 导入unihiker库
import time  # 导入time库

from pinpong.board import Board # 从pinpong.board包中导入Board模块
from pinpong.extension.unihiker import * # 导入pinpong.extension.unihiker包中所有模块

Board().begin() # 初始化，选择板型和端口号，不输入则进行自动识别

gui = GUI()  # 实例化GUI类，创建gui对象

img = gui.draw_image(x=0,y=0,w=240, h=320, image='light-1.png')# 显示初始背景图为light-1
value = gui.draw_text(x=145, y=28, text='0', font_size=18) # 显示初始光线值

while True :
    Light = light.read() # 读取光线值
    value.config(text = Light) # 更新显示光线值
    # 光线值等级
    if 0 <= Light < 1024:
        img.config(image='light-2.png')  # 切换背景图为light-2
    elif 1024 <= Light < 2048:
        img.config(image='light-3.png')  # 切换背景图为light-3
    elif 2048 <= Light < 3072:
        img.config(image='light-4.png')  # 切换背景图为light-4   
    else:
        img.config(image='light-5.png')  # 切换背景图为light-5

    time.sleep(1) # delay 1 秒