numbers = []
n = int(input("Ile liczb chcesz wprowadzić: "))
for numer in range(n):
    komunikat = f"Podaj liczbę nr {numer+1}:"
    numbers.append(int(input(komunikat)))
print("Wprowadzone liczby:", numbers)

x = 0
i = 0
while i <= n:
    x = x + numbers[i]
    print(numbers[i])
    print(x)
    i = i + x
    print(i)
print("Suma liczb wynosi", i)


x = 0
i = 0
while i < n:
    x = x + numbers[i]
    i = i + 1
x = x / n
komunikat = f"Średnia liczb wynosi {x}"
print(komunikat)