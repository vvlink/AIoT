# 按钮测试数字输入
# 按钮A：P5，按钮B：P11
from pinpong.board import Board,Pin
Board("handpy").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
from pinpong.extension.handpy import HPScreen
import time
esp32 = HPScreen()
esp32.display_in_line("请按下按钮，观察屏幕变化",1)
button_a = Pin(Pin.P5, Pin.IN) #引脚初始化为数字输入
button_b = Pin(Pin.P11, Pin.IN) #引脚初始化为数字输入
while True:
    val_a = button_a.read_digital()
    val_b = button_b.read_digital()
    esp32.display_clear_in_line(2)
    esp32.display_in_line(str(val_a),2)
    esp32.display_clear_in_line(3)
    esp32.display_in_line(str(val_b),3)
    time.sleep(0.1)
    