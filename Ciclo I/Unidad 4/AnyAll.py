numeros = [2345,45,4576,568,5687,45,53,45323,46467,5678,-678,45,23,45]
impares = list(map(lambda num: num%2 != 0, numeros))
#print(impares)

#print(all(impares)) # False
#print(any(impares)) # True

#print(all([])) # True
#print(any([])) # False

numeros = [2345,45,4576,568,5687,45,0,45323,46467,5678,-678,45,23,45]
#print(any(numeros))
#print(all(numeros))

#info = [int(input()), input().split(' ')]
info = [6, ['345','457','687945','34','56','456', '5']]

print(
    'True'
    if all(
        list(map(
            lambda x: x>0,
            list(map(int, info[1]))
            )))
        and
        any(
            list(map(
                lambda x: x[0] == x[1] or x[0] == '5',
                list(zip(
                    info[1],
                    list(map(
                        lambda x: x[-1:(len(x)+1)*-1:-1],
                        info[1])))))))
    else 'False'
    )

print('\nAnalisis\n')

# ALL
print('Parte del ALL')
print(list(map(
            lambda x: x>0,
            list(map(int, info[1]))
            )))

print(all(list(map(
            lambda x: x>0,
            list(map(int, info[1]))
            ))))

# ANY
print('\nParte del ANY')
print(list(map(
    lambda x: x[-1:(len(x)+1)*-1:-1],
    info[1])))

print(list(zip(
    info[1],
    list(map(
        lambda x: x[-1:(len(x)+1)*-1:-1],
        info[1])))))

print( list(map(
                lambda x: x[0] == x[1] or x[0] == '5',
                list(zip(
                    info[1],
                    list(map(
                        lambda x: x[-1:(len(x)+1)*-1:-1],
                        info[1])))))))
        
print(any( list(map(
                lambda x: x[0] == x[1] or x[0] == '5',
                list(zip(
                    info[1],
                    list(map(
                        lambda x: x[-1:(len(x)+1)*-1:-1],
                        info[1]))))))))