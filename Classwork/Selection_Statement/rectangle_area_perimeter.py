length =float(input("Enter the length of rectangle : "))
if length <= 0:
    exit("Invalid! length must be positive.")
width = float(input("Enter the width of rectangle : "))
if width <= 0:
    exit("Invalid! width must be positive.")
area = length * width
perimeter = 2 * (length + width)
print("Area  =", area)
print("Perimeter  =", perimeter)
