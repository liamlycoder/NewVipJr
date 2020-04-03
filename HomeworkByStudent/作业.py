password = input('password:')
with open ('作业附件.txt') as f:
    rs = f.readlines()
    for i in range ():
        if i%2 == 0 and rs[i]
            if rs[i+1]
                print('登录成功')
            else:
                print('密码错误')
            break
    else:
        print('用户未注册')