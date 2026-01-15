import sys

def spocitej_statistiku(text):
    pocet_radku = 0
    pocet_slov = 0
    pocet_znaku = 0

    if text == "":
        return 0, 0, 0

    pocet_radku = text.count("\n") + 1
    pocet_slov = len(text.split())
    pocet_znaku = len(text)

    return pocet_radku, pocet_slov, pocet_znaku


def test_spocitej_statistiku():
    assert spocitej_statistiku("Ahoj svet\nToto je test.") == (2, 5, 23)
    assert spocitej_statistiku("") == (0, 0, 0)
    assert spocitej_statistiku("Jediny radek bez novych radku") == (1, 5, 29)
    assert spocitej_statistiku("Prvni radek\nDruhy radek\nTreti radek") == (3, 6, 35)


if __name__ == "__main__":
    try:

        vstupni_soubor = 'data.txt'
        vystupni_soubor = 'statistika.txt'

        with open(vstupni_soubor, 'r', encoding='utf-8') as f:
            obsah = f.read()
    
        pocet_radku, pocet_slov, pocet_znaku = spocitej_statistiku(obsah)

        with open(vystupni_soubor, 'w', encoding='utf-8') as f:
            f.write(f"Pocet radku: {pocet_radku}\n")
            f.write(f"Pocet slov: {pocet_slov}\n")
            f.write(f"Pocet znaku: {pocet_znaku}\n")

        # volitelne info pro uzivatele
        print("Statistika byla ulozena do souboru", vystupni_soubor)

    except FileNotFoundError:
        print("Vstupni soubor neexistuje")
    except Exception:
        print("Doslo k chybe pri praci se souborem")