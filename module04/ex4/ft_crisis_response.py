def crisis_handler(filename):
    if filename == "standard_archive.txt":
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
            print(f"SUCCESS: Archive recovered - `{content}`")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception:
        print("RESPONSE: Unexpected system anomaly")
    finally:
        if filename == "standard_archive.txt":
            print("STATUS: Normal operations resumed")
        elif filename == "classified_vault.txt":
            print("STATUS: Crisis handled, security maintained")
        else:
            print("STATUS: Crisis handled, system stable")
    print()


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    files_to_check = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]

    for file in files_to_check:
        crisis_handler(file)

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
