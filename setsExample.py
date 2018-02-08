#sets
def setFunc():
    a = set(["Jake", "John", "Eric"])
    b = set(["John", "Jill"])

    print (a)
    print (b)
    print("intersection")
    print(a.intersection(b))
    print(b.intersection(a))
    print("symmetric_difference")
    print(a.symmetric_difference(b))
    print(b.symmetric_difference(a))
    # symmetric difference is similar to AvB U BvA
    print("difference")
    print(a.difference(b))
    print(b.difference(a))
    print("union")
    print(a.union(b))

setFunc()
