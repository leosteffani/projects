'''
A função recursiva deve receber um numero N >= 0 (deve validar o input para a função), 
e retornar o valor correspondente desse número na sequência Fibonacci. 
EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.
'''
def fib(numero):
    if numero == 0:
        return 0
    if numero == 1:
        return 1
    return fib(numero-1) + fib(numero-2)
print(fib(6))
    