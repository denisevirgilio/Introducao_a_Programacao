print('Digite as notas do aluno. Para encerrar, digite -1.')

notas = []
while True:
    entrada = input('Digite uma nota: ')
    try:
        nota = float(entrada)
        if nota == -1:
            break
        elif 0 <= nota <= 10:
            notas.append(nota)
        else:
            print('Nota inválida! Digite um valor entre 0 e 10.')
    except ValueError:
        print('Entrada inválida! Por favor digite um número.')

if notas:
    media = sum(notas) / len(notas)
    print(f'A média do aluno é {media:.2f}')
else:
    print('Nenhuma nota válida foi inserida')