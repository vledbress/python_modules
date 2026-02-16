def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")

    try:
        with open("classified_data.txt", "r") as f:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            for line in f:
                print(line, end="")
            print("\n")

        with open("vault_preservation.txt", "w") as f:
            print("SECURE PRESERVATION:")
            f.write("[CLASSIFIED] New security protocols archived\n")
            print("[CLASSIFIED] New security protocols archived")

    except FileNotFoundError:
        print("SECURITY ALERT: Classified vault not found")

    else:
        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security")


if __name__ == "__main__":
    main()
