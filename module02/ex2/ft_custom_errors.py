class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant_health(is_wilting: bool):
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def check_water_levels(liters: int):
    if liters < 5:
        raise WaterError("Not enough water in the tank!")


def main():
    print("=== Custom Garden Errors Demo ===")
    print("Testing PlantError...")
    try:
        check_plant_health(True)
    except PlantError as e:
        print(F"Caught PlantError: {e}\n")
    print("Testing WaterError...")
    try:
        check_water_levels(3)
    except WaterError as e:
        print(F"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    try:
        check_plant_health(True)
    except GardenError as e:
        print(F"Caught GardenError: {e}")
    try:
        check_water_levels(3)
    except GardenError as e:
        print(F"Caught GardenError: {e}\n")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
