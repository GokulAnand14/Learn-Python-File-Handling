# 21. Text File - Word Search and Count (Board Level)

def search_word_in_file(filepath, target_word):
    count = 0
    target_word_lower = target_word.lower()
    
    with open(filepath, 'r') as f:
        print(f"--- Lines containing the word '{target_word}' ---")
        for line in f:
            # Convert line to lowercase for case-insensitive matching
            line_lower = line.lower()
            
            # Count occurrences in the current line
            words_in_line = line_lower.split()
            
            # Note: A strict equality check on words is often needed (e.g. removing punctuation)
            # For simplicity, we just count exact string matches in the split list, 
            # or use the count() method on the string.
            occurrences = line_lower.count(target_word_lower)
            
            if occurrences > 0:
                count += occurrences
                # Print the original line without the extra newline
                print(line.rstrip('\n'))
                
    print(f"\nTotal occurrences of '{target_word}': {count}")

if __name__ == '__main__':
    search_word_in_file('../data/story.txt', 'files')
