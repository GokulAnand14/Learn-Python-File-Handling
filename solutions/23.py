# 23. CSV File with Custom Delimiters (Board Level)
import csv

def write_custom_csv(filepath):
    data = [
        ["Item_ID", "Item_Name", "Price"],
        ["I01", "Keyboard", 1500],
        ["I02", "Mouse", 800],
        ["I03", "Monitor", 12000]
    ]
    
    with open(filepath, 'w', newline='') as f:
        # Use the delimiter parameter to specify the pipe character
        writer = csv.writer(f, delimiter='|')
        writer.writerows(data)
    print(f"Data written to {filepath} with pipe delimiter.")

def read_custom_csv(filepath):
    print(f"\nReading {filepath}:")
    with open(filepath, 'r') as f:
        # You MUST specify the same delimiter when reading
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            print(row)

if __name__ == '__main__':
    filepath = '../data/items.csv'
    write_custom_csv(filepath)
    read_custom_csv(filepath)
