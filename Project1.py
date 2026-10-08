Bacche = []

def add_student():
    Name = input("Enter name: ")
    RollNo = int(input("Enter Roll No: "))
    Marks = float(input("Enter Marks: "))

    student = {
        "Name": Name,
        "RollNo": RollNo,
        "Marks": Marks
    }

    Bacche.append(student)
    print("Student added")


def calculate_res():
    for B in Bacche:

        if B["Marks"] >= 85:
            print("Grade A")

        elif B["Marks"] >= 75:
            print("Grade B")

        elif B["Marks"] >= 50:
            print("Grade C")

        else:
            print("Fail")


def view_student():
    for B in Bacche:
        print("Name:", B["Name"])
        print("Roll No:", B["RollNo"])
        print("Marks:", B["Marks"])


def main():
    while True:

        print("\n1. Add Student")
        print("2. View Student")
        print("3. Calculate Result")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_student()

        elif choice == "3":
            calculate_res()

        elif choice == "4":
            print("Thank you for using Student Analyzer!")
            break

        else:
            print("Invalid choice. Try again.")


main()
