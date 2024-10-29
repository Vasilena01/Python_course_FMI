def outer(x):
    print(x)
    def inner():
        x = 0
        print(x)
    inner()
    print(x)
#outer(2); #2, 0, 2

def start(x):
    def increment(y):
        return x + y
    return increment
#Equal calls
#print(start(0)(3))
#func = start(0)
#print(func(3))

def notifyme(f):
    def logged(*args, **kwargs):
        print(f.__name__, ' called with ', args, ' and ', kwargs)
        return f(*args, **kwargs)
    return logged

@notifyme
def square(x):
    return x * x
result = square(25) 
print(result)

# Something like this is equal to the above
result = notifyme(square(25))
print(result)
    
def served_by(server):
    def decorator(func):
        def cached_server(n):
            print("{}, dear {}".format(func(n), server))
        return cached_server
    return decorator

def thank_you(func):
    def with_thanks(n):
        print("{}. Thank you very much!".format(func(n)))
    return with_thanks

@served_by("sir")
def spam(n):
    spams = ("spam", ) * (n - 1)
    print("I would like {} and spam".format(", ".join(spams)))

@thank_you
@served_by("sir")
def eggs(n):
    print("I would like {} eggs".format(n))