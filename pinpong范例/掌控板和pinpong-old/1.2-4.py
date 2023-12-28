# 按钮控制蜂鸣器
# 按钮A：P5，按钮B：P11，蜂鸣器：P6
from pinpong.board import Board,Pin
Board("handpy").begin() #板型为掌控板，端口号自动识别
from pinpong.extension.handpy import HPScreen
import time
esp32 = HPScreen()
esp32.display_in_line("请按下按钮，观察屏幕变化",1)
button_a = Pin(Pin.P5, Pin.IN) #引脚设置为数字输入
button_b = Pin(Pin.P11, Pin.IN) #引脚设置为数字输入
buzzer = Pin(Pin.P6, Pin.PWM) #引脚设置为模拟输出
while True:
    val_a = button_a.read_digital()
    val_b = button_b.read_digital()
    esp32.display_clear_in_line(2)
    esp32.display_in_line(str(val_a) + ',' + str(val_b),2)
    if (val_a != val_b):
        buzzer.write_analog(1000)
    else:
        buzzer.write_analog(0)
    time.sleep(0.1)
    