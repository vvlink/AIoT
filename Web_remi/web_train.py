# 实现模型训练
# 代码编写：谢作如(2023.7.27)

import remi.gui as gui
from remi import start, App
import time,threading

# Web主程序
class MyApp(App):
    global i
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        vhtml = gui.VBox(width=400, height=360,style={'margin':'0px auto'})
        self.lbl_00 = gui.Label('XEdu无代码模型训练插件',style={'font-size': '25px'})
        div_1 = gui.HBox(width=400, height=60)
        self.lbl_01 = gui.Label('选择模型：')
        self.in_01 = gui.Input('')
        div_1.append(self.lbl_01)
        div_1.append(self.in_01)
        div_2 = gui.HBox(width=400, height=60)
        self.lbl_02 = gui.Label('数据集地址：')
        self.in_02 = gui.Input('')
        div_2.append(self.lbl_02)
        div_2.append(self.in_02)
        div_3 = gui.HBox(width=400, height=60)
        self.lbl_03 = gui.Label('分类数量：')
        self.in_03 = gui.Input('')
        div_3.append(self.lbl_03)
        div_3.append(self.in_03)
        div_4 = gui.HBox(width=400, height=60)
        self.lbl_04 = gui.Label('权重保存地址：')
        self.in_04 = gui.Input('')
        div_4.append(self.lbl_04)
        div_4.append(self.in_04)
        div_5 = gui.HBox(width=400, height=60)
        self.lbl_05 = gui.Label('是否验证：')
        self.in_05 = gui.CheckBox(checked=False, user_data='True')
        div_5.append(self.lbl_05)
        div_5.append(self.in_05)
        
        self.bt = gui.Button('[ 浇水 ]')

        # 按钮按下时执行
        self.bt.onclick.do(self.on_button_pressed)

        # 添加到网页上
        vhtml.append(self.lbl_00)
        vhtml.append(div_1)
        vhtml.append(div_2)
        vhtml.append(div_3)
        vhtml.append(div_4)
        vhtml.append(self.bt)
        return vhtml

    # 训练
    def on_button_pressed(self, widget):
        self.lbl_9.set_text('成功发送浇水指令！次数：' + str(i))
        # 开启新的进程训练
        t = threading.Thread(target=self.showmqtt)
        t.start()
        
# starts the web server
start(MyApp,address='0.0.0.0',port=8001)