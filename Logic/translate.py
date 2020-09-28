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
    res += "{0:05b}".format(inmediate)
  return res

def getTranslationR(instruction):
  if instruction[0] in ["sra", "sll", "srl"]:
    return R.getOpCode(instruction[0]) + "00000" + rgstr.getRegisterCode(instruction[2]) + rgstr.getRegisterCode(instruction[1]) + convertInmediate(instruction[3])
  elif instruction[0] in ["add", "addu", "sub", "subu", "and", "or", "nor", "slt", "sltu"]:
    return R.getOpCode(instruction[0]) + rgstr.getRegisterCode(instruction[2]) + rgstr.getRegisterCode(instruction[3]) + rgstr.getRegisterCode(instruction[1]) + "00000" +R.getFunctionCode(instruction[0])
  elif instruction[0] in ["div", "divu", "mult", "multu"]:
    return R.getOpCode(instruction[0]) + rgstr.getRegisterCode(instruction[2]) + rgstr.getRegisterCode(instruction[3]) + "00000" + "00000" + R.getFunctionCode(instruction[0])
  elif instruction[0] == "jr":
    return R.getOpCode(instruction[0]) + rgstr.getRegisterCode(instruction[1]) + "00000" + "00000" + "00000" + R.getFunctionCode(instruction[0])
  elif instruction[0] in ["mfhi", "mflo"]:
    return R.getOpCode(instruction[0]) + "00000" + "00000" + rgstr.getRegisterCode(instruction[1]) + "00000" + R.getFunctionCode(instruction[0])


def translate(instructions):
  instructions = lx.parse(instructions)
  tagsPos = lx.getTagsPos(instructions)

  finalInstructions = ""
  for instruction in instructions:
    finalInstructions += "{0}\n".format(getTranslation(instruction, tagsPos))
  return finalInstructions.strip()