# 8. The Pure Python JOIN (Extreme)
import csv

def join_csvs(users_file, orders_file, output_file):
    # Read users into a dictionary for O(1) lookup
    users = {}
    with open(users_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            users[row['User_ID']] = row
            
    # Perform INNER JOIN while reading orders
    with open(orders_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        
        # Define new headers
        fieldnames = ["Order_ID", "Name", "Email", "Amount", "Date"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            user_id = row['User_ID']
            if user_id in users:
                user_info = users[user_id]
                # Combine info
                joined_row = {
                    "Order_ID": row['Order_ID'],
                    "Name": user_info['Name'],
                    "Email": user_info['Email'],
                    "Amount": row['Amount'],
                    "Date": row['Date']
                }
                writer.writerow(joined_row)

if __name__ == '__main__':
    join_csvs('../data/users.csv', '../data/orders.csv', '../data/user_orders.csv')
    print("Joined CSVs created at data/user_orders.csv")
