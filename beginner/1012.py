# 1012 - Área

# Input > A (float), B (float), C (float)
# Example: 3.0 4.0 5.2

user_input = input().split(" ")

side_a = float(user_input[0])
side_b = float(user_input[1])
side_c = float(user_input[2])

triangle_area   = (side_a * side_c) / 2
circle_area     = 3.14159 * (side_c ** 2)
trapeze_area    = ((side_a + side_b) * side_c) / 2
square_area     = side_b ** 2
rectangle_area  = side_a * side_b

print("TRIANGULO: {:.3f}".format(triangle_area))
print("CIRCULO: {:.3f}".format(circle_area))
print("TRAPEZIO: {:.3f}".format(trapeze_area))
print("QUADRADO: {:.3f}".format(square_area))
print("RETANGULO: {:.3f}".format(rectangle_area))
