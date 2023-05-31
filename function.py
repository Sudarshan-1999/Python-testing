def downloadFile(url):
    print(url)
    print("Open Connection ", url)
    print("Download Data ")
    print("Close Connection ", url)

downloadFile("https://lms.intellipaat.com/")


def multiply(x, y):
    return x * y

print(multiply(20, 12) , '\n\n')

def createMultiply(x):
    return lambda y : x * y

multiply1 = createMultiply(10)



def execute(f, args):
    print("Called F with " , str(args))
    return f(args)


print(execute(multiply1, 15))
print(execute(multiply1, 25))