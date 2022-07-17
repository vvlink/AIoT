import time
from pinpong.board import Board,Pin,DHT11
from unihiker import GUI
Board().begin()
gui = GUI()
dht11 = DHT11(Pin(Pin.D23))
led = Pin(Pin.P24,Pin.OUT)
text1 = gui.draw_text(x = 40,y=120,text="temperature:",color="red")
text2 = gui.draw_text(x = 160,y=120,color="red")
text3 = gui.draw_text(x = 40,y=200,text="humidity:",color="red")
text4 = gui.draw_text(x = 160,y=200,color="red")
while True:
    temp = dht11.temp_c()
    humi = dht11.humidity()
    if temp > 30:
        # led.value(1)
        led.write_digital(1)
    else:
        # led.value(0)
        led.write_digital(0)
    # print("temperature=",temp,"humidity=",humi)

    text2.config(text=temp)
    text4.config(text=humi)
    time.sleep(1)
