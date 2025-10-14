
def cislo_text(cislo):
    num = int(cislo)

    if num < 10:
        slovnik_jednotky = [
        "nula", "jedna", "dva", "tri", "ctyri", "pet",
        "sest", "sedm", "osm", "devet"
    ]
        return slovnik_jednotky[num]
        
    elif num > 9 and num < 20:
        slovnik2 = [
        "deset", "jedenact", "dvanact", "trinact", "ctrnact", "patnact",
        "sestnact", "sedmnact", "osmnact", "devatenact"
    ]
        return slovnik2[num - 10]
        
    elif num < 100:
        slovnik_jednotky = [
        "nula", "jedna", "dva", "tri", "ctyri", "pet",
        "sest", "sedm", "osm", "devet"
    ]
        slovnik_desitky = [
         "dvacet", "tricet", "ctyricet",
         "padesat", "sedesat", "sedmdesat", "osmdesat", "devadesat"
    ]
        desitka = (num // 10) - 2
        jednotka = num % 10

        if jednotka == 0:
            return slovnik_desitky[desitka]
        else:
            return f"{slovnik_desitky[desitka]} {slovnik_jednotky[jednotka]}"
    
    if num == 100:
        return "sto" 


if __name__ == "__main__":
    cislo = input("Zadejte cislo: ")
    text = cislo_text(cislo)
    print(text)