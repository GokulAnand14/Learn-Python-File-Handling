# 20. Random Access with Seek and Tell (Board Level)

def demonstrate_seek_tell(filepath):
    with open(filepath, 'r') as f:
        # 1. Initial position
        initial_pos = f.tell()
        print(f"1. Initial pointer position: {initial_pos}")
        
        # 2. Read first 10 characters
        first_10 = f.read(10)
        print(f"2. Read first 10 chars: '{first_10}'")
        
        # 3. New position
        new_pos = f.tell()
        print(f"3. Pointer position after reading: {new_pos}")
        
        # 4. Seek to 5th byte (offset 5 from beginning)
        f.seek(5)
        print("4. Moved pointer back to 5th byte using seek(5).")
        
        # 5. Read next 5 characters
        next_5 = f.read(5)
        print(f"5. Read next 5 chars from position 5: '{next_5}'")

if __name__ == '__main__':
    demonstrate_seek_tell('../data/story.txt')
