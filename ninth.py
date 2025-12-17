def dec_to_bin(cislo):
    """
    Prevede cislo na binarni reprezentaci.
    Cislo muze byt zadano jako str nebo int.
    """
    if isinstance(cislo, str):
        cislo = int(cislo)
    
    if cislo == 0:
        return "0"
    
    binary_digits = []
    
    while cislo > 0:
        binary_digits.append(str(cislo % 2))
        cislo = cislo // 2
    
    return ''.join(reversed(binary_digits))


def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"