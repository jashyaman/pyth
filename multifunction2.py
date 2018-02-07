def sum (a, b):
    return (a+b)


def anyfunction(**args):
    print(type(args))
    val1 = args.get("x")
    print(type(val1))
    val2 = args.get("y")
    result = args.get("fn");
    print(type(result))
    ans = result(val1,val2)
    print(type(ans))
    print(ans)

    #lots of questions answered
    #arguments by keyword can replace positional arguments
    #arguments can be functions

    



anyfunction(x = 12,y = 23,z = [1,2,3], fn = sum)
