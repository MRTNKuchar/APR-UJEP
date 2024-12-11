def bubble_sort_while(seznam):
    n = len(seznam)
    vymena = True  # Příznak, zda došlo k výměně během iterace
    while vymena:
        vymena = False  # Na začátku iterace předpokládáme, že k výměně nedojde
        for i in range(n - 1):
            if seznam[i] > seznam[i + 1]:
                # Prohození prvků
                seznam[i], seznam[i + 1] = seznam[i + 1], seznam[i]
                vymena = True  # Nastavíme příznak, že došlo k výměně
        n -= 1  # Snižujeme rozsah, protože poslední prvek je již seřazený
    return seznam

# Příklad použití
data = [64, 34, 25, 12, 22, 11, 90]
serazene = bubble_sort_while(data)
print("Seřazený seznam:", serazene)


