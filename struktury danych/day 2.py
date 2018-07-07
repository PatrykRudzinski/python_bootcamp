##todo: zamiana najwiekszej i najmniejszej w liscie

# li = [2, 4, 6, 3, 5, 1, 8, 10, 11, 4, 564]
# minli = li[0]
# maxli = li[0]
# for i in li:
#     if i > maxli:
#         maxli = i
#     elif i < minli:
#         minli = i
# maxin = li.index(maxli)
# minin = li.index(minli)
# li[minin] = maxli
# li[maxin] = minli
# print(li)

##todo: zagniezdzanie list

# x = [[1,2,3], [4,5,6]]
#
# a = [1,2,3]
# b = [4,5,6]
#
# x = [a, b]
#
# print(x[0][2])
##todo:ctrl d zeby linnie dublowac

#copy vs deepcopy raw string

##todo:napisy

word = input('Podaj słowo: ')
list_samo = ['a', 'e', 'i', 'o', 'u', 'y']
samogloski = 0

for i in list_samo:
    samogloski += word.count(i)
print(samogloski)

for i in list_samo:
    x = word.count(i)
    print(f'Ilość samogłosek {i}: {x}')