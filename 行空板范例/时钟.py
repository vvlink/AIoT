# 实时更新的时钟
from unihiker import GUI   #导入包
import time
gui=GUI()  #实例化GUI类
cur_time = time.strftime('%Y-%m-%d\n\n %X', time.localtime())
text1 = gui.draw_digit(x=120, y=160, text=cur_time, origin = "center",color="red",font_size=25)#数码管字体显示
while True:
    #增加等待，防止程序退出和卡住
    cur_time = time.strftime('%Y-%m-%d\n\n %X', time.localtime())
    text1.config(text=cur_time)
    time.sleep(1)