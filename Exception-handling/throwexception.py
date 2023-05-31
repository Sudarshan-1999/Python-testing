def throw_exception(num):
    if (num == 0): raise Exception("Argument 0 is not accepted.")
    else: print(num)
try:
    throw_exception(0)
except Exception as ex:
    print(ex)
else:
    print("Exception not thrown")
finally:

    print("Done")