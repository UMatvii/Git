def znaki(string):
    słownik = {}
    for i in string:
        słownik[i] = słownik.get(i, 0) + 1
 #        if i in słownik:
 #           słownik[i] += 1
  #      else:
   #         słownik[i] = 1

    return słownik

result = znaki("znaki napisu")
print(result)
for w in sorted(result):
    print(f"{w}: {result[w]}")


