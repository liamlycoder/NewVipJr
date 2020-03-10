lst = ("yellow","red","purple","pink","blue")
lst2 = ("黄色","红色","紫色","粉色","蓝色")
print("*"*200)
x = 0
for i,j in zip(lst,lst2):
    print(lst[i]+"是什么意思？")
    a = input("请输入答案：")
    print("*"*200)
    if a == lst2[i]:
        print("恭喜，答对了！！！")
        x += 20
    else:
        print("糟糕，答错了！！！答案是{}".format(lst2[i]))
print("你的得分是{}分".format(x))




