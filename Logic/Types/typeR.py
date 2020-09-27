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
  }
  return functionCode[function]

def getOpCode(function):
  return "000000"

def isFunction(function):
  functions = ["add", "addu", "sub", "subu", "and", "or", "nor", "slt", "sltu", "sll", "srl", "jr"]
  return function in functions