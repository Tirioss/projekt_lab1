print("Hello, Git")

def przywitaj(imie):
    print("Witaj", imie)

print("Podaj imie: ")
imie = input()

przywitaj(imie)

def loguj():
    print("Podaj haslo")
    haslo = input()
    if haslo == "malpa":
        print("Poprawne haslo")
    else: print("Niepoprawne haslo")
loguj()