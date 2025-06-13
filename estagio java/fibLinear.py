'''
A função linear deve receber um numero N >= 0 (deve validar o input para a função), 
e retornar o valor correspondente desse número na sequência Fibonacci. 
EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.
'''
def fib(numero):
    lista = [0,1]
    if numero == 0:
        return 0
    for i in range(2,numero+1):
        lista.append(lista[i-1] + lista[i-2])
    return lista.pop()
