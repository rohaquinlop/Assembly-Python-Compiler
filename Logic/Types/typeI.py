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
  }
  return opCode[op]


def isOpCode(op):
  ops = ["beq", "bne", "addi", "addiu", "andi", "ori", "slti", "sltiu", "lui", "lw", "sw"]
  return op in ops