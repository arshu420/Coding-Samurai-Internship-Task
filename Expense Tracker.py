import os
import datetime

# Initialize an empty list to store expenses
expenses = []

# Function to add an expense
def add_expense():
    date = datetime.datetime.now()
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the expense category: ")
    description = input("Enter a brief description: ")
    
    expense = {
        "Date": date.strftime("%Y-%m-%d %H:%M:%S"),
        "Amount": amount,
        "Category": category,
        "Description": description,
    }
    
    expenses.append(expense)
    print("Expense added successfully!")

# Function to list expenses
def list_expenses():
    if not expenses:
        print("No expenses found.")
    else:
        print("\nExpense List:")
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. Date: {expense['Date']}")
            print(f"   Amount: ${expense['Amount']:.2f}")
            print(f"   Category: {expense['Category']}")
            print(f"   Description: {expense['Description']}\n")

# Function to calculate and display total expenses for a specified time frame
def calculate_total_expenses():
    try:
        start_date = datetime.datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d")
        end_date = datetime.datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d")
        
        total_expenses = sum(expense['Amount'] for expense in expenses if start_date <= datetime.datetime.strptime(expense['Date'], "%Y-%m-%d %H:%M:%S") <= end_date)
        
        print(f"Total expenses from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}: ${total_expenses:.2f}")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

# Function to generate and display a monthly report
def generate_monthly_report():
    try:
        report_month = datetime.datetime.strptime(input("Enter report month (YYYY-MM): "), "%Y-%m")
        
        monthly_expenses = [expense for expense in expenses if datetime.datetime.strptime(expense['Date'], "%Y-%m-%d %H:%M:%S").month == report_month.month]
        
        if not monthly_expenses:
            print("No expenses found for the specified month.")
        else:
            print(f"\nMonthly Report for {report_month.strftime('%B %Y')}:")
            categories = set(expense['Category'] for expense in monthly_expenses)
            
            for category in categories:
                category_total = sum(expense['Amount'] for expense in monthly_expenses if expense['Category'] == category)
                print(f"{category}: ${category_total:.2f}")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM.")

# Function to save expenses to a text file
def save_expenses():
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense['Date']},{expense['Amount']},{expense['Category']},{expense['Description']}\n")
    print("Expenses saved to 'expenses.txt'.")

# Function to load expenses from a text file
def load_expenses():
    global expenses
    expenses = []
    if os.path.exists("expenses.txt"):
        with open("expenses.txt", "r") as file:
            for line in file:
                date, amount, category, description = line.strip().split(",")
                expenses.append({
                    "Date": date,
                    "Amount": float(amount),
                    "Category": category,
                    "Description": description
                })
        print("Expenses loaded from 'expenses.txt'.")

# Main loop
while True:
    print("\nExpense Tracker Application")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Calculate Total Expenses for a Time Frame")
    print("4. Generate Monthly Report")
    print("5. Save Expenses")
    print("6. Load Expenses")
    print("7. Quit")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        list_expenses()
    elif choice == "3":
        calculate_total_expenses()
    elif choice == "4":
        generate_monthly_report()
    elif choice == "5":
        save_expenses()
    elif choice == "6":
        load_expenses()
    elif choice == "7":
        print("Thank you for using the Expense Tracker Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-7).")
