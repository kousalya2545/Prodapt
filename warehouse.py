# Warehouse Inventory Management System

inventory = {
    "Electronics": [
        {"product": "Laptop", "quantity": 0},
        {"product": "TV", "quantity": 0},
        {"product": "Headphones", "quantity": 0}
    ],
    "Clothing": [
        {"product": "T-Shirt", "quantity": 0},
        {"product": "Jeans", "quantity": 0},
        {"product": "Jacket", "quantity": 0}
    ],
    "Groceries": [
        {"product": "Rice", "quantity": 0},
        {"product": "Flour", "quantity": 0},
        {"product": "Sugar", "quantity": 0}
    ]
}

# Enter quantity available for each product
print("===== WAREHOUSE INVENTORY SYSTEM =====\n")

for category in inventory:
    for item in inventory[category]:
        while True:
            try:
                qty = int(input(f"Enter quantity for {item['product']}: "))
                if qty >= 0:
                    item['quantity'] = qty
                    break
                else:
                    print("Quantity cannot be negative. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Display organized inventory category-wise
print("\n\n===== INVENTORY SUMMARY =====")

stock_record = []

for category in inventory:
    print(f"\n{category}:")
    print("-" * 40)
    total_items = 0
    
    for item in inventory[category]:
        print(f"  {item['product']:<20} {item['quantity']:>10} units")
        stock_record.append({
            "category": category,
            "product": item['product'],
            "stock": item['quantity']
        })
        total_items += item['quantity']
    
    print(f"  {'Total:':<20} {total_items:>10} units")

# Record stock of every product for future inventory
print("\n\n===== STOCK RECORD FOR FUTURE REFERENCE =====\n")

for record in stock_record:
    print(f"{record['category']} | {record['product']:<15} | Stock: {record['stock']} units")