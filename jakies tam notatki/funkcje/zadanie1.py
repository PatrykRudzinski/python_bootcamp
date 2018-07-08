def czy_jest_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba%i == 0:
            return False
        if i > round(liczba/2)+1:
            return True


def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert czy_jest_pierwsza(11) == True

def test_czy_jest_pierwsza_dla_liczby_niepierwszej():
    assert czy_jest_pierwsza(4) == False
    assert czy_jest_pierwsza(15) == False