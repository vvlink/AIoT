# PySimpleGUI的基本窗体（TK）
import PySimpleGUI as sg

layout = [
    [sg.Text('请输入你的名字：')],
    [sg.Input(key='in')],
    [sg.Button('确认'), sg.Button('取消')],
    [sg.Text('输出：'), sg.Text(key='out')]
]
window = sg.Window('PySimpleGUI 范例', layout)
while True:
    # event为按钮的名称，values为一个字典
    event, values = window.read()
    print(event,values)
    if event in (None, '取消'):
        window['in'].update('')
        window['out'].update('')
    else:
        if values:
            s = '欢迎你，' + values['in']
        window['out'].update(s)
window.close()