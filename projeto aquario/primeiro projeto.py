from time import sleep
print(
    '\033[1:33m Olá, me chamo DORY e vou te ajudar a montar um aquário lindo e saudável!\033[m')
sleep(3)
print(
    '\033[1mVamos coletar algumas informações...\033[m \n')
sleep(2)
medida1 = int(input('\033[4mQual a largura do seu aquário:'))
medida2 = int(input('\033[4mQual a profundidade do seu aquário:'))
medida3 = int(input('Qual a altura do seu aquário:\033[m'))
litragem = (medida3 * medida2 * medida1) / 1000
print('Seu aquário tem \033[1:31m{}\033[m litros'.format(litragem))
sleep(1)
for c in range(1):
    DOCE = 0
    SALGADO = 0
    usuario = 0
    tipoaquario = str(input('\n QUAL O TIPO DO SEU AQUÁRIO? \033[1:34m[SALGADO]\033[m ou \033[1:32m[DOCE]\033[m \n')).upper().strip()
    sleep(1)
while usuario != 4:
    sleep(1)
    if tipoaquario == 'SALGADO':
        usuario = int(input('Escolha uma das opções abaixo para saber mais...\n\n'
        '[1] Condicionador PRIME\n'
        '[2]Ativado Biológico STABILITY\n'
        '[3]PH ideal para o seu aquário\n'
        '[4]FIM DO PROGRAMA: \n >>>  '))
        prime = 1
        stability = 2
        ph = 3
        if usuario == 1:
            doseprime = litragem // 2
            print('\033[1:34m Você vai precisar adcionar {:.0f} gotas de prime à água do seu aquário\033[m \n\n'.format(doseprime))
            sleep(2)
        elif usuario == 2:
            dosestability = litragem // 8
            dosestability2 = dosestability // 2
            print('\033[1:34mVocê vai precisar de {:.0f}ml de STABILITY no primeiro dia...\033[m'.format(dosestability))
            print('\033[1:34me {:.0f}ml de STABILITY nos 8 dias seguintes!\033[m \n\n'.format(dosestability2))
            sleep(2)
        elif usuario == 3:
            print('\033[1:34mO PH ideal para aquário marinho é entre 7.8 e 8.4 e a temperatura de aproximadamente 26ºC\033[m \n\n')
            sleep(2)
        elif usuario == 4:
            sleep(1)
            print('FIM DO PROGRAMA, VOLTE SEMPRE QUE PRECISAR\n\n')
    if tipoaquario == 'DOCE':
        usuario = int(input('Escolha uma das opções abaixo para saber mais...\n'
         '[1] Condicionador PRIME\n'
         '[2]Ativado Biológico STABILITY\n'
         '[3]PH ideal para o seu aquário\n'
         '[4]FIM DO PROGRAMA: \n >>>  '))
        prime = 1
        estabilidade = 2
        ph = 3
        if usuario == 1:
            doseprime = litragem // 2
            print('\033[1:32mVocê vai precisar adicionar {:.0f} gotas de prime à água do seu protetor\033[m \n\n'.format(doseprime))
            sleep(2)
        elif usuario == 2:
            dosestability = litragem // 8
            dosestability2 = dosestability // 2
            print('\033[1:32mVocê vai precisar de {:.0f}ml de STABILITY no primeiro dia...\033[m \n'.format(dosestability))
            print('\033[1:32me {:.0f}ml de STABILITY nos 8 dias seguintes!\033[m \n\n'.format(dosestability2))
            sleep(2)
        elif usuario == 3:
            print('\033[1:32m Aquário de água doce respeitam 3 faixas de PH: \n '
                  '6.2 a 6.8: Quer dizer se seu PH está ÁCIDO\n'
                  '6.8 a 7.2: Quer dizer que seu PH está NEUTRO\n'
                  '7.2 a 7.6: Quer dizer que seu PH está ALCALINO\033[m')
            sleep(2)
        elif usuario == 4:
            sleep(2)
            print('FIM DO PROGRAMA, VOLTE SEMPRE QUE PRECISAR')