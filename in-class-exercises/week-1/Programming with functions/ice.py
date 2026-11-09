
def create_multiplication_table(size):
    table = []
    for row_index in range(size):
        row = []
        for column_index in range(size):
            x = row_index + 1
            y = column_index + 1
            product = x * y
            row.append(product)
        table.append(row)
    return table


def display_table(table):
    for row in table:
        for value in row:
            print(f"{value}", end="\t")
        print()


def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False

def count_parity(table):
    counts = {}
    counts["even"] = 0
    counts["odd"] = 0

    for row in table:
        for value in row:
            if is_even(value):
                counts["even"] += 1
            else:
                counts["odd"] += 1
    return counts


def main():
    print(" == Multiplication Table == ")
    size = 3
    table = create_multiplication_table(size)
    display_table(table)
    print("\n == Counts == ")
    counts = count_parity(table)
    print(counts)


main()