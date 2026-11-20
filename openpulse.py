import csv
import sys
from collections import Counter


def profile_dataset(filename):
    with open(filename, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not reader.fieldnames:
        raise ValueError("The CSV file has no column headers.")

    print("\n========== OPENPULSE REPORT ==========")
    print(f"Dataset: {filename}")
    print(f"Rows: {len(rows)}")
    print(f"Columns: {len(reader.fieldnames)}")

    for column in reader.fieldnames:
        values = [row[column] for row in rows]
        missing = sum(
            1 for value in values
            if value is None or value.strip() == ""
        )

        present = [
            value.strip() for value in values
            if value is not None and value.strip() != ""
        ]

        numeric = []
        for value in present:
            try:
                numeric.append(float(value))
            except ValueError:
                pass

        print(f"\n--- {column} ---")
        print(f"Missing values: {missing}")
        print(f"Unique values: {len(set(present))}")

        if present and len(numeric) == len(present):
            print(f"Type: Numeric")
            print(f"Average: {sum(numeric) / len(numeric):.2f}")
            print(f"Minimum: {min(numeric)}")
            print(f"Maximum: {max(numeric)}")
        else:
            print("Type: Text or mixed")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python openpulse.py dataset.csv")
    else:
        try:
            profile_dataset(sys.argv[1])
        except (OSError, ValueError) as error:
            print(f"Error: {error}")
