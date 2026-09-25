#Ex1
radius = float(input("Enter radius:"))
area = 3.14 * (radius ** 2)
print("Circle area = ", area)

#Ex2
Celsius = float(input("Enter temperature in Celsius? "))
Fahrenheit = 5 * Celsius
print(Celsius,"(C) =", Fahrenheit,"(F)")

#Ex3
import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number? "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is a NOT prime number")

#Ex4
def is_perfect(n):
    if n <= 0:
        return False
    total_sum = 0
    for i in range(1, n):
        if n % i == 0:
            total_sum += i
    return total_sum == n
num = int(input("Enter a number? "))
if is_perfect(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is a NOT perfect number")

#Ex5
colors = ["Blue", "Yellow", "Orange", "Red", "Black"]
user_color = input("What is your favorite color? ")
if user_color in colors:
    index = colors.index(user_color)
    print(f"Your colod is at index {index} in my list")
else:
    print("Sorry, I could not find your color")

#Ex6
range1 = list(range(0, 7))
range2 = list(range(1, 11, 3))
range3 = list(range(5, 0, -1))
range4 = list(range(6, -3, -2))
print("range1:", range1)
print("range2:", range2)
print("range3:", range3)
print("range4:", range4)

#Ex7
def remove_dollar_sign(s):
    return s.replace("$", "")

s = input("Enter the money amount:")
result = remove_dollar_sign(s)
print(result)

#Ex8
def extract_even(I):
    return [num for num in I if num % 2 == 0]

I = list(map(int, input("Enter the list: ").split()))
result = extract_even(I)
print(result)

#Ex9
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1,):
        result *= i
    return result
    
num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("This is a negative integer")
else:
    print(f"Factorial of {num} is: {factorial(num)}")

#Ex10
def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

num = int(input("Enter a number: "))
divisors = get_divisors(num)
print("Divisors :", divisors)

#Ex11
import math
def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

x1, y1 = map(float, input("First co-ordinate : ").split())
x2, y2 = map(float, input("Second co-ordinate: ").split())
p1 = (x1, y1)
p2 = (x2, y2)
distance = calculate_distance(p1, p2)
print("Distance :", distance)

#Ex12
def print_pattern(m, n):
    for i in range(m):
        if i == 0 or i == m - 1:
            print("* " * n)
        else:
            print("* " + " " * (2 * n - 3) + "*")

m = int(input("input m: "))
n = int(input("input n: "))
result = print_pattern(m, n)
print(result)
