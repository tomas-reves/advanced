def laikrodis(val):
    count = 1
    while count <= val:
        yield count
        count +=1


clock = laikrodis(12)

while True:
    try:
        print(next(clock))
        print(next(clock))
        print(next(clock))
        print(next(clock))
        print(next(clock))
        print(next(clock))
        print(next(clock))
        print(next(clock))
        print(next(clock))
        print(next(clock))
        print(next(clock))
        print(next(clock))
        print(next(clock))
        print(next(clock))
    except StopIteration:
        clock = laikrodis(12)





