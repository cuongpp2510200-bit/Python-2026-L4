students = []   
courses = []   
marks = {}      

def input_number_of_students():
    count = int(input("Enter number of students in class: "))
    return count

def input_students_info():
    num_students = input_number_of_students()
    for i in range(num_students):
        print(f"\n-Enter information for student #{i+1}")
        std_id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of Birth : ")
        students.append({
            'id': std_id,
            'name': name,
            'dob': dob
        })

def input_number_of_courses():
    count = int(input("\nEnter number of courses: "))
    return count

def input_courses_info():
    num_courses = input_number_of_courses()
    for i in range(num_courses):
        print(f"\nEnter information for course #{i+1}")
        course_id = input("Course ID: ")
        name = input("Course Name: ")
        courses.append({
            'id': course_id,
            'name': name
        })

def input_marks_for_course():
    if not courses:
        print("\nERROR! No courses available")
        return
    if not students:
        print("\nERROR! No students available")
        return
    print("\nAvailable Courses")
    list_courses()
    course_id = input("Select a course ID to input marks: ")
    course_exists = any(c['id'] == course_id for c in courses)
    if not course_exists:
        print("\nERROR! No course found")
        return
    if course_id not in marks:
        marks[course_id] = {}
    print(f"\nInputting marks for course {course_id}")
    for std in students:
        mark = float(input(f"Enter mark for Student {std['name']} (ID: {std['id']}): "))
        marks[course_id][std['id']] = mark

def list_courses():
    if not courses:
        print("\nCourse list is empty.")
        return
    print("\nCOURSE LIST")
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")

def list_students():
    if not students:
        print("\nStudent list is empty.")
        return
    print("\nSTUDENT LIST")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def show_student_marks():
    if not marks:
        print("\nNo marks have been recorded yet!")
        return
    course_id = input("\nEnter Course ID to view marks: ")
    if course_id not in marks:
        print("\nERROR! No mark")
        return
    print(f"\nMARKS FOR COURSE {course_id}")
    for std in students:
        std_id = std['id']
        if std_id in marks[course_id]:
            print(f"ID: {std_id} | Name: {std['name']} | Mark: {marks[course_id][std_id]}")
        else:
            print(f"ID: {std_id} | Name: {std['name']} | Mark: Not entered")

def main():
    while True:
        print("\nSTUDENT MARK MANAGEMENT: ")
        print("1. Input student information")
        print("2. Input course information")
        print("3. Select course and input marks for students")
        print("4. List courses")
        print("5. List students")
        print("6. Show student marks for a given course")
        print("7. Exit program")  
        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            input_students_info()
        elif choice == '2':
            input_courses_info()
        elif choice == '3':
            input_marks_for_course()
        elif choice == '4':
            list_courses()
        elif choice == '5':
            list_students()
        elif choice == '6':
            show_student_marks()
        elif choice == '7':
            print("\nExiting program")
            break
        else:
            print("\nInvalid choice")

if __name__ == "__main__":
    main()