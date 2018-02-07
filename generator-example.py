import random

dict = {}
dict["lottery2"] = 0;
dict["forloop"] = 0;

def lottery2():
    for i in range(6):
        dict["lottery2"]+= 1;
        yield random.randint(1,40)

    yield random.randint(1,15)

count = 0;
for random_number in lottery2():
    dict["forloop"]+= 1;
    print(random_number)

print (dict["lottery2"])
print (dict["forloop"])
