import math
hotdog_db = "hotdog_sales.txt"
def get_todays_sales_total():
    sales = float(input("Enter the total sales for today: "))
    return sales

def append_sales_to_file(sales, database_file):
    with open(database_file, 'a') as f:
        print(sales, file=f)
        # f.write(f"{sales}\n")

def read_all_sales(database_file):
    sales = []
    with open(database_file) as f:
        for line in f:
            sales.append(float(line.strip()))
    return sales

def calculate_stats(sales):
    stats = {}
    stats["average"] = sum(sales) / len(sales)
    stats["max"] = max(sales)
    stats["min"] = min(sales)
    stats["count"] = len(sales)
    return stats

def main():
    total = get_todays_sales_total()
    append_sales_to_file(total, hotdob_db)
    sales = read_all_sales(hotdog_db)
    stats = calculate_stats(sales)
    print(stats)

if __name__ == "__main__":
    main()