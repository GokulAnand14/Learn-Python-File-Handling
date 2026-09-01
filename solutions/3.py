# 3. File Reversal (Hard)

def reverse_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
        
    with open(output_file, 'w') as outfile:
        for line in reversed(lines):
            # Remove newline for character reversal, then add it back
            clean_line = line.rstrip('\n')
            reversed_line = clean_line[::-1] + '\n'
            outfile.write(reversed_line)

if __name__ == '__main__':
    reverse_file('../data/story.txt', '../data/story_reversed.txt')
    print("Reversed file created at data/story_reversed.txt")
