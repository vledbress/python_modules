def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for i in plant_list:
            if not isinstance(i, str):
                raise ValueError(F"Cannot water {i} - invalid plant!")
            print(F"Watering {i}")
    except ValueError as e:
        print(F"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    good_plants = ["tomato", "lettuce", "carrots"]
    bad_plants = ["tomato", None, "carrots"]
    print("Testing normal watering...")
    water_plants(good_plants)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    water_plants(bad_plants)
    print("\nCleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering System ===")
    test_watering_system()


if __name__ == "__main__":
    main()
