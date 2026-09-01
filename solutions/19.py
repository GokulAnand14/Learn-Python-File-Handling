# 19. Delete a Record in Binary File (Board Level)
import pickle

def delete_student(roll_no):
    # Read all records
    with open('../data/students.dat', 'rb') as f:
        records = pickle.load(f)
        
    initial_length = len(records)
    
    # Filter out the record to delete
    # Only keep students whose RollNo does NOT match the parameter
    records = [student for student in records if student['RollNo'] != roll_no]
    
    if len(records) < initial_length:
        # Overwrite the file with the filtered list
        with open('../data/students.dat', 'wb') as f:
            pickle.dump(records, f)
        print(f"Student with RollNo {roll_no} deleted successfully.")
    else:
        print("Student not found, nothing deleted.")

if __name__ == '__main__':
    delete_student(3)
