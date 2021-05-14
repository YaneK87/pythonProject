import math

print("Równanie w postaci a*x**2 + b*x + c == 0")
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))


delta = (b ** 2) - (4 * a * c)
print("Delta wynosi", delta)

if delta == 0:
    x_0 = (-b)/(2*a)
    print("delta ma jedno miejsc zerowe i wynosi", x_0)

elif delta > 0:
    x_1 = (-b - math.sqrt(delta) / (2 * a))
    x_2 = (-b + math.sqrt(delta) / (2 * a))
    print("delta ma dwa miejsca zerowe i wynosi", x_1, "i", x_2)

else:
    print("Brak Rozwiązań")
