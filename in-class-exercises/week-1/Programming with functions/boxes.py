import math
while True:
    print("SHIPPING CALCULATOR: ")
    items = int(input("Enter the number of items: "))
    itemsPerBox = int(input("Enter the number of items per box: "))
    boxes = math.ceil(items / itemsPerBox)
    print(f"For {items} items, packing {itemsPerBox} items in each box,\nyou will need {boxes} boxes.")