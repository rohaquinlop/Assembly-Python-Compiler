def getOpCode(op):
  opCode = {
    "beq"    : "000100",
    "bne"    : "000101",
    "addi"   : "001000",
    "addiu"  : "001001",
    "andi"   : "001100",
    "ori"    : "001101",
    "slti"   : "001010",
    "sltiu"  : "001011",
    "lui"    : "001111",
    "lw"     : "100011",
    "sw"     : "101011",
    "lbu"    : "100100",
    "lhu"    : "100101",
    "ll"     : "110000",
    "sb"     : "101000",
    "sh"     : "101001",
    "lwc1"   : "110001",
    "ldc1"   : "110101",
    "swc1"   : "111001",
    "sdc1"   : "111101",
  }
  return opCode[op]


def isOpCode(op):
  ops = ["beq", "bne", "addi", "addiu", "andi", "ori", "slti", "sltiu", "lui", "lw", "sw", "lbu", "lhu", "ll", "sb", "sh", "lwc1", "ldc1", "swc1", "sdc1"]
  return op in ops