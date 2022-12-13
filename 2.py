def sum_of_values(słownik):
    suma = 0
    for i in słownik.values():
        suma += i
    return suma


x = sum_of_values({'data1':-1, 'data2':-6, 'data3':2})
print(x)
