# 1. **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
input = [("John", 25), ("Jane", 30)]
for name, age in input:
    print(f"{name} is {age} years old.")

print()



# 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
    # - *Input*: Add "John": 25, Update "John": 26, Delete "John"
    # - *Output*: "{}, {'John': 26}, {}"
dict = {}
dict["John"] = 25
print(dict)

dict.update({"John": 26})
print(dict)

del dict["John"]
print(dict)
print()



# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
    # - *Input*: [2, 7, 11, 15], target = 9
    # - *Output*: "[0, 1]"

def findTwoInt(arr,k):
    i = 0
    while i < len(arr):
        j = 0
        while j < len(arr):
            if (i != j) and (arr[i] + arr[j] == k):
                return [i,j]
            j += 1
    i += 1

arr = [2, 7, 11, 15]
k = 9
print(findTwoInt(arr,k))
print()



# Palindrome Check: Write a Python function that checks whether a given word or phrase is a palindrome.
def checkPalindrome(str):
    s = 0
    e = len(str) - 1
    while s < e :
        if str[s] != str[e] :
            return False
        s += 1
        e -= 1

    return True

str = "madam"
print(checkPalindrome(str))
print()



# Selection Sort: Implement the selection sort algorithm in Python.
arr = [64, 25, 12, 22, 11]
print(arr)

i = 0
while i < len(arr):
    x = i
    j = i
    while j < len(arr):
        if arr[x] > arr[j]:
            x = j
        j += 1
    temp = arr[x]
    arr[x] = arr[i]
    arr[i] = temp
    i += 1

print(arr)
print()



# Implement Stack using Queue: Use Python's queue data structure to implement a stack.





# 1. **FizzBuzz**: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz", end=" ")
    elif i%3 == 0:
        print("Fizz", end=" ")
    elif i%5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")

print()
print()



# File I/O: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
def file():--
    input = open("input.txt","r")
    content = input.read()
    count = len(content.split())
    print(f"count: {count}")
    output = open("output.txt","w")
    output.write(f"{count}")


file()
print()



# Exception Handling: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
def funWithException(a,b):
    try:
        ans = a/b
    except ZeroDivisionError:
        print("can't divid with zero!")
    else:
        print(ans)

funWithException(10,10)



