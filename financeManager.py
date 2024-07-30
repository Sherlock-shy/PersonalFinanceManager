import csv
import gspread
import time

MONTH = 'april'
total = 0.0
transactions = []

file = f"lloyds_{MONTH}.csv"

def lloydsFin(file, month):
    global total
    global transactions

    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            date = row['Transaction Date']
            name = row['Transaction Description']

            try:
                amount = float(row['Debit Amount']) if row['Debit Amount'] else 0.0
            except ValueError as e:
                print(f"ValueError: {e} - Invalid value for conversion to float")
                continue

            total += amount

            category = 'other'
            if name == "NX BUS CONTACTLESS":
                category = 'transport'
            elif name == "http://taobao.com":
                category = 'shopping'
            elif "UBER" in name:
                category = 'food'
            elif "BT" in name:
                category = 'internet bills'
            else:
                category = 'other'

            transaction = (date, name, category, amount)
            transactions.append(transaction)

    return transactions, total

# Authenticate and open the Google Sheets
sa = gspread.service_account()
sh = sa.open("Personal Finances")
wks = sh.worksheet(f"{MONTH}")

# Process the CSV file and get transactions
transactions, total = lloydsFin(file, MONTH)

# Insert each transaction into the Google Sheets
for transaction in transactions:
    wks.append_row(transaction)

print(f"Total: {total}")
