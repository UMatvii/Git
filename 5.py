def dodawanie(liczba1, liczba2):
    wynik = liczba1 + liczba2
    return  wynik
def odejmowanie(liczba1,liczba2):
    wynik = liczba1 - liczba2
    return wynik
def mnożenie(liczba1, liczba2):
    wynik = liczba1 * liczba2
    return wynik
def dzielenie(liczba1,liczba2):
    if liczba2 != 0:
        wynik = liczba1 / liczba2
    return wynik

słownik = {'+': dodawanie, "-": odejmowanie, "*": mnożenie, "/": dzielenie}
liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))
działanie = input("Podaj rodzaj działania(+, -, *, /): ")
słownik[działanie](liczba1,liczba2)
print(słownik[działanie](liczba1,liczba2))