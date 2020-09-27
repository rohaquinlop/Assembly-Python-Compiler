def getOpCode(op):
  opCode = {
    "j"   : "000010",
    "jal" : "000011",
  }

def isOpCode(op):
  ops = ["j", "jal"]
  return op in ops