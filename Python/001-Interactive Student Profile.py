#Basic Student Profile Project

#Collect Information

print("Welcome To Student Profile\n")

name = input("Enter your name : ")
age = input("Enter your age : ")
gpa = input("Enter your GPA : ")
field = input("Enter your study field : ")
courses = input(("How many courses completed in this semester : "))
graduationYear = int(input("Your Graduation Year : "))

#Process The Data

int_age = int(age)
float_gpa = float(gpa)
int_courses = int(courses)

int_age += 1
predicted_gpa = float_gpa + 0.5
avgCourses = int_courses/2

#Display Profile

print("=" * 50)
print("YOUR STUDENT PROFILE")

print(f"Name : {name}")
print(f"Age : {age}")
print(f"Field : {field}")
print(f"GPA : {float_gpa:.2f}")
print(f"Courses : {int_courses}") 
print(f"Graduation year : {graduationYear}") 
print("=" * 50)

#Display Predication

print("\n")

print("=" * 50)
print("NEXT YEAR PROJECTIONS")

print(f"Age Next Year : {int_age}")
print(f"Potential GPA : {predicted_gpa:.2f}")
print(f"Average Courses Per Semester : {avgCourses:.1f}")
print("=" * 50)

#Data Types 
print("\n")

print("=" * 50)
print("DATA TYPES")
print(f"Type Of Name : {type(name)}")
print(f"Type Of Age : {type(age)}")
print(f"Type Of Converted Age : {type(int_age)}")
print(f"Type Of Converted GPA : {type(float_gpa)}")
print(f"Type Of Study Field : {type(field)}")
print(f"Type Of Courses Count : {type(courses)}")
print(f"Type Of Graduation Year : {type(graduationYear)}")
print("=" * 50)

print("\n")

print("=" * 50)
if float_gpa > 3.5:
    print("Excellent work, Keep it up!!")
elif float_gpa > 3.0:
    print("Good Work, Keep It Up!!")
else:
    print("You Need Improvement")

print("Student Profile Completed Successfully")
print("=" * 50)
