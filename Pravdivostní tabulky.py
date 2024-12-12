def pravdivostni_tabulka_and():
    print("A B | A AND B")
    print("-------------")
    for A in [False, True]:
        for B in [False, True]:
            print(f"{int(A)} {int(B)} |   {int(A and B)}")


def pravdivostni_tabulka_or():
    print("A B | A OR B")
    print("------------")
    for A in [False, True]:
        for B in [False, True]:
            print(f"{int(A)} {int(B)} |  {int(A or B)}")


def pravdivostni_tabulka_not():
    print("A | NOT A")
    print("---------")
    for A in [True, False]:
        print(f"{int(A)} |  {int(not A)}")


def pravdivostni_tabulka_xor():
    print("A B | A XOR B")
    print("-------------")
    for A in [True, False]:
        for B in [True, False]:
            print(f"{int(A)} {int(B)} |   {int(A != B)}")


# Vytiskneme pravdivostní tabulky
pravdivostni_tabulka_and()
print()
pravdivostni_tabulka_or()
print()
pravdivostni_tabulka_not()
print()
pravdivostni_tabulka_xor()
