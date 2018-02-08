def print_number(num):
    print(" the number is : %d" % num)

list = [1,3,4,5,7,2,6,8,4]

for i in range(10):
    try:
        print_number(list[i])
    except IndexError:
        print("Index Error %d" % i)
