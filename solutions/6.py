# 6. Filter by Complex Conditions (Intermediate)
import csv
from datetime import datetime

def filter_employees(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        
        # Write headers
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        
        for row in reader:
            salary = float(row['Salary'])
            hire_year = datetime.strptime(row['Hire_Date'], "%Y-%m-%d").year
            
            if row['Department'] == 'Engineering' and salary > 80000 and hire_year > 2015:
                writer.writerow(row)

if __name__ == '__main__':
    filter_employees('../data/employees.csv', '../data/high_earners.csv')
    print("Filtered employees to data/high_earners.csv")
