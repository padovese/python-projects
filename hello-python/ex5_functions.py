def print_two(arg1, arg2):
    print arg1, arg2

def print_many(*args):
    arg1, arg2 = args
    print arg1, arg2

def print_many2(*args):
    for arg in args:
        print arg

def add(arg1, arg2):
    return arg1+arg2

print_two("AAA", "BBB")
print_many("AAA", "BBB")
print_many2("AAA", "BBB")

sum = add(2, 3)
print sum