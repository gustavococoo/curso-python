primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))
if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior do que {segundo_valor=}')
elif primeiro_valor == segundo_valor:
    print(f'Os dois valores são iguais!')
else:
    print(f'{segundo_valor=} é maior do que {primeiro_valor=}')