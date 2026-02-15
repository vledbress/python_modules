import sys


def main():
    print("=== Inventory System Analysis ===")
    if (len(sys.argv) == 1):
        print("No arguments provided")
        return
    inventory = {item.split(":")[0]: int(item.split(":")[1])
                 for item in sys.argv[1:]}
    total = sum(inventory.values())
    print(F"Total items in inventory: {total}")
    print(F"Unique item types: {len(inventory)}\n")

    print("=== Current Inventory ===")
    for item, qty in inventory.items():
        percent = round(qty / total * 100, 1)
        unit = "unit" if qty == 1 else "units"
        print(f"{item}: {qty} {unit} ({percent}%)")

    print("\n=== Inventory Statistics ===")
    most_item = None
    least_item = None
    most_qty = -1
    least_qty = float("inf")
    for item, qty in inventory.items():
        if qty > most_qty:
            most_qty = qty
            most_item = item
        if qty < least_qty:
            least_qty = qty
            least_item = item
    print(f"Most abundant: {most_item} ({most_qty} units)")
    print(f"Least abundant: {least_item} ({least_qty} unit)")

    print("\n=== Item Categories ===")
    moderate = {}
    scarce = {}

    for item, qty in inventory.items():
        if qty >= 5:
            moderate[item] = qty
        else:
            scarce[item] = qty
    print("Moderate:", moderate)
    print("Scarce:", scarce)

    print("\n=== Management Suggestions ===")
    restock = []
    for k, v in inventory.items():
        if v == 1:
            restock.append(k)
    print(F"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    print(F"Dictionary keys: {list(inventory.keys())}")
    print(F"Dictionary values: {list(inventory.values())}")
    print("Sample lookup - 'sword' in inventory:", "sword" in inventory)


if __name__ == "__main__":
    main()
