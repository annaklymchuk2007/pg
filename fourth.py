def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):

    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    # Implementace pravidel pohybu pro různé figury zde.
    typ = figurka["typ"]
    pozice = figurka["pozice"]
    r1, s1 = pozice
    r2, s2 = cilova_pozice
   

    if not (1 <= r2 <= 8 and 1 <= s2 <= 8):
        return False

    if (r2, s2) in obsazene_pozice:
        return False

    dr, ds = abs(r2-r1), abs(s2-s1)

    if typ == "pěšec":
        return s1 == s2 and (r2-r1 == 1 or (r1 == 2 and r2 == 4 and (3, s1) not in obsazene_pozice))
    elif typ == "jezdec":
        return (dr == 2 and ds == 1) or (dr == 1 and ds == 2)
    elif typ == "věž":
        return (r1 == r2 or s1 == s2) and volna_cesta(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "střelec":
        return dr == ds and volna_cesta(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "dáma":
        return (r1 == r2 or s1 == s2 or ds == dr) and volna_cesta(pozice, cilova_pozice, obsazene_pozice)
    elif typ == "král":
        return dr <= 1 and ds <= 1 and (dr != 0 or ds != 0)
    return False

def volna_cesta(od, do, obsazene):
    r1, s1 = od 
    r2, s2 = do 

    if r1 == r2:
        krok_r = 0
    elif r2 > r1:
        krok_r = 1
    else:
        krok_r = -1

    if s1 == s2:
        krok_s = 0
    elif s2 > s1:
        krok_s = 1
    else:
        krok_s = -1

    r, s = r1 + krok_r, s1 + krok_s

    while (r, s) != (r2, s2):
        if (r, s) != (r2, s2):
            return False
        r += krok_r
        s += krok_s
        return True

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o dvě pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True