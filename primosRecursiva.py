'''
A função recursiva deve receber um número N > 1 (validar o input),
 e retornar todos os números primos até o número N. 
EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];
'''
def p(numero):
    if numero == 2:
        return [2]
    resposta = []
    count = 0
    for i in range(1,(numero//2)+1):
        if (numero // i) == (numero / i):
            count +=1
    resposta = p(numero-1)
    if count == 1:
        resposta.append(numero)
    return resposta
