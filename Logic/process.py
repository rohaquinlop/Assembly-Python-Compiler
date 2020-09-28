import sys
sys.path.append("..")
from Logic import lexer as lx

def process(instructions):
  if lx.verify(instructions):
    return "Se puede traducir"
  else:
    return "Error! no se cumplen los requirimientos de sintaxis!"