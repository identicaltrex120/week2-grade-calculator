# Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures
# Name: Krish Sunil
# Description: Calculates grades for multiple students, assigns grades with comments,
# stores results using lists, displays statistics, allows searching and saving results.

def calculate_grade(average):
    """Calculate grade based on average marks"""
    if average >= 90:
        return 'A', 'Excellent! Keep up the great work!'
    elif average >= 80:
        return 'B', 'Very Good! You\'re doing well.'
    elif average >= 70:
        return 'C', 'Good. Room for improvement.'
    elif average >= 60:
        return 'D', 'Needs Improvement. Please study more.'
    else:
        return 'F', 'Failed. Please seek help from teacher.'

def get_valid_number(prompt, min_val=0, max_val=100):
    """Get a valid number within specified range"""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input! Please enter a number.")

def display_results(student_names, student_results):
    print("\n" + "=" * 50)
    print("            RESULTS SUMMARY")
    print("=" * 50)
    print(f"{'Name':<20} | {'Avg':>5} | {'Grade':^5} | Comment")
    print("-" * 60)

    for i in range(len(student_names)):
        name = student_names[i]
        avg = student_results[i]['average']
        grade = student_results[i]['grade']
        comment = student_results[i]['comment']

        # color coding
        if grade == 'A':
            color = "\033[92m"
        elif grade == 'B':
            color = "\033[94m"
        elif grade == 'C':
            color = "\033[93m"
        else:
            color = "\033[91m"

        reset = "\033[0m"

        print(f"{name:<20} | {avg:>5.1f} | {color}{grade:^5}{reset} | {comment}")

def show_statistics(student_names, student_results):
    averages = [result['average'] for result in student_results]

    class_avg = sum(averages) / len(averages)
    max_avg = max(averages)
    min_avg = min(averages)

    max_index = averages.index(max_avg)
    min_index = averages.index(min_avg)

    print("\n" + "=" * 50)
    print("          CLASS STATISTICS")
    print("=" * 50)

    print(f"Total Students: {len(student_names)}")
    print(f"Class Average: {class_avg:.1f}")
    print(f"Highest Average: {max_avg:.1f} ({student_names[max_index]})")
    print(f"Lowest Average: {min_avg:.1f} ({student_names[min_index]})")

def search_student(student_names, student_results):
    name = input("Enter student name to search: ")

    for i in range(len(student_names)):
        if student_names[i].lower() == name.lower():
            result = student_results[i]

            print("\nStudent Found:")
            print(f"Name: {student_names[i]}")
            print(f"Average: {result['average']:.1f}")
            print(f"Grade: {result['grade']}")
            print(f"Comment: {result['comment']}")
            return

    print("Student not found.")

def save_to_file(student_names, student_results):
    try:
        with open("results.txt", "w") as file:
            file.write("STUDENT RESULTS\n")
            file.write("-" * 40 + "\n")

            for i in range(len(student_names)):
                result = student_results[i]

                file.write(f"{student_names[i]}")
                file.write(f" | {result['average']:.1f}")
                file.write(f" | {result['grade']}")
                file.write(f" | {result['comment']}\n")

        print("Results saved to results.txt")

    except:
        print("Error saving file")

def main():

    student_names = []
    student_results = []

    while True:

        print("\n" + "=" * 50)
        print("      STUDENT GRADE CALCULATOR MENU")
        print("=" * 50)

        print("1. Enter Student Data")
        print("2. View Results")
        print("3. View Statistics")
        print("4. Search Student")
        print("5. Save Results to File")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":

            while True:
                try:
                    num_students = int(input("Enter number of students: "))
                    if num_students > 0:
                        break
                    else:
                        print("Enter positive number")
                except ValueError:
                    print("Enter valid number")

            for i in range(num_students):

                print(f"\n=== STUDENT {i+1} ===")

                name = input("Student name: ")

                while name.strip() == "":
                    print("Name cannot be empty")
                    name = input("Student name: ")

                student_names.append(name)

                print("Enter marks (0-100)")

                math = get_valid_number("Math: ")
                science = get_valid_number("Science: ")
                english = get_valid_number("English: ")

                average = (math + science + english) / 3

                grade, comment = calculate_grade(average)

                student_results.append({
                    "average": average,
                    "grade": grade,
                    "comment": comment
                })

        elif choice == "2":

            if len(student_names) == 0:
                print("No data available")
            else:
                display_results(student_names, student_results)

        elif choice == "3":

            if len(student_names) == 0:
                print("No data available")
            else:
                show_statistics(student_names, student_results)

        elif choice == "4":

            if len(student_names) == 0:
                print("No data available")
            else:
                search_student(student_names, student_results)

        elif choice == "5":

            if len(student_names) == 0:
                print("No data available")
            else:
                save_to_file(student_names, student_results)

        elif choice == "6":

            print("Goodbye")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()