

def check_temperature(temp_str: str) -> int | None:
    try:
        print(f"Testing temperature: {temp_str}")
        temp = int(temp_str)
        if temp < 0:
            print(f"Temperature {temp}°C is too cold for plants (min 0°C)\n")
            return None
        elif temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!\n")
            return temp
        else:
            print(f"Temperature {temp}°C is too hot for plants (max 40°C)\n")
            return None
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
