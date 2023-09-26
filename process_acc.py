import csv
from datetime import datetime, timedelta

# Function to load data from the CSV file
def load_accounts_from_csv(file_path):
    accounts = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            accounts.append(row)
    return accounts

# Main program
if __name__ == "__main__":
    accounts_file = 'accounts.csv'
    accounts_data = load_accounts_from_csv(accounts_file)

    # Define a menu for options
    while True:
        print("\nMenu:")
        print("1. Print total accounts per plan")
        print("2. Find free accounts with more than 3 months to login")
        print("3. Find basic or full accounts that are expired")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Print total accounts per plan
            plan_counts = {"free": 0, "basic": 0, "full": 0}
            for account in accounts_data:
                plan = account["plan"].lower()
                if plan in plan_counts:
                    plan_counts[plan] += 1

            for plan, count in plan_counts.items():
                print(f"{plan.capitalize()}: {count} accounts")

        elif choice == '2':
            # Find free accounts with more than 3 months to login
            for account in accounts_data:
                if account["plan"].lower() == "free":
                    last_login_date = account["last_login_date"]
                    if last_login_date:
                        last_login_date = datetime.strptime(last_login_date, '%Y-%m-%d %H:%M:%S')
                        three_months_ago = datetime.now() - timedelta(days=90)
                        if last_login_date < three_months_ago:
                            print(f"Username: {account['username']} has more than 3 months to login.")

        elif choice == '3':
            # Find basic or full accounts that are expired
            for account in accounts_data:
                if account["plan"].lower() in ["basic", "full"]:
                    expire_date = account["expire_date"]
                    if expire_date:
                        expire_date = datetime.strptime(expire_date, '%Y-%m-%d %H:%M:%S')
                        if expire_date < datetime.now():
                            print(f"Username: {account['username']} is expired.")

        elif choice == '4':
            # Exit the program
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
