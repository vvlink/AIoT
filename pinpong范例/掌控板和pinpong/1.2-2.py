# 触摸背面的0，屏幕输出电平状态
from pinpong.board import Board,Pin
Board("handpy").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
from pinpong.extension.handpy import HPScreen
import time
esp32 = HPScreen()
esp32.display_in_line("请用手触摸背面的0",1)
p0 = Pin(Pin.P0, Pin.ANALOG) #引脚初始化为电平输出 模拟输入方法2
while True:
    v = p0.read_analog()
    esp32.display_clear_in_line(2)
    esp32.display_in_line(str(v),2)
    time.sleep(0.1)
    