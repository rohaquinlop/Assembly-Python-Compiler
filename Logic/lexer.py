import sys
sys.path.append("..")

from Logic.Types import typeR as R
from Logic.Types import typeI as I
from Logic.Types import typeJ as J
from Logic.Types import registers as rgstr

def parse(instructions):
  """
  Split each input line and return it
  """
  instructions = instructions.strip().split("\n")

  ##Split each line and delete special characters
  instructions = list(map(lambda x : x.replace(",", " ").replace("(", " ").replace(")", " ").split(), instructions))
  return instructions

def isRInstruction(instruction):
  ##Validate if there is the correct length for the instruction
  n = len(instruction)
  if n == 4 and instruction[0] != "jr":
    ##Is a valid length
    for i in range(1, n):
      if i == 1 and instruction[i] == "$zero":
        ## If we are trying to modify the register $zero then return False, it's not allowed
        return False
      else:
        if not(rgstr.isRegister(instruction[i])) or rgstr.isReserved(instruction[i]):
          ##If it's not a valid register or it's a reserved register then return False, it's not allowed
          return False
    ##If finalizes all the process that means that the input was correct (Never returned False)
    return True
  elif n == 2:
    ##Is a valid length (jr)
    if instruction[0] == "jr" and rgstr.isRegister(instruction[1]):
      ##Means that the instruction is correct
      return True
    else:
      return False
  else:
    return False

def isAcceptable(instruction):
  """
  Determine if a instruction is acceptable or not
  return True or False
  """
  if R.isFunction(instruction[0]):
    ##Is a type R instruction
    return isRInstruction(instruction)
  elif I.isOpCode(instruction[0]):
    ##Is a type I instruction
  elif J.isOpCode(instruction[0]):
    ##Is a type J instruction
  else:
    ##It's a not valid case
    return False

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