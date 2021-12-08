class SomeClass:
 def __init__(self):
     print(' SomeClass obj was created')
 def someMethod(self, a):
     print('The value of a is', a)
     self.a = a
     return self.a
class SomeOtherClass:
 def __init__(self):
     print('This is SomeOtherClass')


def Somefunc(var):
    print('some func is being implemented!')
    var+=4
    return var

