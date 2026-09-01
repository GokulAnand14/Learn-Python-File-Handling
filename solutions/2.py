# 2. Search and Extract (Intermediate)

def extract_errors(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if "ERROR" in line:
                outfile.write(line)
                
if __name__ == '__main__':
    extract_errors('../data/logs.txt', '../data/errors.txt')
    print("Extracted errors to data/errors.txt")
