import numpy as np
#Розмірність першої матриці.
n,m=int(input('Введіть кількість рядків 1 матриці: ')),\
    int(input('Введіть кількість стовчиків 2 матриці: '))

#Розмірність другої матриці.
p,r=int(input('Введіть кількість рядків 2 матриці: ')),\
    int(input('Введіть кількість стовпчиків 2 матриці: '))

#Ініціалізація двох матриць нулями.
A, B=np.zeros((n,m), dtype=int), np.zeros((p,r), dtype=int)
#Для кожного елемента стовпчиків та рядків матриць А, В\
#використаємо for.
for i in range(n):
    for j in range(m):
    #Перевірка, чи користувач дійсно ввів розміри матриць 3х3.
        if n==3 and m==3 and p==3 and r==3:
            print('Заповніть числами матриці А та В.')
            #Для кожної комірки матриць А та В користувач вводить\
            #числа.
            A[i,j]=int(input(f' A([{i+1}, {j+1}]): '))
            B[i,j]=int(input(f' B([{i+1}, {j+1}]): '))
    #Якщо користувач вибрав розміри матриць не 3 на 3, то print.
    if n!=3 or m!=3 and p!=3 or r!=3:
        print('Введіть розмірність 3 на 3 для двох матриць!')
    if n>3 or m>3 and p>3 or r>3:
        print('Введіть розмірність 3 на 3 для двох матриць!')
        

#Ініціалізуємо матрицю (поки нулями), яка буде результатом \
#множення двох матриць.
C=np.zeros((p, r), dtype=int)
F=0 #Тимчасова змінна, яка буде результатом множення стовпчика на рядок.
#Тут ми створимо ще одну, грубо кажучи, порожню матрицю та, у подальшому, \
#транспонуємо її. Зробимо ми це для зручності, адже після транспонування \
#можна буде перемножати не рядок першої матриці на стовпчик другої, а рядок\
#першої матриці на рядок другої. Результат буде індентичним.
T = np.zeros((p, r), dtype=int)
#Ще раз отримаємо доступ до кожного елемента матриць. Але тут ми \
#використовуємо for для елементів рядка першої матриці та стопчика \
#другої матриці.
for i in range(n):
    for j in range(r):
        #В першій стрічці ми транспонуємо матрицю В, як і зазначалося раніше.
        T[i,j]=B[j,i]
        F=A[i-2]*T[i-2] #Використовуємо тимчасову змінну для добутку \
        #РЯДКА на РЯДОК (так як друга матриця транспонована)
        #Та вже тут починаємо заповнювати кожну комірку нашої нової, утвореної\
        #нулями матриці.
        C[0,0]=F[i-2]+F[i-1]+F[i]#Елемент першого рядка, першого стопчика.
        F=A[i-2]*T[i-1]
        C[0,1]=F[i-2]+F[i-1]+F[i]
        F=A[i-2]*T[i]
        C[0,2]=F[i-2]+F[i-1]+F[i]
        F=A[i-1]*T[i-2]
        #Другий рядок матриці C.
        C[1,0]=F[i-2]+F[i-1]+F[i]
        F=A[i-1]*T[i-1]
        C[1,1]=F[i-2]+F[i-1]+F[i]
        F=A[i-1]*T[i]
        C[1,2]=F[i-2]+F[i-1]+F[i]
        F=A[i]*T[i-2]
        #Третій рядок матриці C.
        C[2,0]=F[i-2]+F[i-1]+F[i]
        F=A[i]*T[i-1]
        C[2,1]=F[i-2]+F[i-1]+F[i]
        F=A[i]*T[i]
        C[2,2]=F[i-2]+F[i-1]+F[i]

print('Результат добутку: ', C)

    