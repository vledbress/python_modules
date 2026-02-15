def main():
    print("=== Achievement Tracker System ===\n")

    alice = set(['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'])
    bob = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
    charlie = set(['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
                   'perfectionist'])

    print(f"Player Alice achievements: {alice}")
    print(f"Player Bob achievements: {bob}")
    print(f"Player Charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===")

    all_unique = alice.union(bob, charlie)
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}\n")

    common_all = alice.intersection(bob, charlie)
    print(f"Common to all players: {common_all}")

    rare = (alice.difference(bob, charlie)
            .union(bob.difference(alice, charlie))
            .union(charlie.difference(alice, bob)))
    print(f"Rare achievements (1 player): {rare}\n")

    alice_vs_bob_common = alice.intersection(bob)
    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)
    print(f"Alice vs Bob common: {alice_vs_bob_common}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
