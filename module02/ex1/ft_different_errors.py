
def garden_operations():
    print("Testing ValueError...")
    try:
        int("five")
    except ValueError as e:
        print(F"Caught ValueError: {e}\n")
    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(F"Caught ZeroDivisionError: {e}\n")
    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError as e:
        print(F"Caught FileNotFoundError: {e}\n")
    print("Testing KeyError...")
    try:
        my_dict = {"key1": 1, "key2": 2}
        my_dict["key3"]
    except KeyError as e:
        print(F"Caught KeyError: {e}\n")
    print("Testing multiple errors together...")
    try:
        int("five")
        10 / 0
        open("missing.txt")
        my_dict = {"key1": 1, "key2": 2}
        my_dict["key3"]
    except Exception:
        print("Caught an error, but program continues!\n")


def main():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    main()
