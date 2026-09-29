import csv
import os
import matplotlib.pyplot as plt

students = [
    {"RollNo": 101, "Name": "Aarav Sharma", "Python": 92, "Maths": 88, "Physics": 90},
    {"RollNo": 102, "Name": "Diya Patel", "Python": 85, "Maths": 91, "Physics": 87},
    {"RollNo": 103, "Name": "Rohan Verma", "Python": 76, "Maths": 79, "Physics": 72},
    {"RollNo": 104, "Name": "Ananya Singh", "Python": 95, "Maths": 93, "Physics": 96},
    {"RollNo": 105, "Name": "Arjun Mehta", "Python": 68, "Maths": 74, "Physics": 70},
    {"RollNo": 106, "Name": "Meera Joshi", "Python": 88, "Maths": 84, "Physics": 90},
    {"RollNo": 107, "Name": "Kabir Khan", "Python": 72, "Maths": 69, "Physics": 75},
    {"RollNo": 108, "Name": "Ishita Gupta", "Python": 91, "Maths": 89, "Physics": 94},
    {"RollNo": 109, "Name": "Aditya Rao", "Python": 63, "Maths": 71, "Physics": 66},
    {"RollNo": 110, "Name": "Neha Sharma", "Python": 82, "Maths": 86, "Physics": 80}
]

def validate_data():
    for student in students:
        for subject in ["Python", "Maths", "Physics"]:
            if not 0 <= student[subject] <= 100:
                print("Invalid marks for", student["Name"])
                return False
    return True

def calculate_averages():
    for student in students:
        total = student["Python"] + student["Maths"] + student["Physics"]
        student["Average"] = total / 3

def display_students():
    print("\n" + "=" * 80)
    print("STUDENT RECORDS")
    print("=" * 80)
    print(f"{'Roll':<8}{'Name':<20}{'Python':<10}{'Maths':<10}{'Physics':<10}{'Average':<10}")
    print("-" * 80)
    for s in students:
        print(f"{s['RollNo']:<8}{s['Name']:<20}{s['Python']:<10}{s['Maths']:<10}{s['Physics']:<10}{s['Average']:.2f}")

def class_summary():
    average = sum(s["Average"] for s in students) / len(students)
    highest = max(students, key=lambda s: s["Average"])
    lowest = min(students, key=lambda s: s["Average"])
    passed = sum(1 for s in students if s["Average"] >= 40)
    print("\n" + "=" * 50)
    print("CLASS SUMMARY")
    print("=" * 50)
    print("Number of students :", len(students))
    print("Class average      :", round(average, 2), "%")
    print("Highest performer  :", highest["Name"], "-", round(highest["Average"], 2), "%")
    print("Lowest performer   :", lowest["Name"], "-", round(lowest["Average"], 2), "%")
    print("Students passed    :", passed)
    print("Students failed    :", len(students) - passed)

def show_top_students():
    ranked = sorted(students, key=lambda s: s["Average"], reverse=True)
    print("\nTOP 5 STUDENTS")
    print("-" * 40)
    for i, s in enumerate(ranked[:5], 1):
        print(i, ".", s["Name"], "-", round(s["Average"], 2), "%")

def subject_averages():
    print("\nSUBJECT AVERAGES")
    print("-" * 40)
    for subject in ["Python", "Maths", "Physics"]:
        average = sum(s[subject] for s in students) / len(students)
        print(subject, ":", round(average, 2))

def student_graph():
    names = [s["Name"] for s in students]
    averages = [s["Average"] for s in students]
    plt.figure(figsize=(10, 6))
    plt.bar(names, averages)
    plt.xlabel("Students")
    plt.ylabel("Average Marks")
    plt.title("Student Average Performance")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

def subject_graph():
    subjects = ["Python", "Maths", "Physics"]
    averages = [sum(s[x] for s in students) / len(students) for x in subjects]
    plt.figure(figsize=(7, 5))
    plt.bar(subjects, averages)
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.title("Subject-wise Class Average")
    plt.tight_layout()
    plt.show()

def save_to_csv():
    os.makedirs("output", exist_ok=True)
    filename = "output/student_report.csv"
    fields = ["RollNo", "Name", "Python", "Maths", "Physics", "Average"]
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(students)
    print("\nReport saved to:", filename)

def main():
    print("=" * 60)
    print("STUDENT PERFORMANCE ANALYZER")
    print("=" * 60)

    if not validate_data():
        return

    calculate_averages()

    while True:
        print("\n1. Display Student Records")
        print("2. View Class Summary")
        print("3. Show Top 5 Students")
        print("4. Show Subject Averages")
        print("5. Student Performance Graph")
        print("6. Subject Average Graph")
        print("7. Save Report to CSV")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_students()
        elif choice == "2":
            class_summary()
        elif choice == "3":
            show_top_students()
        elif choice == "4":
            subject_averages()
        elif choice == "5":
            student_graph()
        elif choice == "6":
            subject_graph()
        elif choice == "7":
            save_to_csv()
        elif choice == "8":
            print("Thank you for using Student Performance Analyzer!")
            break
        else:
            print("Invalid choice. Please enter 1-8.")

if __name__ == "__main__":
    main()
