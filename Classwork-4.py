fruits = ["Apple", "Banana", "Mango"]
vegetables = ["Carrot", "Potato", "Tomato"]
beverages = ["Juice", "Milk", "Tea"]

fruits.append("Orange")
vegetables.insert(1, "Onion")
beverages.pop()
inventory = [fruits, vegetables, beverages]

print(inventory)

print(fruits[:2])

print(vegetables[-1])

fruit_lengths = [len(x) for x in fruits]
print(fruit_lengths)

if "Water" in beverages:
    print("Water is in the beverages list")
else:
    print("Water is not in the beverages list")

first_items = (fruits[0], vegetables[0], beverages[0])
print(first_items)