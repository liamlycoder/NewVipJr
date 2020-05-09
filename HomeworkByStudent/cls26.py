yong_hu_ming = input("用户名：")
with open("database.txt", "r") as f:
    rec = f.readlines()
    for i in range(len(rec)):
        if i % 2 == 0 and rec[i].strip("\n") == yong_hu_ming:
            mi_ma = input("密码：")
            if rec[i + 1].strip("\n") == mi_ma:
                print("登陆成功！")
            else:
                print("密码错误！")
            break
    else:
        print("该用户未注册！")
"""
这里我不知道为什么他会报错，UnicodeDecodeError: 'gbk' codec can't decode byte 0xac in position 2: illegal multibyte sequence
"""