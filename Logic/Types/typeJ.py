def getOpCode(op):
  opCode = {
    "j"   : "000010",
    "jal" : "000011",
  }
  return opCode[op]

def isOpCode(op):
  ops = ["j", "jal"]
  return op in ops