# 16. Dynamic CSV Append (Board Level)
import csv

def add_student(roll_no, name, marks):
    # Note: Opened in 'a' (append) mode
    with open('../data/students.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([roll_no, name, marks])
        print(f"Record for {name} added successfully.")

if __name__ == '__main__':
    # Simulating user input
    add_student("101", "Gokul", "98")
    add_student("102", "Anand", "95")
