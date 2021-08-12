from random import randint
numpc = randint(1,10)
print('Chute um número no intervalo de 1 até 10! Se quiser sair do programa, digite 0!\n')

# Enquanto o usuário não acertar ou desistir o laço de repetição continuara
while True:
    numjogador = int(input('Chute um número: '))

    if numjogador < 0 or numjogador > 10:
        print('Ops! O número que você digitou está fora do intervalo!')
    
    elif numjogador == 0:
        print('Você deveria continuar tentando! Mas muito obrigado por tentar!!')
        break

    elif numpc > numjogador:
        print('Eita! Você chutou baixo!')

    elif numpc < numjogador:
        print('Nossa! Você chuto alto!')

    elif numpc == numjogador:
        print('Parabéns!! Você acertou!')
        break
