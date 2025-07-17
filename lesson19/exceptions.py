class JustNotCollError(Exception):
    pass


x=2
try:
    raise JustNotCollError("This just isn't cool.")
    #raise Exception("I'm a custom exception")
    #print (x/0)
    # if not type(x) is str:
    #     raise TypeError("Only Strings are allowed")
except NameError:
    print('NameError means something is undefined')

except ZeroDivisionError:
    print('Divide by zero error')
except Exception as error:
    print(error)
else:
    print('no errors')
    
finally:
    print("I'm going to print no matter what")

