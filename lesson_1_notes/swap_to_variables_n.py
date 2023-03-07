

def swap_variables(a:int, b:int):
    print(f'Before swap a= {a}, b = {b}') #we expect to see a = 5, b = 10
    temp = a
    a = b
    b = temp
    print(f' After swap: a= {a}, b= {b}')

test_a = 5
test_b = 10
swap_variables(test_a, test_b)


# Q: What is the time complexity of this solution?
# A: It has a time plexity of O(1) because we always solve it in a constant number of steps, 3 steps

#What if we cannot use a variable "temp"?
def swap_variables_second(a:int, b:int):
    print(f'Before swap a= {a}, b = {b}') #we expect to see a = 5, b = 10
    a = a + b
    b = a - b
    a = a - b
    print(f' After swap: a= {a}, b= {b}')

test_a = 5
test_b = 10
swap_variables_second(test_a, test_b)


# Q: What is the time complexity of this solution?
# A: It i still O(1) - there are still just 3 steps

def swap_variables_third(a: int, b: int):
    print(f'Before swap a= {a}, b = {b}') #we expect to see a = 5, b = 10
    a, b = b, a #this is a python specific solution
    print(f' After swap: a= {a}, b= {b}') #we expect to see b = 5,  a = 10

test_a = 5
test_b = 10
swap_variables_third(test_a, test_b)