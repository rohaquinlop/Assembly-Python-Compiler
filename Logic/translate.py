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


def translate(instructions):
  instructions = lx.parse(instructions)
  tagsPos = lx.getTagsPos(instructions)

  finalInstructions = ""
  for instruction in instructions:
    finalInstructions += "{0}\n".format(getTranslation(instruction, tagsPos))
  return finalInstructions.strip()