import random
def gra():
    y = 0
    x = random.randint(0,20)
    while True:
        y += 1
        liczba = int(input("Podaj pierwszą liczbę: "))
        if liczba == x:
            print("Gratulacja")
            return
        elif liczba > x:
            print("Wylosowana liczba jest mniejsza")
        else:
            print("Wylosowana liczba jest większa")

print(gra())