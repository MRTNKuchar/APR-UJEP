import random

# Slovník pro pravidla hry: co poráží co
rules = {
    "kámen": ["nůžky", "ještěr"],
    "nůžky": ["papír", "ještěr"],
    "papír": ["kámen", "spock"],
    "spock": ["nůžky", "kámen"],
    "ještěr": ["papír", "spock"]
    }

# Funkce pro určení výsledku
def vyhodnot_tah(hrac, pocitac):
    if hrac == pocitac:
        return "Remíza!"
    elif pocitac in rules[hrac]:
        return "Vyhrál jsi"
    else:
        return "Počítač vyhrál"

#zadání počátečních hodnot pro výsledky
sk_pc = 0
sk_pl= 0
rem = 0

# Hlavní smyčka hry
def hra():
    tahy = list(rules.keys())  # Možné tahy: kámen, nůžky, papír, Spock, ještěr
    print("Vítej ve hře Kámen, Nůžky, Papír, spock, Ještěr!")
    print("Napiš 'kámen', 'nůžky', 'papír', 'spock'  nebo 'ještěr'. Jestli nechceš hrát tak napiš 'konec'.\n")
    
    while True:
        global sk_pc, sk_pl, rem
        # Hráčův tah
        hrac_tah = input("Tvůj tah: ").lower().strip()
        
        if hrac_tah == "konec":
            print("Hra ukončena. Díky za hraní!")
            break
        
        if hrac_tah not in tahy:
            print("Neplatný tah. Zkus to znovu.")
            continue
        
        # Počítačův tah
        pocitac_tah = random.choice(tahy)
        print(f"Počítač zvolil: {pocitac_tah}")
        
        # Vyhodnocení výsledku a zapsání skóre
        vysledek = vyhodnot_tah(hrac_tah, pocitac_tah)
        if vysledek == "Vyhrál jsi":
            print("Vyhrál jsi")
            sk_pl += 1
        elif vysledek == "Počítač vyhrál":
            print("Počítač vyhrál")
            sk_pc += 1
        elif vysledek == "Remíza!":
            print("Remíza")
            rem += 1

        #zobrazení skóre
        print(f"Vysledky jsou : remízy {rem}, výhry počítače {sk_pc}, tvoje výhry {sk_pl}")



# Spuštění hry
hra()
