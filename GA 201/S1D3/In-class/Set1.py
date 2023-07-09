# Hello, World!: Write a Python program that prints "Hello, World!" to the console.
print("Hello, World!")
print()

# Data Type Play: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
a = 10
b = 5.4
c = "Python"
d = True
e = [1, 2, 3, 4, 5]
f = (1, 2)
g = {"name": "Thor", "age": 1500}
h = {1, 2, 3, 4}

print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)
print(type(f), f)
print(type(g), g)
print(type(h), h)
print()

# List Operations: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.

list = [1, 6, 7, 8, 10, 2, 3, 4, 5, 9]

list.append(15)  # Adding the value 15
print(list)

list.remove(6)  # Removing the value 6
print(list)

list.sort()     # Sorting the list
print(list)
print()

# Sum and Average: Write a Python program that calculates and prints the sum and average of a list of numbers.
list = [10, 20, 30, 40]

sum = 0
avg = 0
for i in list:
    sum += i

avg = sum / len(list)
print("Sum:", sum)       # Printing sum of list
print("Average:", avg)  # Printing average of list
print()

# String Reversal: Write a Python function that takes a string and returns the string in reverse order.
def reverseString(str):
    ans = ""
    for i in str:
        ans = i + ans
    return ans

str = "Python"
x = reverseString(str)
print(str,x)
print()


# Count Vowels: Write a Python program that counts the number of vowels in a given string
str = "Hello"
vowel = 0

for i in str:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowel += 1

print(vowel)
print()


# Prime Number: Write a Python function that checks whether a given number is a prime number.
def checkPrime(num):
    if num == 1:
        print(num, "is not prime number")
    elif num > 1:
        flag = True
        for i in range(2, num):
            if (num % i) == 0 :
                flag = False
                break
        
        if flag: print(num, "is prime number")
        else: print(num, "is not prime number")

checkPrime(13)
checkPrime(10)
print()


# Factorial Calculation: Write a Python function that calculates the factorial of a number.
def factorial(num):
    if num == 1: 
        return 1
    else:
        return num * factorial(num -1)

print(factorial(5))
print()


# Fibonacci Sequence: Write a Python function that generates the first n numbers in the Fibonacci sequence.
def fibonacci(num):
    arr = [0,1]
    i = 2
    while i < num:
        arr.append(arr[i-1] + arr[i-2])
        i += 1
    return arr

print(fibonacci(10))
print()


# List Comprehension: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
list = [i**2 for i in range(1,11)]
print(list)
