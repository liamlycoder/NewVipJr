a = []


def count(x, y, n="+"):
    if n == "+":
        b = int(x + y)
        a.append(b)
    if n == "-":
        c = int(x - y)
        a.append(c)
    if n == "*":
        d = int(x * y)
        a.append(d)
    if n == "/":
        e = int(x / y)
        a.append(e)


count(5, 6, "+")
print(a)
