import csv
import json

csv_path = r"sa.csv"
json_path = r"sa1.json"

def read_csv_file(file_path):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            print(f"\nTotal rows: {len(rows)}")
            if rows:
                print("Columns:", list(rows[0].keys()))
                print("\nFirst 3 rows:")
                for row in rows[:3]:
                    print(row)
    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print("Error reading CSV:", e)

def read_json_file(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            data = json.load(file)
            print("\nData Type:", type(data))
            if isinstance(data, list):
                print(f"Total records: {len(data)}")
                print("First 3 records:")
                for item in data[:3]:
                    print(item)
            elif isinstance(data, dict):
                print("Top-level keys:", list(data.keys()))
                print("Sample value:", next(iter(data.values())))
            else:
                print("Unrecognized JSON structure.")
    except FileNotFoundError:
        print("JSON file not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
    except Exception as e:
        print("Error reading JSON:", e)

# Menu loop
while True:
    print("\n=== Read and Analyze Data ===")
    print("1. Read CSV File")
    print("2. Read JSON File")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        read_csv_file(csv_path)
    elif choice == '2':
        read_json_file(json_path)
    elif choice == '3':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice!")

    cont = input("\nDo you want to analyze another file? (yes/no): ").strip().lower()
    if cont != 'yes':
        print("Goodbye!")
        break


