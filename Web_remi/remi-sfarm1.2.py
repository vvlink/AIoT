# 将该程序的地址(IP地址加8001端口)做成二维码，手机扫描后就可以访问，可以快速查看信息，控制浇水。
# 支持多个设备，同时在页面中生成二维码。
# 代码编写：谢作如(2021.4.13)

import remi.gui as gui
from remi import start, App
import siot,time
import threading
import qrcode,base64,io,socket

topic_msg_map={}
i = 0
# 设备名称列表
project_list= ['sf88','sf89'] 
# 设备编号默认先呈现第一个
id = 0

iot_server = '192.168.3.41' # mqtt服务器地址
iot_user = 'scope'
iot_pwd = 'scope'

# 获取IP地址
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

# 处理订阅消息
def on_topic_subscribe(client,userdata,msg):
    global topic_msg_map
    topic_msg_map[str(msg.topic)]=str(msg.payload.decode())

def on_topic_read(topic):
    global topic_msg_map
    result=topic_msg_map.get(topic,None)
    if result:
        del topic_msg_map[topic]
        return str(result)

data='http://' + get_host_ip() + ':8001'
img = qrcode.make(data)
out = io.BytesIO()
img.save(out, 'PNG')
base64_data=base64.b64encode(out.getvalue())
s=base64_data.decode()
data='data:image/jpeg;base64,%s'%s

siot.init('remi',iot_server,user=iot_user,password=iot_pwd)
siot.connect()
for item in project_list:
    siot.subscribe(item + '/light',on_topic_subscribe)
    siot.subscribe(item + '/soil',on_topic_subscribe)
siot.loop()

# Web主程序
class MyApp(App):
    global i,project_list,id
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.VBox(width=400, height=340,style={'margin':'0px auto'})
        self.lbl_01 = gui.Label('开源智慧农场监控页面',style={'font-size': '25px'})
        self.dd = gui.DropDown(['设备编号：' + x for x in project_list],width=150,style={'font-size': '12px'})
        self.lbl_1 = gui.Label('环境光照值：等待数据中')
        self.lbl_2 = gui.Label('土壤湿度值：等待数据中')
        self.lbl_9 = gui.Label(' ')
        self.img_1 = gui.Image(data,width=150, height=150)

        
        self.bt = gui.Button('[ 浇水 ]')

        # 选择时执行
        self.dd.onchange.do(self.on_dropdown_onchange)
        
        # 按钮按下时执行
        self.bt.onclick.do(self.on_button_pressed)

        # 添加到网页上
        container.append(self.lbl_01)
        container.append(self.dd)
        container.append(self.lbl_1)
        container.append(self.lbl_2)
        container.append(self.bt)
        container.append(self.lbl_9)
        container.append(self.img_1)
        
        # 开启新的进程处理MQTT消息
        t = threading.Thread(target=self.showmqtt)
        t.start()

        # returning the root widget
        return container

    # 选择设备
    def on_dropdown_onchange(self, emitter, new_value):
        global id
        # print(new_value)
        id = project_list.index(new_value[5:])
        self.lbl_1.set_text('环境光照值：等待数据')
        self.lbl_2.set_text('土壤湿度值：等待数据')
        
    
    # 发送MQTT消息
    def on_button_pressed(self, widget):
        global i
        i = i+1
        siot.publish(project_list[id] + '/relay','1')
        self.lbl_9.set_text('成功发送浇水指令！次数：' + str(i))
    
    # 处理MQTT消息
    def showmqtt(self):
        while True:
            getcmd = on_topic_read(project_list[id] + '/light')
            if getcmd:
                self.lbl_1.set_text('环境光照值：' + getcmd)
            getcmd = on_topic_read(project_list[id] + '/soil')
            if getcmd:
                self.lbl_2.set_text('土壤湿度值：' + getcmd)
            time.sleep(1)
        
# starts the web server
start(MyApp,address='0.0.0.0',port=8001)
