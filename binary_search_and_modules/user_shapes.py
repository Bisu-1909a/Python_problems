import shapes

from shapes import circle

from shapes.rectangle import rectangle_area

print(("circle",
       round(circle.circle_area, 5),
       round(circle.circle_perimeter, 4)))

print(("rectangle",
       rectangle_area,
       shapes.rectangle.rectangle_perimeter))

print(("triangle",
       shapes.triangle.triangle_area,
       shapes.triangle.triangle_perimeter))

areas = {
    "circle": round(circle.circle_area, 5),
    "rectangle": rectangle_area,
    "triangle": shapes.triangle.triangle_area
}

print()
print("Areas:", areas)
