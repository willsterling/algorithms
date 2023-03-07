
a = input('Input a number:\n ')
i = 0
even_count = 0
odd_count = 0
while i < len(a):
    par = int(a[i])
    integer = int(par)
    if integer % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    i += 1
print(f'The number of even integers in {a} is {even_count} \nThe number of odd integers in {a} is {odd_count}')
