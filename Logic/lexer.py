import sys
sys.path.append("..")

from Logic.Types import typeR as R
from Logic.Types import typeI as I
from Logic.Types import typeJ as J

def parse(instructions):
  """
  Split each input line and return it
  """
  instructions = instructions.strip().split("\n")

  ##Split each line and delete special characters
  instructions = list(map(lambda x : x.replace(",", " ").replace("(", " ").replace(")", " ").split(), instructions))
  return instructions

def isAcceptable(instruction):
  """
  Determine if a instruction is acceptable or not
  return True or False
  """

def verify(instructions):
  """
  Determine if input's correct
  return True or False
  """

  ##Parsing input
  instructions = parse(instructions)

  for instruction in instructions:
    print(instruction)

  return True