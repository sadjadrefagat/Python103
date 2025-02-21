a = 2
b = a
c = 0


def func1():
    global c
    c += 1
    return True


if a == b or func1():
    print(c)

if c == 0:
    func1()
    print(c)
elif func1() and c == 2:
    print(c+1)
