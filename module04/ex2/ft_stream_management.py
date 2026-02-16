import sys


def main():
    sys.stdout.write("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    archivist_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    sys.stdout.write(
        f"\n[STANDARD] Archive status from {archivist_id}: {status}\n"
    )

    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n"
    )

    sys.stdout.write("[STANDARD] Data transmission complete\n\n")
    sys.stdout.write("Three-channel communication test successful.\n")


if __name__ == "__main__":
    main()
