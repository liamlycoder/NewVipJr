import os

os.chdir("yy")
x = os.listdir(os.getcwd())
for i in x:
    if os.path.isfile(i):
        print(i + "是文件。")
    if os.path.isdir(i):
        print(i + "是文件夹。")

# 这里我在磁盘中储存了“yy”这个文件夹，但他还是显示未找到指定的文件。
