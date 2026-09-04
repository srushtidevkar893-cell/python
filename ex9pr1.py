# Consumer Transaction Tracker

transactions = []

# Accept five transaction values
for i in range(5):
    amount = float(input(f"Enter transaction {i + 1}: ₹"))
    transactions.append(amount)

# Calculate average spend
average_spend = sum(transactions) / len(transactions)

# Display transactions and average
print("\nTransaction Details")
print("--------------------")

for i, amount in enumerate(transactions, start=1):
    print(f"Transaction {i}: ₹{amount:.2f} | Average Spend: ₹{average_spend:.2f}")
