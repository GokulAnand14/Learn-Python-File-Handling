# Learn Python File Handling
If you haven't already make sure you brush up on Python File Handling basics (`open`, `read`, `write`, `csv` module, `pickle` module).

After reviewing the basics, try to complete the exercises listed below using the data provided in this repository.

All of the solutions are available in the repository in the `solutions/` folder.

## Setup
First, generate the sample data files that you will use for the exercises. 
Run the following command in your terminal from the root of the project:
```bash
python setup.py
```

This will create a `data/` folder with the necessary `.txt`, `.csv`, and `.bin` files.

## Text File Exercises

### 1. Count Words and Lines (Basic)
[Solution](solutions/1.py)

Write a program that reads `data/story.txt`. The program should output the total number of lines, the total number of words, and the total number of characters in the file.

### 2. Search and Extract (Intermediate)
[Solution](solutions/2.py)

Read `data/logs.txt` which contains server log messages. Extract all lines that contain the word "ERROR" (case-sensitive) and write them to a new file called `data/errors.txt`.

### 3. File Reversal (Hard)
[Solution](solutions/3.py)

Read `data/story.txt`. Create a new file called `data/story_reversed.txt` where the lines are in reverse order (the last line becomes the first line) AND the characters in each line are reversed.

### 4. Merging and Sorting Logs (Extreme)
[Solution](solutions/4.py)

You have multiple log files in the `data/server_logs/` folder (`log1.txt`, `log2.txt`, `log3.txt`). Each line in these logs starts with a timestamp in the format `[YYYY-MM-DD HH:MM:SS]`. Write a program that reads all these files, merges them, sorts the lines chronologically based on the timestamp, and writes the output to `data/merged_logs.txt`.

## CSV File Exercises

### 5. Read and Calculate Average (Basic)
[Solution](solutions/5.py)

Read the `data/grades.csv` file which has columns `Student_ID, Math, Science, English`. Calculate the average grade for each student and print it in the format: `Student X: Y`.

### 6. Filter by Complex Conditions (Intermediate)
[Solution](solutions/6.py)

Read `data/employees.csv` (columns: `ID, Name, Department, Salary, Hire_Date`). Extract employees who work in the "Engineering" department AND have a salary greater than 80,000 AND were hired after 2015. Write the extracted records to a new CSV file `data/high_earners.csv`.

### 7. CSV Group By Aggregation (Hard)
[Solution](solutions/7.py)

Using `data/sales.csv` (columns: `Date, Product, Category, Revenue`), write a script to calculate the total revenue for each `Category`. Write the result to `data/category_summary.csv` with columns `Category, Total_Revenue` sorted by `Total_Revenue` in descending order. **Rule: Do not use pandas or any external libraries.**

### 8. The Pure Python JOIN (Extreme)
[Solution](solutions/8.py)

You have two files: `data/users.csv` (`User_ID, Name, Email`) and `data/orders.csv` (`Order_ID, User_ID, Amount, Date`). Write a Python script to perform an INNER JOIN on `User_ID` without using pandas. The output should be written to `data/user_orders.csv` with columns `Order_ID, Name, Email, Amount, Date`.

## Binary File Exercises

### 9. Write and Read Structs (Basic)
[Solution](solutions/9.py)

Create a list of dictionaries in Python (e.g., representing books with title, author, and year). Use the `pickle` module to write this list to a binary file `data/books.dat`. Then, write a function to read the file and print the titles of the books published after 2000.

### 10. Chunked File Copy (Intermediate)
[Solution](solutions/10.py)

Read the binary file `data/image.jpg`. Write a script that copies this file to `data/image_copy.jpg`. However, you are not allowed to read the whole file into memory at once. You must read and write the file in chunks of 1024 bytes.

### 11. Custom Binary Format Parser (Hard)
[Solution](solutions/11.py)

The file `data/sensor_data.bin` contains binary data written in a specific C-struct format. Every record is exactly 12 bytes:
- An integer `sensor_id` (4 bytes, little-endian)
- A float `temperature` (4 bytes, little-endian)
- An integer `timestamp` (4 bytes, little-endian)

Write a program using the `struct` module to read this file, extract all records, and find the maximum temperature recorded by sensor ID 2.

### 12. Steganography - Hide a Message (Extreme)
[Solution](solutions/12.py)

Take the binary file `data/image.jpg`. Append a secret message string (e.g., "SUPER_SECRET_KEY=42") to the end of the file, then create a new file `data/secret_image.jpg`. Since image viewers stop reading after the EOF marker, the image will still be viewable. 
Then, write a second function that reads `data/secret_image.jpg`, extracts the hidden string from the end of the file, and prints it out.
