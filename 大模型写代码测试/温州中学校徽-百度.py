import turtle  
import math  
  
# 定义一些常量  
THICKNESS = 30  
COLOR = "blue"  
ANGLE_1 = 60  
ANGLE_2 = 35  
ANGLE_3 = 200  
RADIUS = 100  # 可以根据需要调整半圆的半径  
HEXAGON_SIDE_LENGTH = 100  # 六边形的边长，可以根据需要调整  
  
# 创建一个turtle对象  
t = turtle.Turtle()  
t.pensize(THICKNESS)  # 设置线条粗细  
t.color(COLOR)  # 设置颜色  
  
# 绘制六边形  
for _ in range(6):  
    t.forward(HEXAGON_SIDE_LENGTH)  
    t.right(60)  
  
# 向右旋转60度  
t.right(ANGLE_1)  
  
# 记录当前位置  
temp = t.position()  
  
# 向前移动2*六边形边长的距离  
t.forward(2 * HEXAGON_SIDE_LENGTH)  
  
# 提笔，回到temp位置，落笔  
t.penup()  
t.goto(temp)  
t.pendown()  
  
# 向左旋转35度  
t.left(ANGLE_2)  
  
# 向右绘制1/4个半圆  
t.circle(RADIUS, -90)  # 绘制半圆，角度为负数表示逆时针旋转  
  
# 提笔，回到temp位置，落笔  
t.penup()  
t.goto(temp)  
t.pendown()  
  
# 向左旋转200度  
t.left(ANGLE_3)  
  
# 向左绘制1/4个半圆  
t.circle(-RADIUS, -90)  # 绘制半圆，角度为负数表示逆时针旋转，半径为负表示反向绘制半圆  
  
turtle.done()