
a = 10
b = 20

if a == b:   # (Condition)  Brackets are optional
    print("True")
else:
    print("False")


marks = 78

if (marks > 80):
    print("Grade A")
elif (marks < 80 and marks > 60):
    print("Grade B")
elif marks < 60 and marks > 40:
    print("Grade C")
else:
    print("Grade D")

if a >= 20:
    print("O. if C. is True")
else:
    if a>=11:
        print("Nested if C. Is True")
    else:
        print("All C. Are False")