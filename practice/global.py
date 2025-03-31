a = 78

def func():
    global a
    a = 4
    print(a)

func()
print(a)