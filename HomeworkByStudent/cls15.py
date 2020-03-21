import random
a = []
def ABC(n):
    for i in range(n):
        x = random.randint(1,20)
        a.append(x)
ABC(10)
print(a)
