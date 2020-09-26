import sys
sys.path.append("..")

from Logic.Types import typeR as R

def parse(instructions):
  ##Split each input line
  instructions = instructions.strip().split("\n")

  ##Split each line and delete special characters
  instructions = list(map(lambda x : x.replace(",", " ").replace("(", " ").replace(")", " ").split(), instructions))
  return instructions

def verify(instructions):
  ##Determine if input's correct

  ##Parsing input
  instructions = parse(instructions)

  for instruction in instructions:
    print(instruction)

  return True