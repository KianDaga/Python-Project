store_a_inventory = {
    'apples': 20,
    'bananas': 30,
    'oranges': 10,
    'grapes': 60
}

store_b_inventory = {
    'apples': 25,
    'bananas': 15,
    'kiwis': 55,
    'grapes': 45
}

both_inventory = store_a_inventory | store_b_inventory
low_inventory = {key: value for key, value in (both_inventory).items() if value < 25}

high_inventory = {value: key for key, value in (both_inventory).items() if value > 50}

#print("Low Inventory Items: ")
#print(low_inventory)
#print("High Inventory Items: ")
#print(high_inventory)
final_inventory = low_inventory | high_inventory
sorted_by_value = dict(sorted(both_inventory.items(), key=lambda item: item[1]))
#print(sorted_by_value)
print(high_inventory)