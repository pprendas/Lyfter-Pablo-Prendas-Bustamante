import actions
import data

MENU_OPTIONS = """
========== Student Control System ==========
1. Add a new student
2. View all students
3. View top 3 students
4. View general average
5. View failed students
6. Delete a student
7. Export data to CSV
8. Import data from CSV
9. Exit
==============================================
"""


def get_menu_choice():
    """Keeps asking until the user enters a valid menu option (1-9)."""
    while True:
        print(MENU_OPTIONS)
        raw_choice = input("Choose an option: ").strip()

        if raw_choice.isdigit() and 1 <= int(raw_choice) <= 9:
            return int(raw_choice)

        print("Invalid option. Please enter a number from 1 to 9.")


def run_menu(students_list):
    """Main loop: shows the menu and routes to the right action."""
    while True:
        choice = get_menu_choice()

        if choice == 1:
            actions.create_student(students_list)
        elif choice == 2:
            actions.view_all_students(students_list)
        elif choice == 3:
            actions.view_top_students(students_list)
        elif choice == 4:
            actions.view_general_average(students_list)
        elif choice == 5:
            actions.view_failed_students(students_list)
        elif choice == 6:
            actions.delete_student(students_list)
        elif choice == 7:
            data.export_students_to_csv(students_list)
        elif choice == 8:
            data.import_students_from_csv(students_list)
        elif choice == 9:
            print("\nNos vimos!!")
            break
