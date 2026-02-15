import math


def distance(pos1: tuple, pos2: tuple) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def unpacking(player: tuple, coordinates: tuple) -> None:
    print("Unpacking demonstration:")
    x1, y1, z1 = player
    x2, y2, z2 = coordinates
    print(F"Player at x={x1}, y={y1}, z={z1}")
    print(F"Cordinates: X={x2}, Y={y2}, Z={z2}")


def main():
    print("=== Game Coordinate System ===\n")
    pos1 = (10, 20, 5)
    pos0 = (0, 0, 0)
    print(F"Position created: {pos1}")
    print(F"Distance between {pos0} and {pos1}: {distance(pos0, pos1)}\n")
    right_cords = "3,4,0"
    wrong_cords = "abc,def,ghi"
    print(F"Parsing coordinates: {right_cords}")
    try:
        right = tuple([int(x) for x in right_cords.split(",")])
        print(f"Parsed position: {right}")
        print(F"Distance between {pos0} and {right}: "
              F"{distance(pos0, right)}\n")
    except ValueError as e:
        print(F"Error parsing coordinates: {e}")
    print(F"Parsing invalid coordinates: {wrong_cords}")
    try:
        wrong = tuple([int(x) for x in wrong_cords.split(",")])
        print(f"Parsed position: {wrong}")
        print(F"Distance between {pos0} and {wrong}: "
              F"{distance(pos0, wrong)}\n")
    except ValueError as e:
        print(F"Error parsing coordinates: {e}")
    print()
    unpacking((3, 4, 0), (3, 4, 0))


if __name__ == "__main__":
    main()
