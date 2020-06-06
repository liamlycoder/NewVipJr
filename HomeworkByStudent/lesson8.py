from turtle import *
x = textinput("灯的状态","开请按'on',关请按'off'")
open = "on"
if x == open:
              begin_fill()
              color("yellow","yellow")
              circle(20)
              end_fill()
else:
    begin_fill()
    color("black","black")
    circle(20)
    end_fill()
              
