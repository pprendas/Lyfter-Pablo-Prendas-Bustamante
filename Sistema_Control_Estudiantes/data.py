import csv
import os

from student import Student

CSV_FILE_NAME = "students.csv"
CSV_FIELD_NAMES = [
    "full_name", "section", "spanish_score", "english_score",
    "social_studies_score", "science_score",
]


def export_students_to_csv(students_list):
    """Exports the current students list to a CSV file."""
    if not students_list:
        print("\nThere are no students to export.")
        return

    with open(CSV_FILE_NAME, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELD_NAMES)
        writer.writeheader()
        for student in students_list:
            writer.writerow(student.to_dict())

    print(f"\nData exported successfully to '{CSV_FILE_NAME}'.")


def import_students_from_csv(students_list):
    """Imports students from a previously exported CSV file, if it exists."""
    if not os.path.exists(CSV_FILE_NAME):
        print(f"\nNo previous export found ('{CSV_FILE_NAME}' does not exist).")
        return

    with open(CSV_FILE_NAME, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        imported_students = [Student.from_dict(row) for row in reader]

    students_list.clear()
    students_list.extend(imported_students)
    print(f"\n{len(imported_students)} student(s) imported successfully.")
