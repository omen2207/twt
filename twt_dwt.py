import csv

def read_csv_data(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            region = row[0]
            item_a = int(row[1])
            item_b = int(row[2])
            data.append({"region": region, "item_a": item_a, "item_b": item_b})
    return data

def calculate_weights(data):
    # Calculate the vertical sum for items A and B
    total_item_a = sum(row["item_a"] for row in data)
    total_item_b = sum(row["item_b"] for row in data)
    total_count = total_item_a + total_item_b

    results = []
    for row in data:
        region = row["region"]
        item_a = row["item_a"]
        item_b = row["item_b"]
        total_region = item_a + item_b
        t_weight_a = (item_a / total_region) * 100 if total_region > 0 else 0
        t_weight_b = (item_b / total_region) * 100 if total_region > 0 else 0
        d_weight_a = (item_a / total_item_a) * 100 if total_item_a > 0 else 0
        d_weight_b = (item_b / total_item_b) * 100 if total_item_b > 0 else 0
        results.append((region, item_a, t_weight_a, d_weight_a, item_b, t_weight_b, d_weight_b))
    
    return results, total_item_a, total_item_b

def print_results(results, total_item_a, total_item_b):
    for row in results:
        print(f"Region: {row[0]}, Item A Count: {row[1]}, T Weight A: {row[2]:.2f}%, D Weight A: {row[3]:.2f}%, "
              f"Item B Count: {row[4]}, T Weight B: {row[5]:.2f}%, D Weight B: {row[6]:.2f}%")
    
    print(f"Total Item A Count: {total_item_a}, Total Item B Count: {total_item_b}")

def main(file_path):
    data = read_csv_data(file_path)
    results, total_item_a, total_item_b = calculate_weights(data)
    print_results(results, total_item_a, total_item_b)

if __name__ == "__main__":
    input_file_path = r'C:\Users\bhilw\OneDrive\Documents\DM\5_twt_dwt\data.csv'
    main(input_file_path)
