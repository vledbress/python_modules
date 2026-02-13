class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, sun_hours: int, water_lvl: int):
        self.name = name
        self.sun_hours = sun_hours
        self.water_lvl = water_lvl

    def water(self):
        self.water_lvl += 1


class GardenManager:
    def __init__(self):
        self.plants = []
        self.water_tank = 10  # Начальный запас воды

    def add_plant(self, plant: Plant):
        if not plant.name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant)

    def water_plants(self):
        # Логика с обязательной очисткой ресурсов
        print("Opening watering system")
        try:
            if self.water_tank < len(self.plants):
                raise WaterError("Not enough water in tank")
            for plant in self.plants:
                plant.water()
                print(f"Watering {plant.name} - success")
        finally:
            # Гарантируем закрытие крана в любом случае
            print("Closing watering system (cleanup)")

    def check_health(self):
        for plant in self.plants:
            if plant.water_lvl < 1:
                raise WaterError(f"Error checking {plant.name}: Water level {plant.water_lvl} is too low (min 1)")
            elif plant.water_lvl > 10:
                raise WaterError(f"Error checking {plant.name}: Water level {plant.water_lvl} is too high (max 10)")
            elif plant.sun_hours < 2:
                raise PlantError(f"Error checking {plant.name}: Sunlight hours {plant.sun_hours} is too low (min 2)")
            elif plant.sun_hours > 12:
                raise PlantError(f"Error checking {plant.name}: Sunlight hours {plant.sun_hours} is too high (max 12)")
            else:
                print(f"{plant.name}: healthy (water: {plant.water_lvl}, sun: {plant.sun_hours})")


def test_garden_management():
    garden = GardenManager()
    print("Adding plants to garden...")
    try:
        garden.add_plant(Plant("tomato", 5, 8))
        print("Added tomato successfully")
        garden.add_plant(Plant("lettuce", 8, 14))
        print("Added lettuce successfully")
        garden.add_plant(Plant("", 5, 5))
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    try:
        garden.water_plants()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nChecking plant health...")
    try:
        garden.check_health()
    except GardenError as e:
        print(f"Error checking health: {e}")

    print("\nTesting error recovery...")
    try:
        garden.water_tank = 0
        if garden.water_tank == 0:
            raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    print("=== Garden Management System ===")
    test_garden_management()
