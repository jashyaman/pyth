#partial functions
#partial functions are used in the case
# where one function's funcationality can be used as part of a larger functions
#multiply function multiplies 2 numbers, taking 2 arguments
#double function is defined to use multiply function as a partial function and 2
# as input
#double function takes one input and multiplies it by two and returns the output

from functools import partial

def multiply(a,b):
    return a * b

duble = partial(multiply,2)

print(duble(4))

def concat(str2, str1):
    return str1 + " " + str2

copyrightText = "copyright Shyam Mohan Raman. All Rights Reserved."
appendCopyright = partial(concat,copyrightText)


text = "DCUPay is a new mobile app that lets you find great food near you, browse menus, order ahead, and pay quickly using just your phone and your linked DCU Credit or Debit card."
print(appendCopyright(text))

#noticed that partial(concat, copyrightText) < in this statement, copyrightText
#appears in the place of str1 in concat.

#Following is the exercise, function provided:
from functools import partial
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function

funcp = partial(func,10,6,1)

print(funcp(0))

#only last argument can be made partial.
#not however in the case of line 18,19,22.
