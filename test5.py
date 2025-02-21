a = 5

def func1():
    a = 7
    
    def func2():
        nonlocal a
        a = 8

    func2()
    print(a)
    
func1()
print(a)
