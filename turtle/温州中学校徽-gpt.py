import turtle

# 设置画笔属性
turtle.pensize(30)
turtle.pencolor("blue")

# 绘制六边形
for _ in range(6):
    turtle.forward(100)
    turtle.right(60)

# 向右旋转60度
turtle.right(60)

# 记录当前位置为temp
temp = turtle.pos()

# 向前移动2倍六边形边长的距离
turtle.forward(2 * 100)

# 提笔，回到temp位置，落笔
turtle.penup()
turtle.goto(temp)
turtle.pendown()

# 向左旋转35度
turtle.left(35)

# 向右绘制1/4个半圆
turtle.circle(100, 90)

# 提笔，回到temp位置，落笔
turtle.penup()
turtle.goto(temp)
turtle.pendown()

# 向左旋转200度
turtle.left(200)

# 向左绘制1/4个半圆
turtle.circle(-100, 90)

turtle.done()