def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    
    typ_figurky = figurka["typ"]
    aktualni_pozice = figurka["pozice"]
    aktualni_radek, aktualni_sloupec = aktualni_pozice
    cilovy_radek, cilovy_sloupec = cilova_pozice
    
    if (cilovy_radek < 1 or cilovy_radek > 8 or 
        cilovy_sloupec < 1 or cilovy_sloupec > 8):
        return False
    
    if cilova_pozice in obsazene_pozice:
        return False
    
    if typ_figurky == "pěšec":
        return _je_tah_mozny_pesec(aktualni_pozice, cilova_pozice, obsazene_pozice)
    
    elif typ_figurky == "jezdec":
        return _je_tah_mozny_jezdec(aktualni_pozice, cilova_pozice)
    
    elif typ_figurky == "věž":
        return _je_tah_mozny_vez(aktualni_pozice, cilova_pozice, obsazene_pozice)
    
    elif typ_figurky == "střelec":
        return _je_tah_mozny_strelec(aktualni_pozice, cilova_pozice, obsazene_pozice)
    
    elif typ_figurky == "dáma":
        return _je_tah_mozny_dama(aktualni_pozice, cilova_pozice, obsazene_pozice)
    
    elif typ_figurky == "král":
        return _je_tah_mozny_kral(aktualni_pozice, cilova_pozice)
    
    else:
        return False


def _je_tah_mozny_pesec(aktualni_pozice, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda může pěšec provést daný tah.
    """
    aktualni_radek, aktualni_sloupec = aktualni_pozice
    cilovy_radek, cilovy_sloupec = cilova_pozice
    
    if cilovy_sloupec != aktualni_sloupec:
        return False
    
    rozdil_radku = cilovy_radek - aktualni_radek
    
    if rozdil_radku == 1:
        return cilova_pozice not in obsazene_pozice
    
    if rozdil_radku == 2 and aktualni_radek == 2:
        mezilehla_pozice = (aktualni_radek + 1, aktualni_sloupec)
        if mezilehla_pozice not in obsazene_pozice:
            return True
    
    return False


def _je_tah_mozny_jezdec(aktualni_pozice, cilova_pozice): 

    aktualni_radek, aktualni_sloupec = aktualni_pozice
    cilovy_radek, cilovy_sloupec = cilova_pozice
    
    rozdil_radku = abs(cilovy_radek - aktualni_radek)
    rozdil_sloupcu = abs(cilovy_sloupec - aktualni_sloupec)
    
    return (rozdil_radku == 2 and rozdil_sloupcu == 1) or (rozdil_radku == 1 and rozdil_sloupcu == 2)


def _je_tah_mozny_vez(aktualni_pozice, cilova_pozice, obsazene_pozice):

    aktualni_radek, aktualni_sloupec = aktualni_pozice
    cilovy_radek, cilovy_sloupec = cilova_pozice
    
    if aktualni_radek != cilovy_radek and aktualni_sloupec != cilovy_sloupec:
        return False
    
    if aktualni_radek == cilovy_radek:
        start = min(aktualni_sloupec, cilovy_sloupec) + 1
        end = max(aktualni_sloupec, cilovy_sloupec)
        for sloupec in range(start, end):
            if (aktualni_radek, sloupec) in obsazene_pozice:
                return False
    else:
        start = min(aktualni_radek, cilovy_radek) + 1
        end = max(aktualni_radek, cilovy_radek)
        for radek in range(start, end):
            if (radek, aktualni_sloupec) in obsazene_pozice:
                return False
    
    return True


def _je_tah_mozny_strelec(aktualni_pozice, cilova_pozice, obsazene_pozice):

    aktualni_radek, aktualni_sloupec = aktualni_pozice
    cilovy_radek, cilovy_sloupec = cilova_pozice
    
    if abs(cilovy_radek - aktualni_radek) != abs(cilovy_sloupec - aktualni_sloupec):
        return False
    
    krok_radek = 1 if cilovy_radek > aktualni_radek else -1
    krok_sloupec = 1 if cilovy_sloupec > aktualni_sloupec else -1
    
    vzdalenost = abs(cilovy_radek - aktualni_radek)
    for i in range(1, vzdalenost):
        radek = aktualni_radek + i * krok_radek
        sloupec = aktualni_sloupec + i * krok_sloupec
        if (radek, sloupec) in obsazene_pozice:
            return False
    
    return True


def _je_tah_mozny_dama(aktualni_pozice, cilova_pozice, obsazene_pozice):

    return (_je_tah_mozny_vez(aktualni_pozice, cilova_pozice, obsazene_pozice) or
            _je_tah_mozny_strelec(aktualni_pozice, cilova_pozice, obsazene_pozice))


def _je_tah_mozny_kral(aktualni_pozice, cilova_pozice):

    aktualni_radek, aktualni_sloupec = aktualni_pozice
    cilovy_radek, cilovy_sloupec = cilova_pozice
    
    rozdil_radku = abs(cilovy_radek - aktualni_radek)
    rozdil_sloupcu = abs(cilovy_sloupec - aktualni_sloupec)
    
    return rozdil_radku <= 1 and rozdil_sloupcu <= 1 and (rozdil_radku != 0 or rozdil_sloupcu != 0)


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