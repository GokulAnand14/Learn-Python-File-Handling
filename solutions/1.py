# 1. Count Words and Lines (Basic)

def count_words_and_lines(filepath):
    lines_count = 0
    words_count = 0
    chars_count = 0
    
    with open(filepath, 'r') as f:
        for line in f:
            lines_count += 1
            chars_count += len(line)
            words_count += len(line.split())
            
    print(f"| {'Metric':<10} | {'Count':<5} |")
    print(f"|{'-'*12}|{'-'*7}|")
    print(f"| {'Lines':<10} | {lines_count:<5} |")
    print(f"| {'Words':<10} | {words_count:<5} |")
    print(f"| {'Characters':<10} | {chars_count:<5} |")

if __name__ == '__main__':
    count_words_and_lines('../data/story.txt')
