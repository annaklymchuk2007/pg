def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    bin_str = str(binarni_cislo)
    
    dec_hodnota = 0
    delka = len(bin_str)
    
    for i in range(delka):
        bit = int(bin_str[i])
        pozice = delka - i - 1
        dec_hodnota += bit * (2 ** pozice)
    
    return dec_hodnota


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128



if __name__ == "__main__":
    test_bin_to_dec()
    print("spravne")