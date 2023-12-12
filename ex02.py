nome = str(input('Qual o seu nome? '))
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2
print(f'{nome} seu Índice de Massa Corporal é: {imc:.2f}')