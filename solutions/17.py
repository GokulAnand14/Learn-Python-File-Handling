# 17. Search a Record in Binary File (Board Level)
import pickle

def search_student(roll_no):
    found = False
    with open('../data/students.dat', 'rb') as f:
        try:
            records = pickle.load(f)
            for student in records:
                if student['RollNo'] == roll_no:
                    print(f"Student Found: {student}")
                    found = True
                    break
        except EOFError:
            pass
            
    if not found:
        print("Student not found!")

if __name__ == '__main__':
    search_student(2)
    search_student(10)
