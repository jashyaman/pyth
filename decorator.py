'''
decorators
are declarative constructs that can be used to add more functionality to existing
functions - such as repeat the operation twice, return a different data type etc.
'''
def repeater(func):
    def repeatTwice(*args,**kwids):
        val1 = func(*args,**kwids)
        val2 = func(*args,**kwids)
        return func(val1,val2)
    return repeatTwice

@repeater
def addTwo(a,b):
    return a + b


print(addTwo(10,23))

def addCopyright(func):
    def appendCopyright(*args,**kwids):
        val1 = func(*args,**kwids)

        return val1+"\ncopyright message"
    return appendCopyright


@addCopyright
def concatTwo(st1,st2):
    return (st1 + st2)

print(concatTwo("marco", " polo "))
