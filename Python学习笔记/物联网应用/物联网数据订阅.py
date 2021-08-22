# 数据订阅主题
# 这是服务器版本
# 没有成功，可能需要开多线程

from pywebio.input import input,file_upload,TEXT
from pywebio.output import put_text,put_image
from pywebio import start_server
import siot,time

topicid_b = 'sfarm/air'
iot_server = '192.168.3.177' # mqtt服务器地址
iot_user = 'scope'
iot_pwd = 'scope'

# 处理订阅消息
def on_topic_subscribe(client,userdata,msg):
    put_text('收到主题消息：' + str(msg.payload.decode()));

# Web主程序
def app():
    global topicid_b
    siot.init('webio',iot_server,user=iot_user,password=iot_pwd)
    siot.connect()
    put_text('当前连接的MQTT服务器是：' + iot_server);
    while True:
        topicid_b = input('请输入要订阅的主题：',value = topicid_b, type=TEXT)
        siot.subscribe(topicid_b,on_topic_subscribe)
        siot.loop()
        put_text('当前订阅的主题是：' + topicid_b);

start_server(app, port=8080, debug=True)

