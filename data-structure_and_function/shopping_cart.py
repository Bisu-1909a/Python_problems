"""
## 5. Shopping Cart Calculator  *(Hard)*

=================================================
SHOPPING CART CALCULATOR
=================================================

Problem Statement:
Build a small shopping cart system using THREE
Python FUNCTIONS that use *args, **kwargs,
and the core data structures (list, tuple,
dictionary, set).

   1. add_items(cart, *items, **quantities)
        - cart   -> dictionary {item_name: qty}
        - *items -> item names to add with a
                    default quantity of 1
        - **quantities -> item names with an
                    explicit quantity
        - update the cart in place AND return it

        add_items(cart, "pen", "apple", book=2, banana=5)
        cart -> {'pen': 1, 'apple': 1, 'book': 2, 'banana': 5}

   2. cart_summary(cart, prices)
        - cart   -> dictionary {item_name: qty}
        - prices -> dictionary {item_name: price}
        - return a TUPLE of:
            (list_of_line_items, total_amount)
          where each line item is a tuple:
            (name, quantity, line_total)
        
        line_items, total = cart_summary(cart, prices)
        line_items ->
          [('pen', 1, 10), ('apple', 1, 30),
           ('book', 2, 300), ('banana', 5, 50)]
        total -> 390

   3. apply_discounts(total, **discounts)
        - total -> the cart total amount
        - **discounts -> named percentage
                         discounts, e.g.
                         festive=10, member=5
        - apply EACH discount sequentially on
          the running total and return a tuple:
            (final_amount, set_of_applied_names)

        final, applied = apply_discounts(total, festive=10, member=5)
        390 - 10% = 351
        351 -  5% = 333.45
        final   -> 333.45
        applied -> {'festive', 'member'}

-------------------------------------------------
Instructions:
1. Implement all three functions.
2. Use only:
   - list, tuple, dictionary, set
   - for loops
   - *args, **kwargs
3. Do NOT use:
   - any external libraries
   - comprehensions
   - lambda / map / filter / reduce
4. Demonstrate the full flow:
   - start with an empty cart
   - call add_items()
   - call cart_summary() with a prices dict
   - call apply_discounts() with at least two
     named discounts
   - print every result.

-------------------------------------------------
Input Example:
prices = {
   "pen": 10, "book": 150, "apple": 30, "banana": 10
}


Output Example:
Cart: {'pen': 1, 'apple': 1, 'book': 2, 'banana': 5}
Line Items: [('pen', 1, 10), ('apple', 1, 30),
             ('book', 2, 300), ('banana', 5, 50)]
Total: 390
Final Amount: 333.45
Applied Discounts: {'festive', 'member'}

-------------------------------------------------
Explanation:
- add_items merges *items (default qty 1) and
  **quantities into the cart dictionary.
- cart_summary multiplies quantity by price
  for every cart entry, builds a list of tuple
  line items, and returns it along with the
  grand total.
- apply_discounts walks through **discounts
  with a for loop, subtracts each percentage
  from the running total, and tracks the names
  of applied discounts in a set.
=================================================

"""
# --- code is from here ---

def add_items(cart, *items, **qty):
    for item in items:
        cart[item] = cart.get(item, 0) + 1

    for item in qty:
        cart[item] = cart.get(item, 0) + qty[item]
    return cart


def cart_summary(cart, prices):
    lines = []
    total = 0

    for item in cart:
        q = cart[item]
        p = prices[item]
        amount = q * p

        lines.append((item, q, amount))
        total += amount
    return (lines, total)


def apply_discounts(total, **disc):
    final = total
    applied = set()

    for name in disc:
        final = final - (final * disc[name] / 100)
        applied.add(name)
    return (final, applied)

cart = {}

add_items(cart, "pen", "apple", book=2, banana=5)

print("Cart:", cart)

prices = {
    "pen": 10,
    "book": 150,
    "apple": 30,
    "banana": 10
}

lines, total = cart_summary(cart, prices)

print("Line Items:", lines)
print("Total:", total)

final, applied = apply_discounts(
    total,
    festive=10,
    member=5
)

print("Final Amount:", final)
print("Applied Discounts:", applied)
