

def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        print("Accessing Storage Vault: ancient_fragment.txt")
        with open("ancient_fragment.txt", "r") as f:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            for line in f:
                print(line, end="")
            print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("missing ancient_fragment.txt")


if __name__ == "__main__":
    main()
