name = input("Podaj swoje imie: ")
year = input("Podaj swój rok urodzenia: ")

age = 2021 - int(year)
print(age)

print("Użytkownik: " + name + " jest w wieku " + F'{age}' + " lat")
