def getRegisterCode(register):
  registerCode = {
    "$zero"   : "00000",
    "$at"     : "00001",
    "$v0"     : "00010",
    "$v1"     : "00011",
    "$a0"     : "00100",
    "$a1"     : "00101",
    "$a2"     : "00110",
    "$a3"     : "00111",
    "$t0"     : "01000",
    "$t1"     : "01001",
    "$t2"     : "01010",
    "$t3"     : "01011",
    "$t4"     : "01100",
    "$t5"     : "01101",
    "$t6"     : "01110",
    "$t7"     : "01111",
    "$s0"     : "10000",
    "$s1"     : "10001",
    "$s2"     : "10010",
    "$s3"     : "10011",
    "$s4"     : "10100",
    "$s5"     : "10101",
    "$s6"     : "10110",
    "$s7"     : "10111",
    "$t8"     : "11000",
    "$t9"     : "11001",
    "$k0"     : "11010",
    "$k1"     : "11011",
    "$gp"     : "11100",
    "$sp"     : "11101",
    "$fp"     : "11110",
    "$ra"     : "11111",
  }
  return registerCode[register]

def isReserved(register):
  reserved = ["$k0", "$k1", "$zero"]
  return register in reserved

def isRegister(register):
  registers = ["$zero","$at","$v0","$v1","$a0","$a1","$a2","$a3","$t0","$t1","$t2","$t3","$t4","$t5","$t6","$t7",
               "$s0","$s1","$s2","$s3","$s4","$s5","$s6","$s7","$t8","$t9","$k0","$k1","$gp","$sp","$fp","$ra",]

  return register in registers