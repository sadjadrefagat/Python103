def myfun1():
    pass
    
    

langs = [
    ('Python', 20, 8),
    ('C++', 10, 20),
    ('C#', 70, 15),
    ('Javascript', 60, 4),
]

x = sorted(langs)
print(x)

pass

y = sorted(langs, key=lambda i: i[1], reverse=True)
print(y)
