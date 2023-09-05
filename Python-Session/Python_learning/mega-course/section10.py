def mean(*args):
    return args
#get back a tupule as an output
print(mean(1,  3, 'a', 4))

def foo(*args):
    args = [str.upper() for str in args]
    return sorted(args)

print( "snow""zaeland" "glacier" "lake")

#keyword argument
def find_sum(**kwargs):
    return sum(kwargs.values())

print(find_sum(x=1, y=2, z=6))