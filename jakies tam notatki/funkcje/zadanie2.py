def wiecej_niz(napis, wiecej):
    ilosci = {}
    wynik = set()
    for l in napis:
        ilosci[l] = ilosci.get(l, 0) + 1
    for k, v in ilosci.items():
        if v > 3:
            wynik.add(k)
    return wynik


def test_wiecej_niz_string1():
    assert wiecej_niz('ala ma kota a kot ma ale', 3) == {'a', ' '}
    assert wiecej_niz('ala mmmma kota a kot ma ale', 3) == {'a', ' ', 'm'}
    assert wiecej_niz('ala mmmma kotttta a kot ma ale', 3) == {'a', ' ', 'm', 't'}