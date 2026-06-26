"""
## 3. Products Within Budget Report  *(Medium)*

=================================================
PRODUCTS WITHIN BUDGET REPORT
=================================================

Problem Statement:
You are given a LIST of TUPLES, where each
tuple represents a product:
        (product_name, price)

Write a Python program that builds a REPORT
DICTIONARY in the following form:

   {
     "within_budget":  [list of (name, price) tuples],
     "over_budget":    [list of (name, price) tuples],
     "categories":     {
                         "cheap":    set of names with price <  50,
                         "moderate": set of names with 50 <= price <= 200,
                         "costly":   set of names with price >  200
                       },
     "cheapest":       (name, price),
     "costliest":      (name, price)
   }

-------------------------------------------------
Input Example:
products = [
   ("Pen",    10),
   ("Book",   150),
   ("Bag",    500),
   ("Pencil", 5),
   ("Lamp",   300),
   ("Mug",    80),
]
budget = 200

Output Example:
{
  'within_budget': [('Pen',10), ('Book',150),
                    ('Pencil',5), ('Mug',80)],
  'over_budget':   [('Bag',500), ('Lamp',300)],
  'categories': {
      'cheap':    {'Pen', 'Pencil'},
      'moderate': {'Book', 'Mug'},
      'costly':   {'Bag', 'Lamp'}
  },
  'cheapest':  ('Pencil', 5),
  'costliest': ('Bag', 500)
}

-------------------------------------------------
Explanation:
Iterate once through the product list and
classify every item:
   price <  50  -> cheap
   50..200      -> moderate
   price > 200  -> costly
Compare each price to the budget to split it
into within/over budget. While iterating, also
remember the smallest and largest prices seen
so far to find the cheapest and costliest
products.
=================================================

"""
# --- code is from here ---

products = [
   ("Pen",    10),
   ("Book",   150),
   ("Bag",    500),
   ("Pencil", 5),
   ("Lamp",   300),
   ("Mug",    80),
]
budget = 200

rep = {
    "within_budget": [],
    "over_budget": [],
    "categories": {
        "cheap": set(),
        "moderate": set(),
        "costly": set()
    },
    "cheapest": None,
    "costliest": None
}

min_p = None
max_p = None

for name, price in products:
    if price <= budget:
        rep["within_budget"].append((name, price))
        
    else:
        rep["over_budget"].append((name, price))

    if price < 50:
        rep["categories"]["cheap"].add(name)
        
    elif price <= 200:
        rep["categories"]["moderate"].add(name)
        
    else:
        rep["categories"]["costly"].add(name)

    if min_p is None or price < min_p[1]:
        min_p = (name, price)

    if max_p is None or price > max_p[1]:
        max_p = (name, price)

rep["cheapest"] = min_p
rep["costliest"] = max_p

print(rep)
