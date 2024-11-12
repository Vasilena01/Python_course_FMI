# Exceptions context managers
try:
    source_file = open("dani_test.py", 'r')
    buffer = []
    try:
        buffer = source_file.readlines()
    finally:
        source_file.close()
    target_file = open("Homework1.py", 'w')
    try:
        for line in reversed(buffer):
            target_file.write(line)
    finally:
        target_file.close()
except IOError:
 print("Something broke")
finally:
    print("Yayy")

# Decorators
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
    
def translate(language="en"):
    """Translate the output of a function to a specific language."""
    def translate_to(func):
        def decorated(*args, **kwargs):
            output = func(*args, **kwargs)
            return output
        return decorated
    return translate_to

@translate("jp")
def horse(number_of_horses):
    return f"{number_of_horses} horses"

print(horse(5))
to_translate = translate("jp")(horse)(5)
print(to_translate)

def de_cor_ator(fun):
    def clean_fun():
        return fun().replace('text', '***')
    return clean_fun

@de_cor_ator
def student_statement():
    return "Some text!"
print(student_statement())

dec = de_cor_ator(student_statement)
print(dec())

# Classes
class Hand:
    fingers_count = 5
    
    def __setattr__(self, name, value):
        print(f"Нand {name} - {value}")
        object.__setattr__(self, name, value)
        #self.name = value - the '=' calls __setattr__ reqursivly
        
hand = Hand()
hand.pinkie = 'little finger'
setattr(hand, 'new_var', 10)
print(getattr(hand, 'new_var'))

# Other
my_tuple = (1, [1, 2])
#my_tuple[1] += [4] error, because we try to edit the tuple - imutable
my_tuple[1][1] = [4] # correct - we modify only the list which is mutable
print(my_tuple)
