def func1(a, b):
    if a < 0 or b < 0:
        raise Exception('Negative numbers not allowed.')
    return a / b


try:
    print(func1(100, 0))
except Exception as ex:
    print("Error: ", ex)