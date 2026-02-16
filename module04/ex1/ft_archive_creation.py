def main():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    filename = "new_discovery.txt"

    print(f"Initializing new storage unit: {filename}")

    try:
        with open(filename, "w", encoding="utf-8") as f:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")

            entries = [
                "[ENTRY 001] New quantum algorithm discovered",
                "[ENTRY 002] Efficiency increased by 347%",
                "[ENTRY 003] Archived by Data Archivist trainee"
            ]

            for line in entries:
                print(line)
                f.write(line + "\n")

    except PermissionError:
        print("ERROR: Permission denied — cannot create archive.")

    except OSError as e:
        print("ERROR: Storage failure:", e)

    else:
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    main()
