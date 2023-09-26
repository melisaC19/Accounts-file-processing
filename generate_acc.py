import csv
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Create a list to store the generated accounts
accounts = []

# Generate 1000 accounts
for _ in range(1000):
    # Generate fake data for each field
    user_id = fake.unique.random_number(digits=5)
    plan = random.choice(["free", "basic", "full"])
    username = fake.user_name()
    last_login_date = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=None)
    expire_date = last_login_date + timedelta(days=random.randint(30, 365))
    
    # Append the account data to the list
    accounts.append([user_id, plan, username, last_login_date.strftime('%Y-%m-%d %H:%M:%S'), expire_date.strftime('%Y-%m-%d %H:%M:%S')])

# Write the data to a CSV file
with open('accounts.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header
    csvwriter.writerow(['id', 'plan', 'username', 'last_login_date', 'expire_date'])
    # Write the account data
    csvwriter.writerows(accounts)

print("Generated 1000 accounts and saved them to accounts.csv")
