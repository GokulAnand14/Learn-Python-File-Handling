# 7. CSV Group By Aggregation (Hard)
import csv

def summarize_revenue(input_file, output_file):
    revenue_by_category = {}
    
    # Read and aggregate
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            category = row['Category']
            revenue = float(row['Revenue'])
            revenue_by_category[category] = revenue_by_category.get(category, 0) + revenue
            
    # Sort by revenue descending
    sorted_categories = sorted(revenue_by_category.items(), key=lambda x: x[1], reverse=True)
    
    # Write output
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Category", "Total_Revenue"])
        for category, revenue in sorted_categories:
            writer.writerow([category, f"{revenue:.2f}"])

if __name__ == '__main__':
    summarize_revenue('../data/sales.csv', '../data/category_summary.csv')
    print("Summarized revenue to data/category_summary.csv")
