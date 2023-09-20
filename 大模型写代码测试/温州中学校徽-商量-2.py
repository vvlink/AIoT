import turtle

# 创建画布和画笔
canvas = turtle.Screen()
pen = turtle.Turtle(shape="square")

# 设置画笔粗细和颜色
pen.width(30)
pen.color("blue")

# 绘制六边形
for i in range(6):
    pen.forward(100)
    pen.right(60)
    
# 保存当前位置
current_pos = (pen.xcor(), pen.ycor())
print("Current position:", current_pos)

# 向右移动
pen.right(90)
distance = 2 * 100 # 假设六边形边长为100
pen.forward(distance)

# 提笔，回到原始位置，落笔
pen.up()
pen.goto(*current_pos)
pen.down()

# 向左旋转35度，向右绘制1/4个半圆
pen.left(35)
radius = distance / 8 # 假设半径为距离的一半
arc_angle = 90 - radius * 2   # 计算弧角度数
pen.circle(-radius, arc_angle + 90)

# 提笔，回到原始位置，落笔
pen.up()
pen.goto(*current_pos)
pen.down()

# 向左旋转200度，向左绘制1/4个半圆
pen.left(200)
pen.setheading(90-arc_angle) # 设置朝向
pen.forward(radius*(math.pi/(180))) # 绘制圆弧

# 隐藏画笔
pen.hideturtle()

# 关闭窗口
canvas.exitonclick()