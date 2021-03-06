#у матриці 4*4, що задана користувачем замініть всі від’ємні елементи на 0.
import numpy as np #Імпортуємо бібліотеку NumPy
while True:
    while True:
        try:
            #Розмірність матриці задає користувач (4х4)
            n,m=int(input('Введіть кількість рядків: ')), \
                int(input('Введіть кількість стовпчиків: '))

            A=np.zeros((n,m), dtype=int) #Ініціалізуємо матрицю нулями.
            for i in range(n): #Для доступу до кожного елемента рядка і\
                for j in range(m): #стопчика використовуємо for.
                    if n==4 and m==4: #Перевірка на розмірність матриці.
                        #Заповнюємо кожну комірку матриці відповідним числом.
                        A[i,j]=int(input(f' [{i+1}, {j+1}]: '))
                        if A[i,j]<0: #Якщо елемент матриці від'ємний (менше нуля)\
                            A[i,j]=0 #то замінюємо його на 0.
            print(A)#Наша матриця уже із заміною від'ємних чисел на число 0.
            if n!=4 or m!=4: #Випадок, коли користувач ввів матрицю не 4 на 4.
                print('Введіть матрицю 4х4!')
                    
        except ValueError: #Щоб уникнути збудження ValueError, введіть число.
            print('Input numbers!! ')
        break

    #Чи бажаєте продовжити програму?
    result=input('Input "1" to continue, and other to exit: ')
    if result=='1':
        continue
    break
