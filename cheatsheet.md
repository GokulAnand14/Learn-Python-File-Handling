# Python File Handling Cheat Sheet

This cheat sheet covers the essential operations for handling text, CSV, and binary files in Python. Review this before diving into the exercises!

---

## 1. General Basics
The built-in `open()` function is used to open files. Always use the `with` statement (Context Manager) as it automatically handles closing the file even if exceptions occur.

```python
with open('filename.txt', 'r') as file:
    # do something with file
    pass
```

### Common File Modes
| Mode | Description |
|------|-------------|
| `'r'`  | Read (default). File must exist. |
| `'w'`  | Write. Creates a new file or overwrites an existing one. |
| `'a'`  | Append. Writes data to the end of the file. |
| `'b'`  | Binary mode (e.g., `'rb'`, `'wb'`). Used for non-text files. |
| `'+'`  | Update mode (read and write). E.g., `'r+'`, `'w+'`. |

---

## 2. Text Files

### Reading
```python
with open('data.txt', 'r') as f:
    # Read the entire file into a single string
    content = f.read()
    
    # Read exactly one line
    line = f.readline()
    
    # Read all lines into a list of strings
    lines = f.readlines()
```

### Iterating Efficiently
For large files, don't use `.readlines()` as it loads the entire file into memory. Iterate directly:
```python
with open('data.txt', 'r') as f:
    for line in f:
        print(line.strip()) # .strip() removes the trailing newline
```

### Writing
```python
with open('output.txt', 'w') as f:
    # Write a single string
    f.write("Hello World\n")
    
    # Write a list of strings (you must include \n manually)
    lines = ["Line 1\n", "Line 2\n"]
    f.writelines(lines)
```

---

## 3. CSV Files
The built-in `csv` module simplifies reading and writing CSVs.

### Standard Reader/Writer (Lists)
```python
import csv

# Reading
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row) # row is a List of strings

# Writing
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerows([["Alice", 25], ["Bob", 30]])
```
*(Note: Always use `newline=''` when writing CSVs in Python 3 to prevent blank lines on Windows).*

### Dictionary Reader/Writer (Dictionaries)
Using dictionaries is highly recommended when your CSV has a header row.
```python
import csv

# Reading
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Name'], row['Age']) # row is a Dictionary

# Writing
with open('output.csv', 'w', newline='') as f:
    fieldnames = ['Name', 'Age']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'Name': 'Alice', 'Age': 25})
```

---

## 4. Random Access (`seek` and `tell`)
Python allows you to jump around a file without having to read it sequentially. This is highly tested in board exams.

- **`file.tell()`**: Returns the current byte position of the file pointer.
- **`file.seek(offset, whence)`**: Moves the file pointer to a specific byte position.
  - `whence = 0`: Absolute file positioning (Default. From the beginning).
  - `whence = 1`: Seek relative to the current position (Only valid in binary mode `b`).
  - `whence = 2`: Seek relative to the file's end (Only valid in binary mode `b`).

```python
with open('data.txt', 'r') as f:
    print(f.tell())   # Output: 0 (Start of file)
    
    data = f.read(5)  # Read 5 characters
    print(data)
    
    print(f.tell())   # Output: 5
    
    f.seek(0)         # Jump back to the beginning of the file
    print(f.tell())   # Output: 0
```

---

## 5. Binary Files
Binary files deal with raw bytes (`bytes` objects) instead of strings. 

### Reading and Writing Raw Bytes
```python
# Write bytes
with open('data.bin', 'wb') as f:
    f.write(b'\x00\x01\x02\x03') # 'b' prefix denotes a bytes literal

# Read bytes in chunks
with open('large_image.jpg', 'rb') as f:
    chunk = f.read(1024) # Read 1024 bytes at a time
```

### The `pickle` Module
Pickle allows you to serialize (save) and deserialize (load) Python objects like lists and dictionaries into binary files.
```python
import pickle

data = {"key": "value", "numbers": [1, 2, 3]}

# Save object to file
with open('data.dat', 'wb') as f:
    pickle.dump(data, f)

# Load multiple objects from file (Crucial for Boards)
# When reading multiple records, you MUST use a try-except block for EOFError
with open('data.dat', 'rb') as f:
    try:
        while True:
            loaded_data = pickle.load(f)
            print(loaded_data)
    except EOFError:
        pass # Reached the end of the file
```

### The `struct` Module
Used to read/write specific binary C-structs. Great for custom binary formats.
```python
import struct

# Packing data into bytes: '<' (little-endian), 'i' (4-byte int), 'f' (4-byte float)
packed_data = struct.pack('<if', 42, 3.14)

with open('data.bin', 'wb') as f:
    f.write(packed_data)

# Unpacking data from bytes
with open('data.bin', 'rb') as f:
    raw_bytes = f.read(8) # Read 8 bytes
    integer, float_val = struct.unpack('<if', raw_bytes)
```
