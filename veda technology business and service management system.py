import json
import os

FILE_NAME = "veda_data.json"


# Load data from file
def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read saved data.")

    return {
        "programs": [],
        "services": [],
        "training": [],
        "internships": [],
        "inquiries": [],
        "requests": []
    }


# Save data to file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# Add a new record
def add_record(data, category):
    print(f"\n--- Add {category.title()} ---")

    name = input("Enter name/title: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    description = input("Enter description: ").strip()

    record = {
        "id": len(data[category]) + 1,
        "name": name,
        "description": description
    }

    data[category].append(record)
    save_data(data)

    print(f"{category.title()} added successfully!")


# View records
def view_records(data, category):
    print(f"\n--- {category.title()} List ---")

    if not data[category]:
        print("No records available.")
        return

    for record in data[category]:
        print("\nID:", record["id"])
        print("Name:", record["name"])
        print("Description:", record["description"])


# Search records
def search_records(data, category):
    keyword = input("Enter name to search: ").strip().lower()

    found = False

    for record in data[category]:
        if keyword in record["name"].lower():
            print("\nID:", record["id"])
            print("Name:", record["name"])
            print("Description:", record["description"])
            found = True

    if not found:
        print("No matching record found.")


# Main program
def main():
    data = load_data()

    categories = {
        "1": ("programs", "Technology Programs"),
        "2": ("services", "Digital Services"),
        "3": ("training", "Training Programs"),
        "4": ("internships", "Internship Programs"),
        "5": ("inquiries", "Customer Inquiries"),
        "6": ("requests", "Service Requests")
    }

    while True:
        print("\n========================================")
        print(" VEDA TECHNOLOGY MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Technology Programs")
        print("2. Digital Services")
        print("3. Training Programs")
        print("4. Internship Programs")
        print("5. Customer Inquiries")
        print("6. Service Requests")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "7":
            print("Thank you for using Veda Technology System!")
            break

        if choice not in categories:
            print("Invalid choice! Try again.")
            continue

        category, title = categories[choice]

        while True:
            print(f"\n--- {title} ---")
            print("1. Add Record")
            print("2. View Records")
            print("3. Search Records")
            print("4. Back to Main Menu")

            action = input("Enter your choice: ").strip()

            if action == "1":
                add_record(data, category)

            elif action == "2":
                view_records(data, category)

            elif action == "3":
                search_records(data, category)

            elif action == "4":
                break

            else:
                print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()