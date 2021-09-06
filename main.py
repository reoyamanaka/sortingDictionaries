from customBubbleSort import customBubbleSort


sampleData = [{"minTemp": 4, "maxTemp": 10}, {"minTemp": -4, "maxTemp": 18}, {"minTemp": 4, "maxTemp": 10}, {"minTemp": 2, "maxTemp": 12}]

while True:
    sortKey = input("\nSelect key to sort list of dictionaries by:\n1) Minimum temperature\n2) Maximum temperature\n")
    if sortKey == "1":
        sortKey = "minTemp"
        break
    elif sortKey == "2":
        sortKey = "maxTemp"
        break
    else:
        print("Invalid option. Choose 1 or 2.")

while True:
    direction = input("In what order?\n1) Ascending\n2) Descending")
    if direction == "1":
        customBubbleSort(sampleData, sortKey, True)
        break
    elif direction == "2":
        customBubbleSort(sampleData, sortKey, False)
        break
    else:
        print("Invalid option. Choose 1 or 2.")

print(sampleData)
