# 4. Merging and Sorting Logs (Extreme)
import os

def merge_and_sort_logs(log_dir, output_file):
    all_logs = []
    
    # Read all log files
    for filename in os.listdir(log_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(log_dir, filename), 'r') as f:
                all_logs.extend(f.readlines())
                
    # Sort chronologically
    # The timestamp is at the beginning of the line: [YYYY-MM-DD HH:MM:SS]
    # String comparison works perfectly for this format
    all_logs.sort()
    
    # Write to output file
    with open(output_file, 'w') as f:
        f.writelines(all_logs)

if __name__ == '__main__':
    merge_and_sort_logs('../data/server_logs', '../data/merged_logs.txt')
    print("Logs merged and sorted into data/merged_logs.txt")
