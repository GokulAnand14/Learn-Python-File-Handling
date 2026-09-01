# 18. Update a Record in Binary File (Board Level)
import pickle

def update_marks(roll_no, new_marks):
    found = False
    
    # Read existing records
    with open('../data/students.dat', 'rb') as f:
        records = pickle.load(f)
        
    # Update the record in the list
    for student in records:
        if student['RollNo'] == roll_no:
            student['Marks'] = new_marks
            found = True
            break
            
    # Write the updated list back to the file
    if found:
        with open('../data/students.dat', 'wb') as f:
            pickle.dump(records, f)
        print(f"Marks updated for RollNo {roll_no}.")
    else:
        print("Student not found!")

if __name__ == '__main__':
    update_marks(2, 99)
