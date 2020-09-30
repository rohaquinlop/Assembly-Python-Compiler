factorial:
    addi $sp,$sp,-8   #reservo 8
    sw $a0, 4($sp)         #guardo parametro de enrtrada
    sw $ra, 0($sp)        #guardo valor de retorno
    addi $t0,$0,2
    slt $t0,$a0,$t0        #pregunto si levalor de entrada es menor que 2
    beq $t0, $0, else       # si no es menor osea que no es 1, va al else
    addi $v0,$0,1        #ultima entrada, le suma 1
    addi $sp ,$sp , 8    #libera direccion
    jr $ra            #salta al anterior


else:
    addi $a0,$a0,-1        #le resto 1 a n
    jal factorial        #salta a factorial y deja un nuevo ra
    lw $ra, 0($sp)        #recupera direccion anterior
    lw $a0 , 4($sp)        #recupera el valor anterior
    addi $sp, $sp, 8        #desapila
    mul $v0, $a0, $v0    #multiplica
    jr $ra            #salta al ra