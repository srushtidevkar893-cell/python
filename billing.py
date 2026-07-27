# Grocery Shop Billing

print("============== Grocery Shop Detail =================")
total = 0

# Item 1
n = int(input("Enter your items : "))
name = str(input("Enter your item name : "))
price = float(input("Enter your price : "))
quantity1 = float(input("Enter your quantity : "))
amount1 = price * quantity1
total += amount1

# Item 2
n = int(input("Enter your items : "))
name = str(input("Enter your item name : "))
price = float(input("Enter your price : "))
quantity2 = float(input("Enter your quantity : "))
amount2 = price * quantity2
total += amount2

amount = amount1 + amount2
quantity = quantity1 + quantity2

print("---------------- BILL ----------------")
print("Total price : ₹", amount)
print("Total Quantity :", quantity)

if amount >= 300:
    discount = total * 0.50
    print("Discount : 50% Discount")
elif amount >= 200:
    discount = total * 0.30
    print("Discount : 30% Discount")
elif amount >= 100:
    discount = total * 0.10
    print("Discount : 10% Discount")
else:
    discount = amount * 0.05
    print("Discount : No Discount")

final_amount = total - discount

print("--------------------------------------------")
print("Total amount : ₹", final_amount)
print("---------------- Thank You.... Visit Again 🙏 ----------------")