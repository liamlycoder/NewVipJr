word = {"yellow": "黄色", "red": "红色", "purple": "紫色", "pink": "粉色", "blue": "蓝色"}
cuotiben = {}
b = 0
for i, j in word.items():
    print(i + '是什么意思？')
    a = input("请回答：")
    if a == j:
        print('恭喜，答对了！！！')
        b += 20
        print('*' * 200)
    else:
        print("糟糕，答错了!!!")
        cuotiben[i] = j
        print('*' * 200)
print('你的得分为{}分'.format(b))
print('*'*200)
print('你的错题是{}'.format(cuotiben))

print("开始订正：")
words = (cuotiben)
for p, r in word.items():
    print(p + '是什么意思？')
    a = input("请回答：")
    if a == r:
        print('恭喜，答对了！！！')
        print('*' * 200)
    else:
        print("糟糕，答错了!!!")
        print('*' * 200)
print('订正完毕。')
