# 1
# 2
# Fizz
# 4
# Buzz
# ...
# 14
# FizzBuzz


#code here

a = 4 % 2
b = 5 % 2 # modular division gives the remainder of the division so this b = 1
print(a)
print(b)

# We also need to usea for loop and range


def fizzbuzz(n:int):
    for i in range(1, n + 1): #note that for range, range will not include the very last number so we must add +1 to our desired range to get it
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz") # note that if i = 15, we only print "Fizz" b/c once the first conition of the if statment is satisfied, we exit the loop
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz(15)
# What is the time complexity of this?
# A: O(n) -> the number of steps executed is equal/proportional to the value of the input