import sys, re
sys.path.append("..")

from Logic.Types import typeR as R
from Logic.Types import typeI as I
from Logic.Types import typeJ as J
from Logic.Types import registers as rgstr
from Logic import lexer as lx


def translate(instructions):
  instructions = lx.parse(instructions)
  tagsPos = lx.getTagsPos(instructions)

  finalInstructions = ""
  for instruction in instructions:
    finalInstructions += "{0}\n".format(getTranslation(instruction, tagsPos))
  return finalInstructions.strip()