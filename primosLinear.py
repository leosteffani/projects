'''
A função linear deve receber um número N > 1 (validar o input),
 e retornar todos os números primos até o número N. 
EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];
'''
def p(numero):
    resposta = [2]
    for j in range(numero,2,-1):
        count = 0
        for i in range(1,(j//2)+1):
            if (j // i) == (j / i):
                count +=1
        if count ==1:
            resposta.insert(1,j)
    return resposta
