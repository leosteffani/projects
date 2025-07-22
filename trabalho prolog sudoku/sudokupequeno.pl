:- use_module(library(clpfd)). %biblioteca auxiliar
n(1). %possiveis valores para os numero
n(2).
n(3).
n(4).

maior(Ma,Me):- n(Ma),n(Me),Ma #> Me. %define que um numero deve ser maior que o outro
todosDiferentes([]). 
todosDiferentes([H|T]) :- not(member(H,T)), todosDiferentes(T). %testa se todos os elementos da lista sao diferentes
completa([X1, X2, X3, X4]) :- %completa a matriz, confirmando que todos os elementos passados são diferentes
	n(X1), n(X2), n(X3), n(X4),
	todosDiferentes([X1, X2, X3, X4]).


solucao(TabuleiroSolucao) :-
	TabuleiroSolucao = [ %matriz base da solucao
		[X11, X12, X13, X14],
		[X21, X22, X23, X24],
		[X31, X32, X33, X34],
		[X41, X42, X43, X44]
	],
%determina as relacoes entre os valores
    maior(X11,X12),
    maior(X14,X13),
    maior(X22,X21),
    maior(X23,X24),
    maior(X32,X31),
    maior(X34,X33),
    maior(X42,X41),
    maior(X44,X43),
    
    maior(X11,X21),
    maior(X22,X12),
    maior(X23,X13),
    maior(X14,X24),
    maior(X41,X31),
    maior(X42,X32),
    maior(X33,X43),
    maior(X34,X44),
    
    %completa as linhas
	completa([X11, X12, X13, X14]),
	completa([X21, X22, X23, X24]),
	completa([X31, X32, X33, X34]),
	completa([X41, X42, X43, X44]),
    %completa as colunas
	completa([X11, X21, X31, X41]),
	completa([X12, X22, X32, X42]),
	completa([X13, X23, X33, X43]),
	completa([X14, X24, X34, X44]),
    %completa os setores
	completa([X11, X12, X21, X22]),
	completa([X31, X32, X41, X42]),
	completa([X13, X14, X23, X24]),
	completa([X33, X34, X43, X44]).

