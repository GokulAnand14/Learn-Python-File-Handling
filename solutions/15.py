# 15. Search in CSV (Board Level)
import csv

def search_user(user_id):
    found = False
    with open('../data/credentials.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip header
        for row in reader:
            if row[0] == user_id:
                print(f"User found! Password: {row[1]}")
                found = True
                break
                
    if not found:
        print("User not found")

if __name__ == '__main__':
    search_user("user01")
    search_user("unknown_user")
