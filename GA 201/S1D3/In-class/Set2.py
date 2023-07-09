# Problem 1: Print the pattern
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

print()


# Problem 2: Display numbers from a list using loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    if i % 5 == 0:
        print(i)
print()



# Problem 3: Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"

mid = len(s1) // 2
s3 = s1[:mid] + s2 + s1[mid:]
print(s3)
print()


# Problem 4: Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"
lower = ""
upper = ""

for i in str1:
    if i.islower():
        lower += i
    else:
        upper += i

print(lower + upper)
print()


# Problem 5: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# list = []
# for i in range(len(list1)):
#     list.append(list1[i] + list2[i])
list = [i+j for i,j in zip(list1, list2)]

print(list)
print()



# Problem 6: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list = []
for i in list1:
    for j in list2:
        list.append(i + j)

print(list)
print()



# Problem 8: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

obj = {i: defaults for i in employees}
print(obj)
print()



# Problem 9: Create a dictionary by extracting the keys from a given dictionary
dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]


ans = {i:dict[i] for i in keys}
print(ans)
print()


# Problem 10: Modify the tuple
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)