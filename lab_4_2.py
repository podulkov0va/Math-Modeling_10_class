def mas(a):
    ''' функция для перемножения элементов массива
    '''
    b=1
    for i in range(0, len(a), 1):
        b=b*a[i]
    return b
a=range(1, 10, 1)
print(mas(a))
