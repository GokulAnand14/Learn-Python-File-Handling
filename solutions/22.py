# 22. Binary File - Appending and Sequential Reading (Board Level)
import pickle

def append_student():
    student_record = {"RollNo": 5, "Name": "Rahul", "Marks": 88}
    
    # Open in 'ab' mode (append binary)
    with open('../data/students.dat', 'ab') as f:
        pickle.dump(student_record, f)
    print("Appended Rahul's record successfully.")

def read_all_students():
    print("\nReading all student records:")
    with open('../data/students.dat', 'rb') as f:
        try:
            while True:
                # Load one object at a time until the end of the file is reached
                record = pickle.load(f)
                print(record)
        except EOFError:
            # This exception is raised when there is no more data to read
            print("End of file reached.")

if __name__ == '__main__':
    append_student()
    read_all_students()
