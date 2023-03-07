


def factorial(number: int):
    result = 1
    for i in range(2, number +1):
        print(f'Step{i}') # proof our time complexity is O(n)
        result = result * i   # we can also use python operand *= -> ex: result *= i
    print(f'factorial of {number} is {result}')


factorial(5)

# Q: What is the time complexity of this solution?
# A: It is O(n) - the number of steps is equal to the value of the input