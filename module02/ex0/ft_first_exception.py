
def check_temperature(temp_str):
    try:
        print(F"Testing temperature: {temp_str}")
        temp = int(temp_str)
        if (temp < 0):
            print(F"Temperature {temp}°C is too cold for plants (min 0°C)\n")
        elif (temp >= 0 and temp <= 40):
            print(F"Temperature {temp}°C is perfect for plants!\n")
        else:
            print(F"Temperature {temp}°C is too hot for plants (max 40°C)\n")
    except ValueError:
        print(F"Error: '{temp_str}' is not a valid number\n")


def main():
    print("=== Garden Temperature Checker ===\n")
    check_temperature(25)
    check_temperature("abc")
    check_temperature(100)
    check_temperature(-50)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
