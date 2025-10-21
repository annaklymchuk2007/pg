
def je_prvocislo(cislo):
    if cislo < 2:
        return False
    
    for cislo2 in range(2, int(cislo ** 0.5) + 1):
        if cislo % cislo2 == 0:
            return False
    
    return True




def vrat_prvocisla(maximum):
    maximum = int(maximum)
    if maximum < 2:
        return []

    prvocisla = []

    for cislo in range(2, maximum + 1):
        je_prvocisla = True
        for cislo2 in range(2, int(cislo ** 0.5) + 1):
            if cislo % cislo2 == 0:
                je_prvocisla = False
                break

        if je_prvocisla:
            prvocisla.append(cislo)

    return prvocisla

if __name__ == "__main__":
    print(je_prvocislo(1))
    print(je_prvocislo(2))
    print(je_prvocislo(3))
    print(je_prvocislo(100))
    print(je_prvocislo(101))

    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
    