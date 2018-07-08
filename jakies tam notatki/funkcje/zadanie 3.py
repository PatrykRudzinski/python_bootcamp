def liczba_znaków_pomiędzy(napis, znak_str='<', znak_stp='>'):
    suma = 0
    start = 0
    for i in napis:
        if i == znak_str:
            start += 1
        elif i == znak_stp:
            start -= 1
        elif start:
            suma += start
    return suma

def test_liczba_znaków_pomiędzy_znaki_podstawowe():
     assert liczba_znaków_pomiędzy('ala ma <kota> a kot ma ale') == 4

def test_liczba_znaków_pomiędzy_znaki_inne():
    assert liczba_znaków_pomiędzy('ala [kota [a kot]] ma [ale]', '[', ']') == 18

def test_liczba_znaków_pomiędzy_znaki_podstawowe_zagniezdzone():
    assert liczba_znaków_pomiędzy('a <a<a<a>>>') == 6
