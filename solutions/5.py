# 5. Read and Calculate Average (Basic)
import csv

def calculate_averages(filepath):
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            math = int(row['Math'])
            science = int(row['Science'])
            english = int(row['English'])
            
            avg = (math + science + english) / 3
            print(f"Student {row['Student_ID']}: {avg:.2f}")

if __name__ == '__main__':
    calculate_averages('../data/grades.csv')
