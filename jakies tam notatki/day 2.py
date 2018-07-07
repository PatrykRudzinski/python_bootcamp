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
#
# while 1:
#     word = input('Podaj słowo: ')
#     if "break" == word:
#         break
#     LIST_SAMO = ['a', 'e', 'i', 'o', 'u', 'y']
#     samogloski = 0
#
#     for i in LIST_SAMO:
#         samogloski += word.lower().count(i)
#     print(samogloski)
#
#     for i in LIST_SAMO:
#         x = word.lower().count(i)
#         print(f'Ilość samogłosek {i}: {x}')
##todo: text pomiędzy <>
# text = input('Podaj text: ')
# for i in range(len(text)):
#     if text[i] == "<":
#         start = i
#     elif text[i] == ">":
#         end = i
#         print((text[start+1:end]))
