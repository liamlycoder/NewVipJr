import os

os.chdir(r"yy")
result = os.listdir(os.getcwd())
for i in result:
    if os.path.isfile(i):
        os.rename(i, "news_" + i)
