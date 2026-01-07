print("STUDENT GRADE MANAGEMENT")

students = ["SM","PT","KV","MT","DN"]
grades = [[("MAD",75),("DSA",80),("ITP",60)], [("MAD",60),("DSA",70),("ITP",55)], [("MAD",75),("DSA",75),("ITP",60)], [("MAD",60),("DSA",65),("ITP",55)], [("MAD",70),("DSA",75),("ITP",55)]]
courses = {"MAD", "DSA", "ITP"}

while True:
    print("\n******* MAIN MENU *******")
    print("01. Add Student")
    print("02. Add Grades")
    print("03. View All Students")
    print("04. Calculate Averages")
    print("05. Find Top Performer")
    print("06. Sort By Average")
    print("07. View All Courses")
    print("08. Exit")

    option = int(input("\nEnter Your Option (1-8): "))

    if option == 1:
        sname = input("Enter Student Name : ")
        if sname in students:
            print("Student Name Already In The List")
        elif sname.strip() == "":
            print("Student Name Should Not Be Empty")
        else:
            students.append(sname)
            grades.append([])
            print(f"Student {sname} Added Successfully")

    elif option == 2:
        if len(students) == 0:
            print("Error: No Students In The List")
        else:
            print("\nAvailable Students : ")
            for i, name in enumerate(students,1):
                print(f"{i}. {name}")
            
            enumber = int(input("Enter Student Number : "))

            index = enumber - 1

            if index < 0 or index >= len(students):
                print("Invalid Student Number")
            else:
                cname = input("Course Name : ")
                cgrade = int(input("Course Grade : "))
                if cgrade >= 0 and cgrade <= 100:
                    grades[index].append((cname,cgrade))
                    courses.add(cname)
                    print("Course & Grade Added Successfully")
                else:
                    print("Enter Valid Grade")
                    cgrade = int(input("Course Grade : "))
                
    elif option == 3:
        if len(students) == 0:
            print("Error: No Students In The List")
        else:
            print("ALL STUDENTS")
            for i, name in enumerate(students, 1):
                print(f"{i}. {name}")
                if grades[i-1]:
                    print("Grades:", end=" ")
                    for course, grade in grades[i-1]:
                        print(f"{course}:{grade}", end=" | ")
                    print()
                else: 
                    print("No Grades Yet")

            
    elif option == 4:
        if len(students) == 0:
            print("Error: No Students In The List")
        else:
            print("STUDENT AVERAGES")
            for i, sname in enumerate(students,1):
                if grades[i-1]:
                    gradenumbers = [grade for course, grade in grades[i-1]]
                    average = sum(gradenumbers) / len(grades[i-1])
                    print(f"{sname} : {average:.2f}%")
                else:
                    print(f"{sname} : No Grades")
                
    elif option == 5:
        topstudent = "None"
        topaverage = -1

        for i, sname in enumerate(students,1):
            if grades[i-1]:
                gradenumbers = [grade for course, grade in grades[i-1]]
                average = sum(gradenumbers) / len(grades[i-1])
                if average > topaverage:
                    topaverage = average
                    topstudent = sname
                
        if topstudent != "None":
            print(f"Top Student : {topstudent} Average : {topaverage:.2f}")
        else:
            print("No Students With Grades")

    elif option == 6:
        has_any_grades = False
        for grade_list in grades:
            if grade_list:
                has_any_grades = True
                break
    
        if not has_any_grades:
            print("No students have grades!")
        else:
            print("STUDENTS SORTED BY AVERAGE")
        
        student_data = []
        
        for i, name in enumerate(students):
            if grades[i]:
                grade_numbers = [grade for course, grade in grades[i]]
                average = sum(grade_numbers) / len(grades[i])
                student_data.append((average, name))
            else:
                student_data.append((0, name))

        student_data.sort(reverse=True)

        for rank, (average, name) in enumerate(student_data, 1):
            if average > 0:
                print(f"{rank}. {name} - {average:.2f}%")
            else:
                print(f"{rank}. {name} - No grades")

    elif option == 7:
        if len(courses) == 0:
            print("Error: Courses Is Empty")
        else:
            print("ALL COURSES")
            sorted_courses = sorted(courses)
            for course in sorted_courses:
                print(f"⚫ {course}")

    elif option == 8:
        print("Thankyou For Visiting")
        break
    
    else:
        print("Your Option Is Wrong")
