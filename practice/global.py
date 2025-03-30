a = 78

def fun():
    global a
    a = 4
    print(a)

fun()
print(a)