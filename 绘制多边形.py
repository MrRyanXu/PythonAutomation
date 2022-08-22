'''
绘制自定义多边形
输入边数，绘制相应多边形
如果输入边数小于3，输出提示信息
'''
import turtle
# 边数
n = int(input('请输入多边形的边数：'))
# 角度
d = int(360/n)
if n >= 3:
    for i in range(n):
        turtle.forward(100)
        turtle.right(d)
    turtle.done()
else:
    print('边数小于3，请输入大于等于3的整数！')