from for_debuger import another_func


def my_func(a, b, c):
    print('Want to divide!')
    c *= 100
    another_func()
    a *= c
    another_func()
    return a / b


print('abc')
d = 3
print(my_func(1, 1, 1))
m = 4
l = [1, 2, 3, 4, 5]
another_func()
print('end')