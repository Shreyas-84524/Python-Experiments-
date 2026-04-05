#Shreyas Rajendra Shigwan, Roll no. 90, CSE (AIML)
#Exp 1.2 : Area Calculator
import math

def area_circle(radius):
    return math.pi * radius**2
def area_rectangles(length, width):
    return length * width
def area_triangle(base, height):
    return 1/2 * base * height
print("1. Area of the rectrangle")
print("2. Area of the traingle")
print("3. Area of the circle " )

choice = int(input("Enter your choice (1/2/3) = "))

if choice == 3:
    r = float(input("Enter the radius of circle = "))
    print("The area of the circle= ", area_circle(r))
elif choice == 1:
    l = float(input("Enter the length of rectangle = "))
    w = float(input("Enter the width of rectangle = "))
    print("The area of the rectangle =", area_rectangles(l, w))
elif choice == 2:
    b = float(input("Enter the base of triangle = "))
    h = float(input("Enter the height of triangle = "))
    print("The area of the triangle= ", area_triangle(b, h))
else:
    print("Invalid choice please choice your choice from (1/2/3)")