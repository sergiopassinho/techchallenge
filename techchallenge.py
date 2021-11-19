expressao = str(input('Digite a expressão: '))

if expressao:
    count = 0
    for i in expressao:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
            if count < 0:
                break    
    if count == 0:
        print('correct')
    else:
        print('incorrect')

