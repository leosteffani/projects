(defun comprimento (lista) ;funcao passada pelo professor
    (if (null lista) ;testa se lista é vazia
        0
        (+ 1 (comprimento (cdr lista))) ;cdr retorna cauda
    )
)
(defun create_pvalues(number) ;funcao para elaborar o conjunto pvalues (explicado adiante)
    (setq temp '())
    (dotimes (i number)
        (setq temp (concatenate 'list temp (list (+ 1 i))))
    )
    temp
)
(defun main()
    ;; criando matriz do tabuleiro
    (setq cont 0) ;contador de slots preenchidos
    (setq matriz '(
        (1 0 0 6 0 0 7 0 1 2)
        (0 0 2 4 0 6 5 3 0 1)
        (0 0 0 2 0 0 0 6 1 0)
        (0 0 0 0 4 0 2 0 0 3)
        (4 0 3 0 0 5 0 0 3 0)
        (0 0 2 0 0 0 2 3 0 0)
        (0 0 0 0 0 5 0 0 1 0)
        (0 1 0 0 0 0 0 0 0 4)
        (4 0 0 1 0 0 3 0 2 0)
        (2 0 0 0 5 3 0 4 0 0)))
    (setq tamanho (comprimento matriz)) ;contem o tamanho da matriz
    (defstruct slot ;extrutura q armazena as informações de cada slot da matriz
        grupo ; qual grupo pertence
        upper ; se precisa ser maior que alguem
        lower ; se precisa ser menor que alguem
        pvalues ;possiveis valores que o slot pode conter (NIL se o slot ja foi preenchido)
        setvalue ;valor final do slot(0 se não foi definido)
        number ;indice da matriz vetorizada (usado pra facilitar certas operacoes)
    )
    

    (setq matriz_slots '( ;matriz que ira conter as extruturas slot
        (0 0 0 0 0 0 0 0 0 0)
        (0 0 0 0 0 0 0 0 0 0)
        (0 0 0 0 0 0 0 0 0 0)
        (0 0 0 0 0 0 0 0 0 0)
        (0 0 0 0 0 0 0 0 0 0)
        (0 0 0 0 0 0 0 0 0 0)
        (0 0 0 0 0 0 0 0 0 0)
        (0 0 0 0 0 0 0 0 0 0)
        (0 0 0 0 0 0 0 0 0 0)
        (0 0 0 0 0 0 0 0 0 0)))
    
    (setq grupos '( ; casas que estão nos mesmo grupo (indice vetoriazado e começa em 1)
        (1 2)
        (3)
        (4 5 6 13 14 15)
        (7 8 16 17 18 19 20)
        (9 10)
        (11 21)
        (12 22 32)
        (23)
        (24 33 34 35 45 46)
        (25)
        (26 36)
        (27 28 29 37 38 48 49)
        (30 39 40 50)
        (31 41 42 51 61)
        (43 44 54 55 64)
        (47 56 57 58 59 67)
        (52 53 62 63)
        (60 69 70 80 90 100)
        (65 66 74 75 76)
        (68 78 79)
        (71 72 73 81 91)
        (77 87 88 89 99)
        (82 92)
        (83 84 85 93)
        (86 94 95 96 97 98)
        ))
    (setq setado '()) ; ira conter o indice vetorizado das casas ja preenchidas
    (setq ngrupos (comprimento grupos)) ; numero de grupos
    (setq a 1) ; variavel usada pra marcar o indice vetorizado dos elementos
    (dotimes (i tamanho) ; agora vamos criar as extruturas slot
        (dotimes (j tamanho)
            (setq temp2 '())
            (setq temp2(cons a temp2)) ;cria lista com o elemento a para que o metodo intersection funcione (não tinha conhecimento ainda da funcao list)
            (dotimes (x (comprimento grupos))
                (setq temp (intersection (nth x grupos) temp2)) ; verifica se esta contido no grupo x
                (if (not (eq temp NIL))
                    (setq tempgrupo x) ; marca o grupo que o slot pertence
                )
            )
            (setq temp2 '())
            (setq temp2(cons (+ a tamanho) temp2))
            (setq temp (intersection (nth tempgrupo grupos) temp2)) ; verifica se o vizinho de baixo esta contido no grupo x
            (if (not (eq temp NIL))
                (setq tempupper T) ;define se o slot é upper ou não
                (setq tempupper NIL)
            )
            (setq temp2 '())
            (setq temp2(cons (- a tamanho) temp2))
            (setq temp (intersection (nth tempgrupo grupos) temp2)) ; verifica se o vizinho de cima esta contido no grupo x
            (if (not (eq temp NIL))
                (setq templower T) ;define se o slot é lower ou não
                (setq templower NIL)
            )
            (if (/= (nth j (nth i matriz)) 0)
                (setq tempvalues NIL)
                (setq tempvalues (create_pvalues (comprimento (nth tempgrupo grupos)))) ;cria pvalues do slot
            )
            (if (/= (nth j (nth i matriz)) 0)
                (setq tempvalue (nth j (nth i matriz))) ;marca o valor do slot (se tiver)
                (setq tempvalue 0)
            )
            (if (/= (nth j (nth i matriz)) 0)
                (setq cont(+ cont 1)) ;soma 1 no contador se o slot tem valor definido
            )
            (setq s0 ;seta a extrutura
                (make-slot
                :grupo tempgrupo
                :upper tempupper
                :lower templower
                :pvalues tempvalues
                :setvalue tempvalue
                :number a
                )
            )
            (if (/= (nth j (nth i matriz)) 0)
                (setq setado (cons a setado)) ; se o valor estiver definido, coloca no vetor
            )
            (setf (nth j (nth i matriz_slots)) s0) ;adiciona a extrutura na matriz
            (setq a (+ 1 a)) ;atualiza o valor de a
        )
    )
    ;funcoes que alteram matriz
    (defun preenche(x y number) ;define o valor number para o slot de coordenadas x y e modifica o que é necessario 
        (setf (nth y (nth x matriz)) number)
        (setf (slot-setvalue (nth y (nth x matriz_slots))) number)
        (setf (slot-pvalues (nth y (nth x matriz_slots))) NIL)
        (setq cont(+ cont 1))
        (setq setado (cons (slot-number (nth y (nth x matriz_slots))) setado))
    )
    (defun detect_upper() ;detecta os slots que são upper e atualiza seus valores possiveis baseado no vizinho de baixo
        (dotimes (i tamanho) 
            (dotimes (j tamanho)
                (if (not (eq NIL (slot-pvalues (nth j (nth i matriz_slots)))))
                    (if (eq T (slot-upper (nth j (nth i matriz_slots))))
                        (progn ;resumindo, se o slot fr upper de alguém, remove os valores impossiveis se baseado nos valores possiveis do vizinho de baixo
                            (setq b 1) ;esses valores impossiveis são valores que são menores ou iguais ao menor valor que o vizinho de baixo pode assumir
                            (if (not (eq (slot-pvalues (nth j (nth (+ i 1) matriz_slots))) NIL))
                                (loop
                                    (setf (slot-pvalues (nth j (nth i matriz_slots))) (set-difference (slot-pvalues (nth j (nth i matriz_slots))) (list b)))
                                    (setq b (+ b 1))
                                    (when (> b (car (slot-pvalues (nth j (nth (+ i 1) matriz_slots))))) (return NIL)) 
                                )
                                (loop
                                    (setf (slot-pvalues (nth j (nth i matriz_slots))) (set-difference (slot-pvalues (nth j (nth i matriz_slots))) (list b)))
                                    (setq b (+ b 1))
                                    (when (> b (slot-setvalue (nth j (nth (+ i 1) matriz_slots)))) (return NIL)) 
                                )
                            )
                        )
                    )    
                )
            )
        )
    )
    
    
    
    
    (defun detect_lower() ;detecta os slots que são upper e atualiza seus valores possiveis baseado no vizinho de bcima
        (dotimes (i tamanho)
            (dotimes (j tamanho)
                (if (not (eq NIL (slot-pvalues (nth j (nth i matriz_slots)))))
                    (if (eq T (slot-lower (nth j (nth i matriz_slots))))
                        (progn ;resumindo, se o slot fr lower de alguém, remove os valores impossiveis se baseado nos valores possiveis do vizinho de cima
                            (setq b 9) ;esses valores impossiveis são valores que são maiores ou iguais ao maior valor que o vizinho de cima pode assumir
                            (if (not (eq (slot-pvalues (nth j (nth (- i 1) matriz_slots))) NIL))
                                (loop
                                    (setf (slot-pvalues (nth j (nth i matriz_slots))) (set-difference (slot-pvalues (nth j (nth i matriz_slots))) (list b)))
                                    (setq b (- b 1))
                                    (when (< b (car (last (slot-pvalues (nth j (nth (- i 1) matriz_slots)))))) (return NIL)) 
                                )
                                (loop
                                    (setf (slot-pvalues (nth j (nth i matriz_slots))) (set-difference (slot-pvalues (nth j (nth i matriz_slots))) (list b)))
                                    (setq b (- b 1))
                                    (when (< b (slot-setvalue (nth j (nth (- i 1) matriz_slots)))) (return NIL)) 
                                )
                            )
                        )
                    )    ;(setr (pvalues (nth j (nth i matriz_slots))) (set-difference (pvalues (nth j (nth i matriz_slots))) '(1)))
                )
            )
        )
    )
    
    (defun detect_ort() ; remove dos valores possiveis os valores dos slots ortogonais ja definidos
        (dotimes (i tamanho)
            (dotimes (j tamanho)
                (if (not (eq NIL (slot-pvalues (nth j (nth i matriz_slots)))))
                    (progn
                        (if (> i 0) ;ifs como esse são para que o codigo não acesse algo fora dos limites da matriz
                            (if (/= (slot-setvalue (nth j (nth (- i 1) matriz_slots))) 0)
                                (setf (slot-pvalues (nth j (nth i matriz_slots))) (set-difference (slot-pvalues (nth j (nth i matriz_slots))) (list (slot-setvalue (nth j (nth (- i 1) matriz_slots))))))
                            )
                        )
                        (if (< i 9)
                            (if (/= (slot-setvalue (nth j (nth (+ i 1) matriz_slots))) 0)
                                (setf (slot-pvalues (nth j (nth i matriz_slots))) (set-difference (slot-pvalues (nth j (nth i matriz_slots))) (list (slot-setvalue (nth j (nth (+ i 1) matriz_slots))))))
                            )
                        )
                        (if (> j 0)
                            (if (/= (slot-setvalue (nth (- j 1) (nth i matriz_slots))) 0)
                                (setf (slot-pvalues (nth j (nth i matriz_slots))) (set-difference (slot-pvalues (nth j (nth i matriz_slots))) (list (slot-setvalue (nth (- j 1) (nth i matriz_slots))))))
                            )
                        )
                        (if (< j 9)
                            (if (/= (slot-setvalue (nth (+ j 1) (nth i matriz_slots))) 0)
                                (setf (slot-pvalues (nth j (nth i matriz_slots))) (set-difference (slot-pvalues (nth j (nth i matriz_slots))) (list (slot-setvalue (nth (+ j 1) (nth i matriz_slots))))))
                            )
                        ) 
                    )
                )
            )
        )
    )
    (defun detect_grupo() ;remove dos valores possiveis os valores que ja estao presentes no grupo
        (dotimes (grupo ngrupos)
            (setq relacao (intersection setado (nth grupo grupos)))
            (if (not (eq NIL relacao))
                (dotimes (n_relacoes (comprimento relacao))
                    (setq j (mod (- (nth n_relacoes relacao) 1) tamanho)) ;desvetorizando a matriz
                    (setq i (floor (- (nth n_relacoes relacao) 1) tamanho))
                    (dotimes (n_grupo (comprimento (nth grupo grupos)))
                        (setq tempj (mod (- (nth n_grupo (nth grupo grupos)) 1) tamanho))
                        (setq tempi (floor (- (nth n_grupo (nth grupo grupos)) 1) tamanho))
                        (setf (slot-pvalues (nth tempj (nth tempi matriz_slots))) (set-difference (slot-pvalues (nth tempj (nth tempi matriz_slots))) (list (slot-setvalue (nth j (nth i matriz_slots))))))
                    )
                    
                )
            )
        )
    )
    (defun detect_set() ;procura por todos os slots que possuem só um valor possivel e define ele como valor efetivo do slot
        (dotimes (i tamanho)
            (dotimes (j tamanho)
                (if (not (eq NIL (slot-pvalues (nth j (nth i matriz_slots)))))
                    (if (= 1 (comprimento (slot-pvalues (nth j (nth i matriz_slots)))))
                        (progn
                            (preenche i j (car (slot-pvalues (nth j (nth i matriz_slots)))))
                        )
                    )
                )
            )
        )
    )
        ;(if (>= cont 100)
            ;(setq stop T)
    (loop ;loop com as funcoes
        (detect_upper)
        (detect_set)
        (detect_lower)
        (detect_set)
        (detect_ort)
        (detect_set)
        (detect_grupo)
        (detect_set)
        (when (>= cont (* tamanho tamanho)) (return NIL)) ;teste de fim do jogo
    ) 
    (dotimes(i tamanho)
        (write (nth i matriz))
        (write-line "")
    )
)
(main)