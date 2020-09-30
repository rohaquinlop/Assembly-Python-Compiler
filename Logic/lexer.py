import sys, re
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

def inmediateVerification(inmediate):
  ##Auxiliar function that verifies if the inmediate is a dec or a hex
  if '0x' in inmediate or '0X' in inmediate:
    return True
  else:
    for i in inmediate:
      if not(48 <= ord(i) <= 57 or ord(i) == 45):
        ##If its true then the i char isn't a number or is different to "X" or "x"
        return False
    ##Then the inmediate is a decimal or a hex
    return True

def getTagsPos(instructions):
  tagsPos = dict()
  PC = 0
  for instruction in instructions:
    if len(instruction) > 0:
      if len(instruction) == 1:
        if isTag(instruction[0]):
          tagsPos[ instruction[0][:len(instruction[0])-1] ] = PC
      PC += 4
  return tagsPos

def isTag(instruction):
  pattern = re.findall("^[a-zA-Z]*:", instruction)
  if len(pattern) > 0:
    return True
  else:
    return False

def isRInstruction(instruction):
  ##Validate if there is the correct length for the instruction
  n = len(instruction)
  if n == 4:
    ##Is a valid length
    if instruction[0] in ["sra", "sll", "srl"]:
      return (rgstr.isRegister(instruction[1]) and instruction[1] != "$zero" and not(rgstr.isReserved(instruction[1])) and rgstr.isRegister(instruction[2]) and inmediateVerification(instruction[3]))
    elif instruction[0] in ["add", "addu", "sub", "subu", "and", "or", "nor", "slt", "sltu"]:
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
    else:
      return False
  elif n == 3:
    if instruction[0] in ["div", "divu", "mult", "multu"]:
      ##Result is saved in HI and LO
      return rgstr.isRegister(instruction[1]) and rgstr.isRegister(instruction[2])
    elif instruction[0] == "mfc0":
      return rgstr.isRegister(instruction[1])  and not(rgstr.isReserved(instruction[1])) and instruction[1] != "$zero" and rgstr.isRegister(instruction[2])
    else:
      return False
  elif n == 2:
    ##Is a valid length (jr)
    if instruction[0] == "jr":
      ##Means that the instruction is correct
      return rgstr.isRegister(instruction[1])
    elif instruction[0] in ["mfhi", "mflo"]:
      return rgstr.isRegister(instruction[1]) and not(rgstr.isReserved(instruction[1])) and instruction[1] != "$zero"
    else:
      return False
  else:
    return False

def isIInstruction(instruction, tagsPos):
  ##Validate if the instruction length is correct
  n = len(instruction)
  if n == 4 and instruction[0] != "lui":
    ##Verify if the instruction's fields are the corrects
    if instruction[0] in ["lw", "sw", "lbu", "lhu", "ll", "sb", "sc", "sh", "lwc1", "ldc1", "swc1", "sdc1"]:
      ##Have inmediate in instruction[2] and all the conditions are respected
      if rgstr.isRegister(instruction[1]) and not( rgstr.isReserved(instruction[1]) ) and instruction[1] != "$zero" and inmediateVerification(instruction[2]) and rgstr.isRegister(instruction[3]):
        return True
      else:
        return False
    else:
      ##Are the standard in the conditions
      for i in range(1, n-1):
        if i == 1 and instruction[i] == "$zero":
          ## If we are trying to modify the register $zero then return False, it's not allowed
          return False
        else:
          if not(rgstr.isRegister(instruction[i])) or rgstr.isReserved(instruction[i]):
            ##If it's not a valid register or it's a reserved register then return False, it's not allowed
            return False
      ##If finalizes all the process that means that we only need to verify if it's last field is a inmediate or is a valid tag
      if instruction[0] in ["beq", "bne"]:
        ##Verify if branch goes to a tag or to a PC number
        if inmediateVerification(instruction[3]):
          return True
        else:
          return instruction[3] in tagsPos
      else:
        ##Only verify if it must jump to a PC number
        return inmediateVerification(instruction[3])
  elif n == 3 and instruction[0] == "lui":
    ##Verify if the fields for the lui are corrects
    if instruction[1] != "$zero" and rgstr.isRegister(instruction[1]) and not(rgstr.isReserved(instruction[1])):
      ##Verify if the inmediate valid
      return inmediateVerification(instruction[2])
    else:
      return False
  else:
    return False

def isJInstruction(instruction, tagsPos):
  ##Validate if the instruction length is correct
  n = len(instruction)
  if n == 2:
    if inmediateVerification(instruction[1]):
      return True
    else:
      j = len(instruction[1])
      return instruction[1] in tagsPos
  else:
    return False

def isAcceptable(instruction, tagsPos):
  """
  Determine if a instruction is acceptable or not
  return True or False
  """
  if R.isFunction(instruction[0]):
    ##Is a type R instruction
    return isRInstruction(instruction)
  elif I.isOpCode(instruction[0]):
    ##Is a type I instruction
    return isIInstruction(instruction, tagsPos)
  elif J.isOpCode(instruction[0]):
    ##Is a type J instruction
    return isJInstruction(instruction, tagsPos)
  else:
    if not(isTag(instruction[0])):
      ##It's a not valid case
      return False
    else:
      return True

def verify(instructions):
  """
  Determine if input's correct
  return True or False
  """

  ##Parsing input
  instructions = parse(instructions)
  ##Getting all the tags
  tagsPos = getTagsPos(instructions)

  for instruction in instructions:
    if(len(instruction) > 0):
      if not(isAcceptable(instruction, tagsPos)):
        return False
  return True