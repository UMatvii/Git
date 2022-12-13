def potęga(lista1,lista2):
    L = []
    dl1 = len(lista1)
    dl2 = len(lista2)
    if dl1 == dl2:
        for i in range(dl1):
            L.append(lista1[i] ** lista2[i])

        return L

Lista1 = [1,4,5,6]
Lista2 = [5,6,8,2]
p = potęga(Lista1,Lista2)
print(p)