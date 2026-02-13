def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!\n")
    if water_level < 1:
        raise ValueError(F"Water level {water_level} is too low (min 1)\n")
    if water_level > 10:
        raise ValueError(F"Water level {water_level} is too high (max 10)\n")
    if sunlight_hours < 2:
        raise ValueError(F"Sunlight hours {sunlight_hours}"
                         " is too low (min 2)\n")
    if sunlight_hours > 12:
        raise ValueError(F"Sunlight hours {sunlight_hours} "
                         F"is too high (max 12)")
    print(F"Plant '{plant_name}' is healthy!\n")


def test_plant_checks():
    print("Testing good values...")
    try:
        check_plant_health("Tomato", 5, 5)
    except ValueError as e:
        print(F"Error: {e}")
    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(F"Error: {e}")
    print("Testing bad water level...")
    try:
        check_plant_health("Tomato", 15, 5)
    except ValueError as e:
        print(F"Error: {e}")
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("Tomato", 5, 0)
    except ValueError as e:
        print(F"Error: {e}")


def main():
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
    print("All error raising tests completed!")


if __name__ == "__main__":
    main()
