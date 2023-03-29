from pywebio.input import *
from pywebio.output import *
 
# 文本输入
s = input('请输入你的名字：')
 
# 输出文本
put_text('欢迎你，' + s)
