import random

# Step 1: Read the student IDs from the file
def load_student_ids(students_ids):
    with open('students_ids.txt', 'r') as file:
        students_ids = [line.strip() for line in file if line.strip()]
    return students_ids

# Step 2: Maintain a list of students who haven’t been selected yet
def reset_student_list():
    return load_student_ids('students_ids.txt')

# Step 3-5: Randomly select a student, remove them, and repeat until all are picked
def select_students_for_viva(student_list):
    while student_list:
        selected_student = random.choice(student_list)
        print("Selected student: ", selected_student)
        student_list.remove(selected_student)

# Step 6: Reset the list once all students have been picked
def viva_selection_process():
    students = reset_student_list()
    select_students_for_viva(students)
    print("All students have been selected. Resetting the list.")
           
        

# Run the viva selection process
viva_selection_process()
