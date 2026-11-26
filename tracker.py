import sqlite3
#1. connect to (or create) a real database file
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()


#2. create a table if it doesn't exist yet
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT NOT NULL,
        amount REAL NOT NULL
    )
""")
  
conn.commit()

def add_expense(item, amount):
    cursor.execute("INSERT INTO expenses (item, amount) VALUES (?, ?)", (item, amount))
    conn.commit() 
    print(f"saved: {item} - NGN{amount}")

def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    print("\n--- your expenses ---")
    for row in rows:
        print(f"{row[0]}. {row[1]}: NGN{row[2]}")
    print("---------------------\n")

# simple menu loop 
while True:
    choice = input("choose: (1) Add Expense (2) View All (3) Quit: ")
    if choice == "1":
        item = input("what did you buy? ")
        amount = float(input("How much (NGN)? "))
        add_expense(item, amount)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid option.")
