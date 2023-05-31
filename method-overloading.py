def add(*args):
    if (len(args) == 2): return args[0] + args[1]
    result = 0
    for x in args:
        result += x

    return result

print(add(1,2))
print(add(1,2, 3,4,5))