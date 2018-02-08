def printNnumbers(n):
  i = 0
  if i <= n:
    i+=1
    yield i


n = 10
while(True):
    i = printNnumbers(n);

    print("%d 'th iteration :" % i)

    # unable to figure out how to extract values from yield statement
    # of 
