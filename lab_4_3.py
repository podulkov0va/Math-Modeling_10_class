def mekh_energy(m, V, H ):
    ''' Функция, определяющая полную механическую энергию
    '''
    from phconst import g
    E = m*g*H + m*V**2/2
    return E
print(mekh_energy(10, 30, 10))

