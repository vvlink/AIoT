# 数据订阅主题
# 这是服务器版本

from pywebio.input import input,file_upload,input_group,TEXT
from pywebio.output import put_text,put_image
from pywebio import start_server
import siot,time

topicid_p = 'sfarm/relay'
iot_server = '192.168.3.177' # mqtt服务器地址
iot_user = 'scope'
iot_pwd = 'scope'

# 处理订阅消息
def on_topic_subscribe(client,userdata,msg):
    global topic_msg_map
    put_text('收到主题消息：' + str(msg.payload.decode()));

# Web主程序
def app():
    global topicid_p
    siot.init('webio',iot_server,user=iot_user,password=iot_pwd)
    siot.connect()
    put_text('当前连接的MQTT服务器是：' + iot_server);
    while True:
        info=input_group('物联网消息', [
            input('请输入要发送的主题：', name='x1',value = topicid_p, type=TEXT),
            input('请输入要发送的数据：', name='x2', type=TEXT),
            ])
        topicid_p = info['x1']
        s = info['x2']
        siot.publish(topicid_p,s)
        put_text('给主题“ %s”，发送了消息: %s' % (topicid_p,s));

start_server(app, port=8080, debug=True)

