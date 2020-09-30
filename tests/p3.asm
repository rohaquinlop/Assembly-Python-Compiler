lui $s0, 0x1000
        ori $s0, $s0, 0x0000

        addi $t0, $0, 100
        addi $t1, $0, -50

        add $a0, $0, $t0
        add $a1, $0, $t1

        jal check

        add $t2, $0, $v0
        addi $t3, $0, 1
        bne  $t2, $t3, end_main

        div $t3, $a0, $a1
        sw $t3, 8($s0)
        add $a0, $0, $t3

        add $a0, $0, $t0
        jal store

        add $t3, $t1, $t0
        sw $t3,    4($s0)
        add $a0, $0, $t3
    end_main:
        jr $ra
    store:

        add $t3, $0, $a0
        addi $s1, $0, 0
        addi $t4, $0, 3
        addi $t2, $0, 100
        lui $s0, 0x1000
        ori $s0, $s0, 0x0000

        while:

            slt $s3, $s1, $t2
            beq $s3, $0, end_while

            sll $s4, $t4, 2
            add $s3, $s0, $s4
            mult $s4, $t3
            sw $s4, 0($s3)
            addi $s1, $s1, 1
            addi $t4, $t4, 1

            add $a0,$0, $s4
            j while

        end_while:

        jr $ra

    check:
        slt $s1, $a1, $a0
        addi $s2, $0, 1
        beq $a1,$0, checkZero

        and $s3, $s1, $s2
        add $v0, $0, $s3

        jr $ra

    checkZero:

        addi $s2, $0, 0