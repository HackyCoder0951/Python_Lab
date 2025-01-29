def student_biodata():
    global std_name, std_class, std_section
    std_name = input("Enter your name: ")
    std_class = input("Enter your class: ")
    std_section = input("Enter your section: ")
    student_mark()

def student_mark():
    global eng, math, science, hindi, std_per, std_remark
    try:
        eng = int(input("Enter English Marks: "))
        math = int(input("Enter Math Marks: "))
        science = int(input("Enter Science Marks: "))
        hindi = int(input("Enter Hindi Marks: "))
    except:
        print("\nPlease Enter Numeric Marks.\n")
        student_mark()  # Retry on invalid input
        return
    else:
        if eng > 100 or math > 100 or science > 100 or hindi > 100 :
            print("Error : Check the mark entry!\n")
            student_mark()  # Retry on invalid marks
        else:
            std_per = (eng + math + science + hindi) / 4
            if 0 < std_per < 45 :
                std_remark = "Failure"
            else :
                std_remark = "PASS"
            student_result()

def student_result():
    print("\nStudent Result")
    print("Student Name      :", std_name)
    print("Student Class     :", std_class)
    print("Student Section   :", std_section)
    print("Student Percentage:", f"{std_per:.2f}%")
    print("Student Remark    :", std_remark, "\n")

if __name__ == "__main__":
    print("Student Results")
    student_biodata()
