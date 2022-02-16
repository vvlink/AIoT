from pinpong.board import Board,Pin
Board("handpy").begin()#初始化，选择板型和端口号，不输入端口号则进行自动识别
from pinpong.extension.handpy import HPScreen
esp32 = HPScreen()
#屏幕显示"pinpong库"在第一行
esp32.display_in_line("PinPong库",1)