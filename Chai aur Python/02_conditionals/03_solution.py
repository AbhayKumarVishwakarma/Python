# Problem: Assign a letter grade based on a student's 
# score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = int(input("Enter score: "))
grade = ""

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")


