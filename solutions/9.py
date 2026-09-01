# 9. Write and Read Structs (Basic)
import pickle

def write_and_read_books(filepath):
    # Data to write
    books = [
        {"title": "Harry Potter", "author": "J.K. Rowling", "year": 1997},
        {"title": "Atomic Habits", "author": "James Clear", "year": 2018},
        {"title": "1984", "author": "George Orwell", "year": 1949},
        {"title": "Project Hail Mary", "author": "Andy Weir", "year": 2021}
    ]
    
    # Write
    with open(filepath, 'wb') as f:
        pickle.dump(books, f)
        
    # Read
    with open(filepath, 'rb') as f:
        loaded_books = pickle.load(f)
        
    print("Books published after 2000:")
    for book in loaded_books:
        if book['year'] > 2000:
            print(f"- {book['title']}")

if __name__ == '__main__':
    write_and_read_books('../data/books.dat')
