import mysql.connector
import time
import os

# ----------- Utility Functions -----------

def loading(message):
    print(message, end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print()

def clear():
    os.system('clear')  # Use 'cls' if on Windows

def banner():
    print("=" * 45)
    print("        🍕 PIZZA DELIVERY SYSTEM 🍕")
    print("=" * 45)

# ----------- Database Connection -----------

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",   # 🔴 CHANGE THIS
    database="pizza_delivery_db"
)

cursor = db.cursor()

# ----------- Main Program Loop -----------

while True:
    clear()
    banner()

    print("\n1. Add Customer")
    print("2. Search Customer")
    print("3. Update Customer")
    print("4. Delete Customer")
    print("5. View All Customers")
    print("6. Total Customers Count")
    print("7. Last Added Customer")
    print("8. Quit")

    choice = input("\nEnter your choice: ")

    # 1️⃣ ADD CUSTOMER
    if choice == '1':
        first = input("First Name: ")
        last = input("Last Name: ")
        address = input("Address: ")
        contact = input("Contact Number: ")

        loading("Adding customer")
        sql = "INSERT INTO customers (first_name, last_name, address, contact_number) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (first, last, address, contact))
        db.commit()
        print("Customer added successfully!")
        time.sleep(1)

    # 2️⃣ SEARCH CUSTOMER
    elif choice == '2':
        contact = input("Enter Contact Number: ")
        loading("Searching customer")

        cursor.execute("SELECT * FROM customers WHERE contact_number = %s", (contact,))
        result = cursor.fetchone()

        if result:
            print("\nCustomer Found:")
            print("ID:", result[0])
            print("Name:", result[1], result[2])
            print("Address:", result[3])
            print("Contact:", result[4])
        else:
            print("Customer not found!")
        input("\nPress Enter to continue...")

    # 3️⃣ UPDATE CUSTOMER
    elif choice == '3':
        contact = input("Enter Contact Number to update: ")
        new_address = input("New Address: ")

        loading("Updating customer")
        cursor.execute("UPDATE customers SET address = %s WHERE contact_number = %s", (new_address, contact))
        db.commit()

        if cursor.rowcount > 0:
            print("Customer updated successfully!")
        else:
            print("Customer not found!")
        time.sleep(1)

    # 4️⃣ DELETE CUSTOMER
    elif choice == '4':
        contact = input("Enter Contact Number to delete: ")

        loading("Deleting customer")
        cursor.execute("DELETE FROM customers WHERE contact_number = %s", (contact,))
        db.commit()

        if cursor.rowcount > 0:
            print("Customer deleted successfully!")
        else:
            print("Customer not found!")
        time.sleep(1)

    # 5️⃣ VIEW ALL CUSTOMERS
    elif choice == '5':
        loading("Fetching customer list")
        cursor.execute("SELECT * FROM customers")
        results = cursor.fetchall()

        if results:
            print("\n--- Customer List ---")
            for row in results:
                print(f"ID: {row[0]} | Name: {row[1]} {row[2]} | Address: {row[3]} | Contact: {row[4]}")
        else:
            print("No customers found!")
        input("\nPress Enter to continue...")

    # 6️⃣ TOTAL CUSTOMER COUNT
    elif choice == '6':
        cursor.execute("SELECT COUNT(*) FROM customers")
        count = cursor.fetchone()[0]
        print(f"\nTotal customers in system: {count}")
        input("\nPress Enter to continue...")

    # 7️⃣ LAST ADDED CUSTOMER
    elif choice == '7':
        cursor.execute("SELECT * FROM customers ORDER BY customer_id DESC LIMIT 1")
        result = cursor.fetchone()

        if result:
            print("\nLast Added Customer:")
            print("ID:", result[0])
            print("Name:", result[1], result[2])
            print("Address:", result[3])
            print("Contact:", result[4])
        else:
            print("No customers found!")
        input("\nPress Enter to continue...")

    # 8️⃣ QUIT
    elif choice == '8':
        print("Exiting program... Goodbye! 🍕")
        break

    else:
        print("Invalid choice!")
        time.sleep(1)

cursor.close()
db.close()
