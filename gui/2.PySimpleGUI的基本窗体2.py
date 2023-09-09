# PySimpleGUI的基本窗体（TK）
import PySimpleGUI as sg

layout = [
    [sg.Text('请输入你的名字和性别：')],
    [sg.Input(key='in01')],
    [sg.Input(key='in02')],
    [sg.Button('确认'), sg.Button('取消')],
    [sg.Text('输出：'), sg.Text(key='out01')]
]
window = sg.Window('PySimpleGUI 范例', layout)
while True:
    # event为按钮的名称，values为一个字典
    event, values = window.read()
    print(event)
    print(values)
    if values['in02']=='男':
        s = values['in01'] + '先生'
    else:
        s = values['in01'] + '女士' 
    if event in (None, '取消'):
        pass
    else:
        window['out01'].update(s)
window.close()