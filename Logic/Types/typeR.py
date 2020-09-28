def getFunctionCode(function):
  functionCode = {
    "add"   : "100000",
    "addu"  : "100001",
    "sub"   : "100010",
    "subu"  : "100011",
    "and"   : "100100",
    "or"    : "100101",
    "nor"   : "100111",
    "slt"   : "101010",
    "sltu"  : "101011",
    "sll"   : "000000",
    "srl"   : "000010",
    "jr"    : "001000",
    "div"   : "011010",
    "divu"  : "011011",
    "mfhi"  : "010000",
    "mflo"  : "010010",
    "mult"  : "011000",
    "multu" : "011001",
    "sra"   : "000011",
    "mfc0"  : "000000",
  }
  return functionCode[function]

def getOpCode(function):
  opCode = {
    "add"   : "000000",
    "addu"  : "000000",
    "sub"   : "000000",
    "subu"  : "000000",
    "and"   : "000000",
    "or"    : "000000",
    "nor"   : "000000",
    "slt"   : "000000",
    "sltu"  : "000000",
    "sll"   : "000000",
    "srl"   : "000000",
    "jr"    : "000000",
    "div"   : "000000",
    "divu"  : "000000",
    "mfhi"  : "000000",
    "mflo"  : "000000",
    "mult"  : "000000",
    "multu" : "000000",
    "sra"   : "000000",
    "mfc0"  : "010000",
  }
  return opCode[function]

def isFunction(function):
  functions = ["add", "addu", "sub", "subu", "and", "or", "nor", "slt", "sltu", "sll", "srl", "jr"]
  return function in functions