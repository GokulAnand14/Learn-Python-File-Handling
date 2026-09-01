import os
import csv
import struct

def setup_data():
    os.makedirs('data', exist_ok=True)
    os.makedirs('data/server_logs', exist_ok=True)
    os.makedirs('solutions', exist_ok=True)
    
    # 1. story.txt
    with open('data/story.txt', 'w') as f:
        f.write("Once upon a time in a land far away,\n")
        f.write("there lived a python programmer.\n")
        f.write("He loved working with files.\n")
        f.write("Text files, CSV files, and Binary files.\n")
        f.write("He mastered them all.\n")
        
    # 2. logs.txt
    with open('data/logs.txt', 'w') as f:
        f.write("INFO: System started\n")
        f.write("WARNING: Low memory\n")
        f.write("ERROR: Failed to open file\n")
        f.write("INFO: User logged in\n")
        f.write("ERROR: Database connection timeout\n")
        
    # 3. server_logs
    log1 = ["[2023-10-01 10:00:00] INFO Start\n", "[2023-10-01 10:05:00] ERROR Crash\n"]
    log2 = ["[2023-10-01 10:02:00] INFO Process A\n", "[2023-10-01 10:04:00] WARNING High CPU\n"]
    log3 = ["[2023-10-01 10:01:00] INFO Process B\n", "[2023-10-01 10:06:00] INFO Stop\n"]
    with open('data/server_logs/log1.txt', 'w') as f: f.writelines(log1)
    with open('data/server_logs/log2.txt', 'w') as f: f.writelines(log2)
    with open('data/server_logs/log3.txt', 'w') as f: f.writelines(log3)
        
    # 4. grades.csv
    with open('data/grades.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Student_ID", "Math", "Science", "English"])
        writer.writerow(["1", "85", "90", "88"])
        writer.writerow(["2", "78", "82", "80"])
        writer.writerow(["3", "92", "95", "98"])
        
    # 5. employees.csv
    with open('data/employees.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Salary", "Hire_Date"])
        writer.writerow(["101", "Alice", "Engineering", "90000", "2016-05-12"])
        writer.writerow(["102", "Bob", "HR", "60000", "2014-08-23"])
        writer.writerow(["103", "Charlie", "Engineering", "75000", "2018-01-15"])
        writer.writerow(["104", "David", "Engineering", "85000", "2017-11-01"])
        
    # 6. sales.csv
    with open('data/sales.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Product", "Category", "Revenue"])
        writer.writerow(["2023-01-01", "Laptop", "Electronics", "1200"])
        writer.writerow(["2023-01-02", "Desk", "Furniture", "300"])
        writer.writerow(["2023-01-03", "Mouse", "Electronics", "50"])
        writer.writerow(["2023-01-04", "Chair", "Furniture", "150"])
        
    # 7. users.csv and orders.csv
    with open('data/users.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["User_ID", "Name", "Email"])
        writer.writerow(["1", "John", "john@example.com"])
        writer.writerow(["2", "Jane", "jane@example.com"])
    with open('data/orders.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Order_ID", "User_ID", "Amount", "Date"])
        writer.writerow(["1001", "1", "250.00", "2023-05-01"])
        writer.writerow(["1002", "2", "120.00", "2023-05-02"])
        writer.writerow(["1003", "1", "50.00", "2023-05-03"])

    # 8. sensor_data.bin
    with open('data/sensor_data.bin', 'wb') as f:
        # struct format: <i (int, 4 bytes), <f (float, 4 bytes), <i (int, 4 bytes)
        f.write(struct.pack('<ifi', 1, 22.5, 1630000000))
        f.write(struct.pack('<ifi', 2, 24.1, 1630000010))
        f.write(struct.pack('<ifi', 1, 22.7, 1630000020))
        f.write(struct.pack('<ifi', 2, 25.3, 1630000030))
        
    # 9. image.jpg (dummy binary file)
    with open('data/image.jpg', 'wb') as f:
        f.write(os.urandom(4096)) # 4KB of random bytes

    # --- Added for Class 12 Boards Preparation ---
    # 10. credentials.csv
    with open('data/credentials.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["UserID", "Password"])
        writer.writerow(["admin", "root123"])
        writer.writerow(["user01", "password@1"])
        writer.writerow(["gokul", "boardexams2024"])

    # 11. students.csv (Empty initially with headers)
    with open('data/students.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["RollNo", "Name", "Marks"])

    # 12. students.dat (Binary file with pickled list of dicts)
    students_data = [
        {"RollNo": 1, "Name": "Aarav", "Marks": 85},
        {"RollNo": 2, "Name": "Riya", "Marks": 92},
        {"RollNo": 3, "Name": "Vikram", "Marks": 78},
        {"RollNo": 4, "Name": "Neha", "Marks": 95}
    ]
    with open('data/students.dat', 'wb') as f:
        import pickle
        pickle.dump(students_data, f)

if __name__ == '__main__':
    setup_data()
    print("Data files generated successfully in the 'data' directory.")
