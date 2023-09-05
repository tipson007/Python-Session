temps = [34, 555,  56, 77, 888]

new_temps = [temp / 10 for  temp in temps]

print(new_temps)


def foo(lst):
    return [i for i in lst if  isinstance(i, int)]


def foo(lst):
    return [i for i in lst if i > 0 ]