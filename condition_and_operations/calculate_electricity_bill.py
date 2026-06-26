"""
=================================================
ELECTRICITY BILL CALCULATOR
=================================================

Problem Statement:
Write a Python program to calculate electricity bill.

-------------------------------------------------
Conditions:
1. First 100 units  -> ₹5 per unit
2. Next 100 units   -> ₹7 per unit
3. Above 200 units  -> ₹10 per unit


-------------------------------------------------
Input Example:
250

Output Example:
Total Bill = ₹1700

-------------------------------------------------
Hints:
Break the problem into multiple conditions.

=================================================
"""

# --- code is from here ---

units = int(input("Enter the number of electricity units used: "))

if units <= 100:
    bill = units * 5

elif units <= 200:
    first_100 = 100 * 5
    remaining = (units - 100) * 7
    bill = first_100 + remaining

else:
    first_100 = 100 * 5
    next_100 = 100 * 7
    extra = (units - 200) * 10
    bill = first_100 + next_100 + extra

print("\n=====Billing Details=====")
print(f"Total units used: {units}")
print(f"Total bill: Rs.{bill}") 
