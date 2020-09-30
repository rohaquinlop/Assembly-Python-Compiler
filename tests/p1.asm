lui      $s0, 0x1000
ori     $s0, $s0, 0x0000
lw     $s1, 0($s0)
lw     $s2,4($s0)
beq     $s2, $0, inicializar
slt     $t0, $s2, $s1
beq     $t0, $0, inicializar
div     $s1, $s2
mflo     $s3
sw         $s3, 8($s0)
inicializar:
addi     $sp, $sp, -4
sw     $ra, 0($sp)
addi     $a0, $0,0
addi     $a1, $s0, 12
addi     $a2, $0, 100
addi     $a3, $s1, 0
jal funct
add     $s2, $s1, $s2
sw     $s2, 4($s0)
lw     $ra, 0($sp)
addi     $sp, $sp,4
jr    $ra


funct:
beq     $a0, $a2, termino
mult     $a0, $a3
mflo     $t0
sw     $t0, 0($a1)
addi     $a0, $a0,1
addi     $a1, $a1,4
j funct

termino:
jr     $ra