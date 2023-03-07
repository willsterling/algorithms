def sum_1_to_n(n: int):
    a = 0
    if n == 0:
       a = 1
    elif n == 1:  #may not need this elif statement
       a = 0
    elif n > 1:
        for i in range(1, n+1):
            a += i
    else:
        for i in range(n, 2):
            a += i
    print(f'The sum of integers from 1 to n is {a}')


n = int(input("Enter an integer 'n':"))
sum_1_to_n(n)
