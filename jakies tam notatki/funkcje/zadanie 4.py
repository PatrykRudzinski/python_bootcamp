def formatuj(*args, **kwargs):
    lista = []
    wynik =''
    for i in args:
        for k, v in kwargs.items():
            if f'${k}' in i:
                lista.append(i.replace(f'${k}',str(v)))
    for i in lista:
        if lista.index(i) == len(lista)-1:
            wynik += i
            break
        wynik += i + '\n'
    return wynik
    # form = []
    # form_temp=[]
    # wynik = ''
    # for i in args:
    #     for k, v in kwargs.items():
    #         try:
    #             form_temp = i.split('$'+k)
    #             form.append(form_temp[0] + str(v) + form_temp[1])
    #         except:
    #             continue
    #
    # for i in form:
    #     if form.index(i) == len(form)-1:
    #         wynik += i
    #         break
    #     wynik += i + '\n'
    #
    # return wynik
print(formatuj('koszt $cena PLN','kwota $cena brutto', 'blabla $volvo blabla', cena=10, volvo=25))
def test_formatuj_podstawowy():
    assert formatuj('koszt $cena PLN','kwota $cena brutto', cena=10) == 'koszt 10 PLN\nkwota 10 brutto'
def test_formatuj_wiecej_kluczy():
    assert formatuj('koszt $cena PLN','kwota $cena brutto', 'blabla $volvo blabla', cena=10, volvo=25) == 'koszt 10 PLN\nkwota 10 brutto\nblabla 25 blabla'