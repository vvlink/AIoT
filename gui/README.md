# GUI界面编写

使用PySimpleGUI库编写GUI界面。

## 介绍

顾名思义，PySimpleGUI是一个简单的GUI设计工具。PySimpleGUI的安装和其他库一样，使用pip命令即可。整个库很小，很快就能完成。参考命令如下：

pip install  PySimpleGUI

## 带GUI界面的AI应用范例

使用PySimpleGUI库编写的带GUI界面摄像头实时推理程序，Web页面形式呈现。

如果将“import PySimpleGUIWeb as sg”改为“import PySimpleGUI as sg”，就是普通的应用程序界面。

### webgui_infer_auto_cls.py

实时图像分类，模型为1000分类预训练模型（MobielNet）。


### webgui_infer_auto_det.py

实时目标检测，模型为80类目标检测预训练模型（SSD_Lite）。




