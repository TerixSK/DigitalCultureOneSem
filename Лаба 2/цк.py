import numpy
import numpy as np
from PIL import Image
image = Image.open('палец.jpg')
image = image.convert('L') # Перевод картинки в чёрно-белое
image.save("палец чб.jpg") # Сохранение картинки для работы
imgp = numpy.array(image)
imgp = imgp[64] # Расчёт средней строки
for i in range(128): # Квантования
    imgp[i] = round(imgp[i] // 20) * 20
for i in range(128): # Вывод значений
    print(imgp[i], end=' ')
print()
print() # Отступ
for i in range(128): #Кодирование равномерным кодом
    if imgp[i] == 0:
        print('0000', end='')
    if imgp[i] == 20:
        print('0001', end='')
    if imgp[i] == 40:
        print('0010‬', end='')
    if imgp[i] == 60:
        print('0011', end='')
    if imgp[i] == 120:
        print('0100‬', end='')
    if imgp[i] == 160:
        print('0101', end='')
    if imgp[i] == 180:
        print('0110', end='')
    if imgp[i] == 200:
        print('0111', end='')
    if imgp[i] == 220:
        print('1000', end='')
    if imgp[i] == 240:
        print('1001', end='')
print()
print() # Отступ
print()
print() # Отступ
for i in range(128): #Кодирование методом Шеннона
    if imgp[i] == 0:
        print('10', end='')
    if imgp[i] == 20:
        print('111110', end='')
    if imgp[i] == 40:
        print('1111111', end='')
    if imgp[i] == 60:
        print('111101', end='')
    if imgp[i] == 120:
        print('1111110', end='')
    if imgp[i] == 160:
        print('111100', end='')
    if imgp[i] == 180:
        print('11101', end='')
    if imgp[i] == 200:
        print('11101', end='')
    if imgp[i] == 220:
        print('110', end='')
    if imgp[i] == 240:
        print('0', end='')
print()
print() # Отступ
print()
print() # Отступ
for i in range(128): #Кодирование методом Хаффмана
    if imgp[i] == 0:
        print('11', end='')
    if imgp[i] == 20:
        print('011000', end='')
    if imgp[i] == 40:
        print('0110100', end='')
    if imgp[i] == 60:
        print('011001', end='')
    if imgp[i] == 120:
        print('0110101', end='')
    if imgp[i] == 160:
        print('011011', end='')
    if imgp[i] == 180:
        print('01110', end='')
    if imgp[i] == 200:
        print('01111', end='')
    if imgp[i] == 220:
        print('010', end='')
    if imgp[i] == 240:
        print('0', end='')
print()
print() # Отступ
print()
print() # Отступ
for i in range(128): #Резерв
    if imgp[i] == 0:
        print('0', end='')
    if imgp[i] == 20:
        print('1', end='')
    if imgp[i] == 40:
        print('2', end='')
    if imgp[i] == 60:
        print('3', end='')
    if imgp[i] == 120:
        print('4', end='')
    if imgp[i] == 160:
        print('5', end='')
    if imgp[i] == 180:
        print('6', end='')
    if imgp[i] == 200:
        print('7', end='')
    if imgp[i] == 220:
        print('8', end='')
    if imgp[i] == 240:
        print('9', end='')
print()
print() # Отступ
for i in range(127): # Сортировка
    for j in range(127-i):
        if imgp[j] > imgp[j+1]:
            imgp[j], imgp[j+1] = imgp[j+1], imgp[j]
for i in range(128):
    print(imgp[i], end=' ')
print()
print() # Отступ

#k = 0
#for i in range(128):
#    if imgp[i] == 240:
#        k+=1
#print()
#print()
#print(k)
