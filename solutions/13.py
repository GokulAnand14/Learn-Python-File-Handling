# 13. Text File Character Statistics (Board Level)

def char_statistics(filepath):
    vowels = consonants = uppercase = lowercase = 0
    vowel_set = set("aeiouAEIOU")
    
    with open(filepath, 'r') as f:
        content = f.read()
        
        for char in content:
            if char.isalpha():
                if char.isupper():
                    uppercase += 1
                elif char.islower():
                    lowercase += 1
                    
                if char in vowel_set:
                    vowels += 1
                else:
                    consonants += 1
                    
    print("Character Statistics:")
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Uppercase: {uppercase}")
    print(f"Lowercase: {lowercase}")

if __name__ == '__main__':
    char_statistics('../data/story.txt')
