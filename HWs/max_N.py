


def max_of_3(a:int, b:int, c:int):
    max = 0
    if a >= b:
        max = a
        if a >= c:
            max = a
        else:
            max = c
    else:
        max = b
        if b >= c:
            max = b
        else:
            max = c
    print(max)

max_of_3(2, 2, 22)