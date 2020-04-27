'''
@Author: Liam
@E-mail: luyu.real@qq.com
@Date: 2020-04-27 22:55:39
@LastEditTime: 2020-04-27 23:26:37
@Software: Visual Studio Code
'''

"""
print("*"*28)
print("*" + " "*26 + "*")
print("*" + " "*10 + "计算器" + " "*10 + "*")
print("*" + " "*2 + "请输入算式按回车键结束" + " "*2 + "*")
print("*" + " "*26 + "*")
print("*"*28)
print()
formula = input("->")
result = eval(formula)
print(formula + "=" + str(result))
"""
import turtle as t 
formula = t.textinput("计算器", "请输入算式")
result = eval(formula)

my_font = ('Arial', 18, 'normal')

t.penup()
t.goto(-200, 100)
t.pendown()
t.write("*"*28, font=my_font)

t.penup()
t.goto(-200, 70)
t.pendown()
t.write("*" + " "*33 + "*", font=my_font)

t.penup()
t.goto(-200, 40)
t.pendown()
t.write("*" + " "*12 + "计算器" + " "*12 + "*", font=my_font)

t.penup()
t.goto(-200, 10)
t.pendown()
t.write("*" + " "*33 + "*", font=my_font)

t.penup()
t.goto(-200, -20)
t.pendown()
t.write("*"*28, font=my_font)

t.penup()
t.goto(-200, -50)
t.pendown()
t.write(formula+"="+str(result), font=my_font)

t.done()

