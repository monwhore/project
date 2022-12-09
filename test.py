#Ганкин Ярослав

#1
n = int(input('Введите степень'))
i = 1
s = 2
k = 1
while (i <= n):
    k = k * s
    i += 1
print (k)

#2
n = int(input('Введите степень'))
k = int(input('Введите число'))
i = 1
s = 0
while (i <= n - 1):
    s =  k ** n
    i = i + 1
print (s)

#3
a = int(input('a = '))
n = int(input('n = ')) 
i = 1
result = 1
while (i <= n):
    result = result * (a + i)
    i += 1
    print (result)

#4
n = int(input('Enter n: '))
i = 1
factorial = 1
while i <= n:
    factorial *= i
    i += 1 
    print (factorial)

#5
a = int(input('Enter a: '))
i = 1 
result = 1
if a < 0 or a > 0:
    while(a < 0):
        print('введено недействительное число, введите действительное')
        a = int(input('Enter a: '))
    n = int(input('Enter n: '))  
    while (i <= n):
        result *= a * (a - i * n)
        i += 1
    print(result)