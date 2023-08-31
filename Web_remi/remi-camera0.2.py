# 摄像头控制（云台版本），0.2
# 代码编写：谢作如(2021.4.12)
# 代码修改：谢作如（2023.8.4）
# 使用说明：访问8001端口，启动失败将显示二维码

import remi.gui as gui
from remi import start, App
import time,threading
import qrcode,base64,io,cv2

camera = cv2.VideoCapture(0)

# 二维码信息提示
def get_img(data):
    img = qrcode.make(data)
    out = io.BytesIO()
    img.save(out, 'PNG')
    base64_data=base64.b64encode(out.getvalue())
    s=base64_data.decode()
    data='data:image/jpeg;base64,%s'%s
    return data

# 返回摄像头画面，自定义大小
def get_frames(x,y): 
    success, frame = camera.read()  # read the camera frame
    if success:
        frame = cv2.flip(frame, 1, dst=None)
        frame = cv2.resize(frame, (x, y), interpolation=cv2.INTER_LINEAR)
        image = cv2.imencode('.jpg', frame)[1]
        base64_data = str(base64.b64encode(image))[2:-1]
        data='data:image/jpeg;base64,%s'%base64_data
        return data
    else:
        return get_img("摄像头启动失败，请检查摄像头是否连接！")

# Web主程序
class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.VBox(width=600, height=420,style={'margin':'0px auto'})
        bts = gui.HBox(width=300, height=50)
        self.lbl_01 = gui.Label('Web摄像头云台控制',style={'font-size': '25px'})
        self.lbl_9 = gui.Label(' ')
        self.img_1 = gui.Image(get_frames(400,300))
        self.bt1 = gui.Button('[ 上 ]')
        self.bt2 = gui.Button('[ 下 ]')
        self.bt3 = gui.Button('[ 左 ]')
        self.bt4 = gui.Button('[ 右 ]')

        # 按钮按下时执行
        self.bt1.onclick.do(self.on_button_pressed,0)
        self.bt2.onclick.do(self.on_button_pressed,1)
        self.bt3.onclick.do(self.on_button_pressed,2)
        self.bt4.onclick.do(self.on_button_pressed,3)

        # 添加到网页上
        container.append(self.lbl_01)
        container.append(self.img_1)
        
        # 将按钮放在一行
        bts.append(self.bt1)
        bts.append(self.bt2)
        bts.append(self.bt3)
        bts.append(self.bt4)
        print(bts)
        container.append(bts)
        # 提示文字
        container.append(self.lbl_9)
        
        # 开启新的进程刷新画面
        t = threading.Thread(target=self.showimg)
        t.start()

        # returning the root widget
        return container

    def on_button_pressed(self, emitter, n):
        # print(n)
        temp = ['上','下','左','右']
        self.lbl_9.set_text('你按下了“' + temp[n] +'”')
        
    #
    def showimg(self):
        while True:
            self.img_1.set_image(get_frames(400,300))
            time.sleep(0.2)

# starts the web server
start(MyApp,title='实时视频',address='0.0.0.0',port=8001)
