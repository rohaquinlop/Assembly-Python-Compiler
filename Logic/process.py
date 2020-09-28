import sys
sys.path.append("..")
from Logic import lexer as lx
from Logic import translate as tsl

def process(instructions):
  if lx.verify(instructions):
    return tsl.translate(instructions)
  else:
    return "Error! no se cumplen los requirimientos de sintaxis!"