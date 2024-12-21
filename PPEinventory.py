import os

def initialize_inventory():
    inventory_file = "PPE_Inventory.txt"
    if not os.path.exists(inventory_file):
        # Predefined PPE items
        initial_items = [
            {"id": "MASK", "name": "Face Mask", "quantity": 100},
            {"id": "GLOVE", "name": "Gloves", "quantity": 200},
            {"id": "SAN", "name": "Hand Sanitizer", "quantity": 150},
            {"id": "GOWN", "name": "Protective Gown", "quantity": 50},
            {"id": "SHIELD", "name": "Face Shield", "quantity": 80},
            {"id": "BOOT", "name": "Protective Boots", "quantity": 30},
        ]

        with open(inventory_file, "w") as file:
            for item in initial_items:
                file.write(f"{item['id']},{item['name']},{item['quantity']}\n")
        print("Inventory file created with initial items.")
    else:
        print("Inventory file already exists.")

def load_inventory():
    inventory = {}
    try:
        with open("PPE_Inventory.txt", "r") as file:
            for line in file:
                item_id, item_name, quantity = line.strip().split(",")
                inventory[item_id] = {"name": item_name, "quantity": int(quantity)}
    except FileNotFoundError:
        print("Error: Inventory file not found. Initializing new inventory.")
        initialize_inventory()
    return inventory

def save_inventory(inventory):
    with open("PPE_Inventory.txt", "w") as file:
        for item_id, details in inventory.items():
            file.write(f"{item_id},{details['name']},{details['quantity']}\n")

def add_ppe(inventory):
    item_id = input("Enter the PPE item ID: ").strip().upper()
    quantity_to_add = int(input("Enter the quantity to add: "))

    if item_id in inventory:
        inventory[item_id]["quantity"] += quantity_to_add
        print(f"Successfully added {quantity_to_add} units to {item_id}.")
    else:
        item_name = input("Item ID not found. Enter the item name to create it: ").strip()
        inventory[item_id] = {"name": item_name, "quantity": quantity_to_add}
        print(f"New item {item_id} created with {quantity_to_add} units.")

    save_inventory(inventory)

def distribute_ppe(inventory):
    item_id = input("Enter the PPE item ID: ").strip().upper()
    quantity_to_distribute = int(input("Enter the quantity to distribute: "))

    if item_id in inventory:
        if inventory[item_id]["quantity"] >= quantity_to_distribute:
            inventory[item_id]["quantity"] -= quantity_to_distribute
            print(f"Successfully distributed {quantity_to_distribute} units of {item_id}.")
        else:
            print("Error: Not enough stock available.")
    else:
        print("Error: Item ID not found in inventory.")

    save_inventory(inventory)

def main():
    initialize_inventory()
    inventory = load_inventory()

    while True:
        print("\nPPE Management System")
        print("1. Add/Receive PPE")
        print("2. Distribute PPE")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_ppe(inventory)
        elif choice == "2":
            distribute_ppe(inventory)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
