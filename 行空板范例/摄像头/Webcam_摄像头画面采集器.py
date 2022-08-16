# 网络摄像头代码，用于采集数据（图像）
# 代码编写：谢作如(2021.4.12)

import remi.gui as gui
from remi import start, App
import time,threading
import qrcode,base64,io,cv2

camera = cv2.VideoCapture(0)
# 临时变量，用于保存画面
tempcam = None
# 图片名称编号
f_num = 1

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
    global tempcam
    success, frame = camera.read()  # read the camera frame
    if success:
        tempcam = frame
        frame = cv2.flip(frame, 1, dst=None)
        frame = cv2.resize(frame, (x, y), interpolation=cv2.INTER_LINEAR)
        image = cv2.imencode('.jpg', frame)[1]
        base64_data = str(base64.b64encode(image))[2:-1]
        data='data:image/jpeg;base64,%s'%base64_data
        return data
    else:
        return get_img("摄像头启动失败")

# Web主程序
class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.VBox(width=700, height=450,style={'margin':'0px auto'})
        bts = gui.HBox(width=300, height=50)
        self.lbl_01 = gui.Label('Web摄像头画面采集器',style={'font-size': '25px'})
        self.lbl_9 = gui.Label(' ')
        self.img_1 = gui.Image(get_frames(640,360))
        self.bt1 = gui.Button('[ 保存画面-按序号命名 ]')
        self.bt2 = gui.Button('[ 保存画面-按时间命名 ]')

        # 按钮按下时执行
        self.bt1.onclick.do(self.on_button_pressed,1)
        self.bt2.onclick.do(self.on_button_pressed,2)

        # 添加到网页上
        container.append(self.lbl_01)
        container.append(self.lbl_9)
        container.append(self.img_1)
        bts.append(self.bt1)
        bts.append(self.bt2)
        container.append(bts)
        
        # 开启新的进程刷新画面
        t = threading.Thread(target=self.showimg)
        t.start()

        # returning the root widget
        return container

    def on_button_pressed(self, emitter, n):
        print(n)
        if n==1:
            global f_num
            f_num = f_num + 1
            cv2.imwrite(str(f_num) + '.jpg',tempcam)
        if n==2:
            f_data = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
            cv2.imwrite(str(f_data) + '.jpg',tempcam)
    # 刷新网页的摄像头画面
    def showimg(self):
        while True:
            self.img_1.set_image(get_frames(640,360))
            time.sleep(0.2)

# starts the web server
start(MyApp,title='摄像头实时视频',address='0.0.0.0',port=8001)
