def div(a, b):
    if a < 0 or b < 0:
        raise Exception('اعداد نمی توانند منفی باشند')
    return a / b


try:
    print(div(100, 0))
except Exception as ex:
    print('خطایی اتفاق افتاده است.', ex)
