import re

from student import Student

section_format = r"^[0-9]{1,2}[a-zA-Z]$"
name_format = r"^[a-zA-Z ]+$"
 
 
def is_valid_name(name):
    """A valid name is not empty and contains only letters and single spaces."""
    return bool(re.match(NAME_PATTERN, name.strip()))


def is_valid_section(section):
    """A valid section looks like '10A', '11B', etc: 1-2 digits + 1 letter."""
    return bool(re.match(SECTION_PATTERN, section.strip()))


def student_exists(students_list, full_name, section):
    """Checks if a student with the same name AND section already exists."""
    for student in students_list:
        if (student.full_name.lower() == full_name.lower() and
                student.section.lower() == section.lower()):
            return True
    return False


def get_valid_name():
    """Keeps asking for a name until it is valid (not empty, no numbers)."""
    while True:
        name = input("Full name: ").strip()
        if is_valid_name(name):
            return name
        print("Invalid name. Please use letters only (no numbers, not empty).")


def get_valid_section():
    """Keeps asking for a section until it matches the expected format."""
    while True:
        section = input("Section (example: 11B): ").strip()
        if is_valid_section(section):
            return section
        print("Invalid section. Expected format like '10A' or '11B'.")


def get_valid_score(subject_name):
    """Keeps asking for a score until it is a number between 0 and 100."""
    while True:
        raw_value = input(f"{subject_name} score (0-100): ").strip()
        try:
            score = float(raw_value)
        except ValueError:
            print("Invalid score. Please enter a number.")
            continue
        if 0 <= score <= 100:
            return score
        print("Invalid score. It must be between 0 and 100.")


def create_student(students_list):
    """Asks the user for all the data of one student and adds it to the list."""
    print("\n--- New Student ---")
    full_name = get_valid_name()
    section = get_valid_section()

    if student_exists(students_list, full_name, section):
        print("A student with that name and section already exists. Not added.")
        return

    spanish_score = get_valid_score("Spanish")
    english_score = get_valid_score("English")
    social_studies_score = get_valid_score("Social Studies")
    science_score = get_valid_score("Science")

    new_student = Student(
        full_name, section, spanish_score, english_score,
        social_studies_score, science_score
    )
    students_list.append(new_student)
    print(f"Student '{full_name}' added successfully.")


def view_all_students(students_list):
    """Prints all students currently stored."""
    if not students_list:
        print("\nThere are no students registered yet.")
        return

    print("\n--- All Students ---")
    for student in students_list:
        print(student)


def view_top_students(students_list, top_count=3):
    """Prints the top N students ranked by average score, highest first."""
    if not students_list:
        print("\nThere are no students registered yet.")
        return

    sorted_students = sorted(
        students_list, key=lambda student: student.get_average(), reverse=True
    )

    print(f"\n--- Top {top_count} Students ---")
    for position, student in enumerate(sorted_students[:top_count], start=1):
        print(f"{position}. {student}")


def view_general_average(students_list):
    """Prints the average of all students' averages."""
    if not students_list:
        print("\nThere are no students registered yet.")
        return

    total_average = sum(student.get_average() for student in students_list)
    general_average = total_average / len(students_list)
    print(f"\nGeneral average of all students: {general_average:.2f}")


def view_failed_students(students_list):
    """Prints students who have at least one subject score below 60."""
    failed_students = [s for s in students_list if s.get_failed_subjects()]

    if not failed_students:
        print("\nNo students have failed subjects.")
        return

    print("\n--- Failed Students ---")
    for student in failed_students:
        print(f"\n{student.full_name} ({student.section})")
        for subject_name, score in student.get_failed_subjects():
            print(f"  - {subject_name}: {score}")


def delete_student(students_list):
    """Removes a student by name and section, after confirmation."""
    if not students_list:
        print("\nThere are no students registered yet.")
        return

    full_name = input("Full name of the student to delete: ").strip()
    section = input("Section of the student to delete: ").strip()

    target_student = None
    for student in students_list:
        if (student.full_name.lower() == full_name.lower() and
                student.section.lower() == section.lower()):
            target_student = student
            break

    if target_student is None:
        print("No student found with that name and section.")
        return

    confirmation = input(
        f"Are you sure you want to delete '{target_student.full_name}' "
        f"({target_student.section})? (y/n): "
    ).strip().lower()

    if confirmation == "y":
        students_list.remove(target_student)
        print("Student deleted successfully.")
    else:
        print("Deletion cancelled.")
