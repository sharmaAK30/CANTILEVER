DATA_FILE = 'finance.txt'

def load_records():
    records = []
    try:
        with open(DATA_FILE, 'r') as f:
            for line in f
                record_type, amount, desc = line.strip().split(',', 2)
                records.append({'type': record_type, 'amount': float(amount), 'desc': desc})
    except FileNotFoundError:
        pass
    return records

def save_records(records):
    with open(DATA_FILE, 'w') as f:
        for r in records:
            f.write(f"{r['type']},{r['amount']},{r['desc']}\n")

def add_income(records):
    amount = float(input("Enter income amount: "))
    desc = input("Description: ")
    records.append({'type': 'income', 'amount': amount, 'desc': desc})
    save_records(records)
    print("Income added.\n")

def add_expense(records):
    amount = float(input("Enter expense amount: "))
    desc = input("Description: ")
    records.append({'type': 'expense', 'amount': amount, 'desc': desc})
    save_records(records)
    print("Expense added.\n")

def view_summary(records):
    income = sum(r['amount'] for r in records if r['type'] == 'income')
    expense = sum(r['amount'] for r in records if r['type'] == 'expense')
    balance = income - expense
    print(f"Total Income: {income}")
    print(f"Total Expenses: {expense}")
    print(f"Current Balance (Savings): {balance}\n")

def view_records(records):
    if not records:
        print("No records found.\n")
    else:
        for i, r in enumerate(records, 1):
            print(f"{i}. {r['type'].title()} | Amount: {r['amount']} | {r['desc']}")
    print()

def main():
    records = load_records()
    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. View All Records")
        print("5. Exit")
        choice = input("Choose option: ")
        if choice == '1':
            add_income(records)
        elif choice == '2':
            add_expense(records)
        elif choice == '3':
            view_summary(records)
        elif choice == '4':
            view_records(records)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == '__main__':
    main()
