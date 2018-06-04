from aop.aspectAop import InvocationLoggerAspect


@InvocationLoggerAspect
def auth(user, password):
    print("user,passowrd",user+password)
    if user == 'aop' and password == '#$%3&23%#$(%':
        return True
    return False


@InvocationLoggerAspect
def hello(hellostr):
    print(hellostr)
    return hellostr


@InvocationLoggerAspect
def fffffff(hellostr):
    print(hellostr)
    return hellostr

# auth = InvocationLoggerAspect(auth)
# hello = InvocationLoggerAspect(hello)

auth('aop', '#$%3&23%#$(%')
hello("zs")
fffffff("lisi")