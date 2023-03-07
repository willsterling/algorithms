

# an example of how floor division works -> returns only the whole number
a = 125 / 10   # will give 12.5
b = 125 // 10  # should give 12


def sum_of_three(n:int):
    result = 0
    original_n = n
    while n != 0:
        print("STEP") # this line is just a counter
        result = result + (n % 10)
        n = n // 10

    print(f'sum of all the digits in {original_n} is {result}')

test = 125

sum_of_three(test)

# Q: What is the time complexity of this solution?
# A: It is O(1) if we are alwyays usuing a 3-digit number; it is O(n) if n may change  - there are still just 3 steps