name = input("Enter your Name: ")
age = input("Enter your Age: ")
sub_1 = int(input("Enter Marks in Subject 1: " ))
sub_2 = int(input("Enter Marks in Subject 2: " ))
sub_3 = int(input("Enter Marks in Subject 3: " ))

total_marks = (sub_1 + sub_2 + sub_3)
avg_marks = (total_marks / 3)

print("Name : " , name)
print("Age :" , age)
print("Toral Marks :" , total_marks)
print("Average Marks :" , avg_marks)

if avg_marks >= 40 :
    print("PASS")
else:
    print("FAIL")