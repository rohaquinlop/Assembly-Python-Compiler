import sys
sys.path.append("..")

from Logic.Types import typeR as R

def verify(instructions):
  ##Determine if input's correct
  instructions = instructions.strip().split("\n")

  instructions = list(map(lambda x : x.replace(",", " ").replace("(", " ").replace(")", " ").split(), instructions))

  for instruction in instructions:
    print(instruction)

  return True