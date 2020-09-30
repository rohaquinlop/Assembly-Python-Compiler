import sys, re
sys.path.append("..")

from Logic.Types import typeR as R
from Logic.Types import typeI as I
from Logic.Types import typeJ as J
from Logic.Types import registers as rgstr
from Logic import lexer as lx

def convertInmediate(inmediate):
  res = ""
  if 'x' in inmediate:
    res += "{0:05b}".format(int(inmediate[inmediate.find('x')+1:], 16))
  elif 'X' in inmediate:
    res += "{0:05b}".format(int(inmediate[inmediate.find('X')+1:], 16))
  else:
    res += "{0:05b}".format(int(inmediate))
  res = res.replace("-", "0")
  return res

def convertInmediateIAux(inmediate):
  res = ""
  if 'x' in inmediate:
    res += "{0:016b}".format(int(inmediate[inmediate.find('x')+1:], 16))
  elif 'X' in inmediate:
    res += "{0:016b}".format(int(inmediate[inmediate.find('X')+1:], 16))
  else:
    res += "{0:016b}".format(int(inmediate))
  res = res.replace("-", "0")
  return res

def convertInmediateI(inmediate):
  res = ""
  if 'x' in inmediate:
    res += "{0:016b}".format(int(inmediate[inmediate.find('x')+1:], 16)//4)
  elif 'X' in inmediate:
    res += "{0:016b}".format(int(inmediate[inmediate.find('X')+1:], 16)//4)
  else:
    res += "{0:016b}".format(int(inmediate)//4)
  res = res.replace("-", "0")
  return res

def convertInmediateJ(inmediate):
  res = ""
  if '0x' in inmediate:
    res += "{0:026b}".format(int(inmediate[inmediate.find('x')+1:], 16)//4)
  elif '0X' in inmediate:
    res += "{0:026b}".format(int(inmediate[inmediate.find('X')+1:], 16)//4)
  else:
    res += "{0:026b}".format(int(inmediate)//4)
  res = res.replace("-", "0")
  return res

def convertInmediateJAux(inmediate):
  res = ""
  if '0x' in inmediate:
    res += "{0:026b}".format(int(inmediate[inmediate.find('x')+1:], 16))
  elif '0X' in inmediate:
    res += "{0:026b}".format(int(inmediate[inmediate.find('X')+1:], 16))
  else:
    res += "{0:026b}".format(int(inmediate))
  res = res.replace("-", "0")
  return res

def getTranslationR(instruction):
  if instruction[0] in ["sra", "sll", "srl"]:
    return (R.getOpCode(instruction[0]) + "00000" + rgstr.getRegisterCode(instruction[2]) + rgstr.getRegisterCode(instruction[1]) + convertInmediate(instruction[3]))
  elif instruction[0] in ["add", "addu", "sub", "subu", "and", "or", "nor", "slt", "sltu"]:
    return (R.getOpCode(instruction[0]) + rgstr.getRegisterCode(instruction[2]) + rgstr.getRegisterCode(instruction[3]) + rgstr.getRegisterCode(instruction[1]) + "00000" + R.getFunctionCode(instruction[0]))
  elif instruction[0] in ["div", "divu", "mult", "multu"]:
    return (R.getOpCode(instruction[0]) + rgstr.getRegisterCode(instruction[2]) + rgstr.getRegisterCode(instruction[1]) + "00000" + "00000" + R.getFunctionCode(instruction[0]))
  elif instruction[0] == "jr":
    return (R.getOpCode(instruction[0]) + rgstr.getRegisterCode(instruction[1]) + "00000" + "00000" + "00000" + R.getFunctionCode(instruction[0]))
  elif instruction[0] in ["mfhi", "mflo"]:
    return (R.getOpCode(instruction[0]) + "00000" + "00000" + rgstr.getRegisterCode(instruction[1]) + "00000" + R.getFunctionCode(instruction[0]))


def getTranslationI(instruction, tagsPos, PC):
  if instruction[0] in ["lw", "sw", "lbu", "lhu", "ll", "sb", "sc", "sh", "lwc1", "ldc1", "swc1", "sdc1"]:
    return (I.getOpCode(instruction[0]) + rgstr.getRegisterCode(instruction[3]) + rgstr.getRegisterCode(instruction[1]) + convertInmediateIAux(instruction[2]))
  elif instruction[0] in ["addi", "addiu", "andi", "ori", "slti", "sltiu"]:
    return (I.getOpCode(instruction[0]) + rgstr.getRegisterCode(instruction[2]) + rgstr.getRegisterCode(instruction[1]) + convertInmediateIAux(instruction[3]))
  elif instruction[0] in ["beq", "bne"]:
    if lx.inmediateVerification(instruction[3]):
      return (I.getOpCode(instruction[0]) + rgstr.getRegisterCode(instruction[1]) + rgstr.getRegisterCode(instruction[2]) + convertInmediateI(instruction[3]))
    else:
      j = len(instruction[3])
      #return instruction[3][:j-1] in tagsPos
      return (I.getOpCode(instruction[0]) + rgstr.getRegisterCode(instruction[1]) + rgstr.getRegisterCode(instruction[2]) + convertInmediateI(str(tagsPos[instruction[3]] - PC)))
  elif instruction[0] == "lui":
    return (I.getOpCode(instruction[0]) + "00000" + rgstr.getRegisterCode(instruction[1]) + convertInmediateIAux(instruction[2]))

def getTranslationJ(instruction, tagsPos, PC):
  if lx.inmediateVerification(instruction[1]):
    return (J.getOpCode(instruction[0]) + convertInmediateJAux(instruction[1]))
  else:
    return (J.getOpCode(instruction[0]) + convertInmediateJ(str(tagsPos[instruction[1]])))

def getTranslation(instruction, tagsPos, PC):
  if R.isFunction(instruction[0]):
    return getTranslationR(instruction)
  elif I.isOpCode(instruction[0]):
    return getTranslationI(instruction, tagsPos, PC)
  elif J.isOpCode(instruction[0]):
    return getTranslationJ(instruction, tagsPos, PC)
  else:
    return ""

def translate(instructions):
  instructions = lx.parse(instructions)
  tagsPos = lx.getTagsPos(instructions)

  finalInstructions = ""
  PC = 0
  for instruction in instructions:
    if len(instruction) > 0:
      PC += 4
      ans  = getTranslation(instruction, tagsPos, PC)
      if len(ans) > 0:
        finalInstructions += "{0}\n".format(ans)
  return finalInstructions.strip()