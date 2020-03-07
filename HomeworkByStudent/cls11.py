lst = ["yellow","red","purple","pink","blue"]
lst2 = ["黄色","红色","紫色","粉色","蓝色"]
print("*"*200)
for i in range(len(lst)):
    print(lst[i]+"是什么意思？")
    a = input("请输入答案：")
    print("*"*200)
    if a == lst2[i]:
        print("恭喜，答对了！！！")
    else:
        print("糟糕，答错了！！！答案是{}".format(lst2[i]))
print("恭喜你，你得了{}分".format())

#不好意思，我想不出来如何计分数，只能将对错分辨出来。
