'''
Q.  Build a Python program that:
    • accepts customer name,
    • accepts electricity units consumed,
    • calculates total bill,
    • prints a professional formatted receipt.
    Billing Rules:
    • First 100 units → ₹5/unit
    • Remaining units → ₹18/unit
'''
# --- code is from here ---

name = input("Enter name of the costumer : ")
unit = int(input("Enter units: "))

r1 = float(input("Rate for 0-100 units: "))
r2 = float(input("Rate for 101-300 units: "))
r3 = float(input("Rate for >300 units: "))

if unit <= 100:
    bill = unit * r1
elif unit <= 300:
    bill = (100 * r1) + ((unit - 100) * r2)
else:
    bill = (100 * r1) + (200 * r2) + ((unit - 300) * r3)

print("\n===== Bill Receipt =====")
print(f"Name   : {name}")
print(f"Units  : {unit}")
print(f"Rate1  : Rs.{r1}")
print(f"Rate2  : Rs.{r2}")
print(f"Rate3  : Ts.{r3}")
print(f"Total  : Rs.{bill:.2f}")
print("========================")
