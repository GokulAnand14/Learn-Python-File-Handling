# 14. Line Filter (Board Level)

def filter_t_lines(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith('T') or line.startswith('t'):
                outfile.write(line)

if __name__ == '__main__':
    filter_t_lines('../data/story.txt', '../data/t_lines.txt')
    print("Lines starting with 'T' or 't' copied to data/t_lines.txt")
