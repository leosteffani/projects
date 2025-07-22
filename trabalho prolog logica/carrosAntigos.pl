%cria todas as possibilidades de cada tipo
cor(amarelo).
cor(branco).
cor(verde).
cor(vermelho).
cor(azul).

ano(1950).
ano(1955).
ano(1960).
ano(1965).
ano(1970).

montadora(chevrolet).
montadora(ford).
montadora(mercedes).
montadora(porsche).
montadora(volkswagen).

dono(aguiar).
dono(glenn).
dono(harley).
dono(ponce).
dono(thales).

km(80).
km(100).
km(140).
km(190).
km(210).

placa(a).
placa(b).
placa(c).
placa(d).
placa(e).


%X está à ao lado de Y
aoLado(X,Y,Lista) :- nextto(X,Y,Lista);nextto(Y,X,Lista).
                       
%X está à esquerda de Y (em qualquer posição à esquerda)
aEsquerda(X,Y,Lista) :- nth0(IndexX,Lista,X), 
                        nth0(IndexY,Lista,Y), 
                        IndexX < IndexY.
                        
%X está à direita de Y (em qualquer posição à direita)
aDireita(X,Y,Lista) :- aEsquerda(Y,X,Lista). 

%Y esta entre X e Z
entre(X,Y,Z,Lista) :- aEsquerda(X,Y,Lista), 
                        aDireita(Z,Y,Lista).

%X está no canto se ele é o primeiro ou o último da lista
noCanto(X,Lista) :- last(Lista,X).
noCanto(X,[X|_]).

%verifica se todos os elementos da lista são diferentes
todosDiferentes([]).
todosDiferentes([H|T]) :- not(member(H,T)), todosDiferentes(T).

%para as regraa de "exatamente a esquerda" ou "exatamente a direita" utilizei o comando nextto()

solucao(ListaSolucao) :- 

    ListaSolucao = [
        carro(Cor1, Ano1, Montadora1, Dono1, Placa1, Km1),
        carro(Cor2, Ano2, Montadora2, Dono2, Placa2, Km2),
        carro(Cor3, Ano3, Montadora3, Dono3, Placa3, Km3),
        carro(Cor4, Ano4, Montadora4, Dono4, Placa4, Km4),
        carro(Cor5, Ano5, Montadora5, Dono5, Placa5, Km5)
    ],

    %O carro da placa CCC-3333 está em algum lugar entre o carro Branco e o carro da placa DDD-4444, nessa ordem.
    entre(carro(branco, _, _, _, _,_),carro(_,_, _, _, c, _),carro(_, _, _,_, d, _), ListaSolucao),

    %Glenn está exatamente à direita do carro de 140.000 Km.
    nextto(carro(_,_, _, _, _, 140),carro(_, _, _, glenn, _,_),ListaSolucao),
    
    %O veículo de 1960 tem 140.000 Km.
    member(carro(_,1960, _, _, _, 140), ListaSolucao),
    
    %Harley está em uma das pontas.
    noCanto(carro(_,_, _, harley, _, _),ListaSolucao),
    
	%O carro Branco está em algum lugar entre o carro da Ford e o carro mais novo, nessa ordem.
    entre(carro(_, _, ford, _, _,_),carro(branco,_, _, _, _, _),carro(_, 1970, _,_, _, _), ListaSolucao),
    
    %O veículo de placa AAA-1111 está exatamente à esquerda do carro de 1955.
    nextto(carro(_, _, _, _, a,_),carro(_,1955, _, _, _, _),ListaSolucao),
    
    %O veículo Amarelo está em algum lugar à esquerda do carro de 140.000 Km.
	aEsquerda(carro(amarelo, _, _, _, _,_),carro(_,_, _, _, _, 140),ListaSolucao),
    
    %Na terceira posição está o carro da cor Verde.
    Cor3 = verde,
    
    %O carro de 1955 está exatamente à esquerda do carro de placa BBB-2222.
    nextto(carro(_, 1955, _, _, _,_),carro(_,_, _, _, b, _),ListaSolucao),

	%O carro da Volkswagen está em algum lugar à direita do carro Vermelho.
    aDireita(carro(_, _, volkswagen, _, _,_),carro(vermelho,_, _, _, _, _),ListaSolucao),

	%O veículo da Chevrolet está ao lado do veículo de 140.000 Km.
   	aoLado(carro(_, _, chevrolet, _, _,_),carro(_,_, _, _, _, 140),ListaSolucao),
    
    %Em uma das pontas está o carro mais rodado.
    noCanto(carro(_,_, _, _, _, 210),ListaSolucao),

    %O carro Branco está em algum lugar entre o carro de 190.000 Km e o veículo da Porsche, nessa ordem.
    entre(carro(_, _, _, _, _,190),carro(branco,_, _, _, _, _),carro(_, _, porsche,_, _, _), ListaSolucao),
    
    %O veículo de placa AAA-1111 está exatamente à esquerda do carro da Mercedes.
    nextto(carro(_, _, _, _, a,_),carro(_,_, mercedes, _, _, _),ListaSolucao),
    
    %O carro Branco está em algum lugar à esquerda do veículo de 100.000 Km.
    aEsquerda(carro(branco, _, _, _, _,_),carro(_,_, _, _, _, 100),ListaSolucao),
    
    %Ponce é o dono do carro da placa EEE-5555.
    member(carro(_,_, _, ponce, e, _), ListaSolucao),
    
    %O carro de 140.000 Km está em algum lugar à direita do carro Branco.
    aDireita(carro(_, _, _, _, _,140),carro(branco,_, _, _, _, _),ListaSolucao),
    
    %Thales está em algum lugar entre o carro de 1970 e o Glenn, nessa ordem.
    entre(carro(_, 1970, _, _, _,_),carro(_,_, _, thales, _, _),carro(_, _,_,glenn, _, _), ListaSolucao),
    
    %O veículo da Chevrolet está em algum lugar à direita do carro de 1965.
    aDireita(carro(_, _, chevrolet, _, _,_),carro(_,1965, _, _, _, _),ListaSolucao),
    
    %Testa todas as possibilidades...
    cor(Cor1),cor(Cor2),cor(Cor3),cor(Cor4),cor(Cor5),
    todosDiferentes([Cor1, Cor2, Cor3, Cor4, Cor5]),
    
    ano(Ano1),ano(Ano2),ano(Ano3),ano(Ano4),ano(Ano5),
    todosDiferentes([Ano1, Ano2, Ano3, Ano4, Ano5]),
    
    montadora(Montadora1), montadora(Montadora2), montadora(Montadora3), montadora(Montadora4), montadora(Montadora5), 
    todosDiferentes([Montadora1, Montadora2, Montadora3, Montadora4, Montadora5]),
    
    dono(Dono1), dono(Dono2), dono(Dono3), dono(Dono4), dono(Dono5), 
    todosDiferentes([Dono1, Dono2, Dono3, Dono4, Dono5]),
    
    km(Km1), km(Km2), km(Km3), km(Km4), km(Km5), 
    todosDiferentes([Km1, Km2, Km3, Km4, Km5]),
	
	placa(Placa1), placa(Placa2), placa(Placa3), placa(Placa4), placa(Placa5), 
    todosDiferentes([Placa1, Placa2, Placa3, Placa4, Placa5]).
    
