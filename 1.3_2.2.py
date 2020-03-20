#Бінарний алгоритм пошуку.
import numpy as np
import random
while True:
    A=np.zeros(8, dtype=int)
    x=3 #Елемент, який ми шукаємо у масиві.
    for i in range(8):
        A[i]=int(input('Введіть числа: '))#Користувач вводить числа для масиву.
    print(A)
    A=sorted(A)#Бінарний пошук вимагає сортування масиву.
    print('Ваш масив відсортовано: ', A)

    L=0 #Змінна, що відповідає за ліву частину масиву.
    R=len(A)-1 #Змінна, що відповідає за праву частину масиву.
    k=0 #Змінна, що буде серединою нашого масиву.
    flag=True
    counter=0

    while L<=R and flag:
        k=(L+R)//2
        if A[k]==x: #Якщо k-й елемент = x, то елемент знайдено.
            flag=False
        elif (A[k]<x): #Елемент знаходиться праворуч від середини, тому ми робимо\
            #зсув ліворуч на один елемент.
            L=k+1
        else: #Аналогічно і з елементом, що знаходиться зліва від середини.
            R=k-1
        counter+=1
    if flag: #Якщо істинність flag не змінилась у стрічці A[k]==x, то елемент не знайдено.
        print(f'Елемент {x} не знайдений')
    else:
        print(f'Елемент {x} був знайдений на позиції {k} за кількість порівнянь : {counter}')

    '''
    Елемент х шукається у масиві, поки зсув ліворуч/праворуч не дійде до потрібного
    елементу. Це відбувається до тих пір, поки A[k] не буде дорвінювати значенню х.
    Наприклад, дано лінійний масив A=[1,2,3,4,5]. Потрібно знайди елемент х=1.
    Середнім значенням у нас буде k. Отже, A[k]>x, тоді зсув відбувається праворуч.
    Якщо k-ий елемент все ще не дорівнює x, то відбувається ще один зсув ліворуч.
    Ось тут вже і співпало значення A[k] та x. Тому робимо висновок, що елемент х є
    у нашій послідовності.
    '''
    #Випадок, коли х не буде знайдено у масиві:
    B=np.array([1,3,5,7,9])
    m=4

    F=0 #Ліва частина
    G=len(A)-1 #Права частина
    l=0
    flag1=False

    while F<=G and not flag1:
        l=(F+L)//2
        if B[l]==m:
            flag1=True
        elif (B[l]<m):
            F=l+1
        else:
            G=l-1
    if not flag1:
        print('Елемент не знайдено')
    else:
        print(f'Елемент {m} був знайдений на позиції {l}')


    result = input('Хочете запустити заново? Якщо так - 1, ні - інше: ')
    if result == '1':
        continue
    else:
        break
        

    