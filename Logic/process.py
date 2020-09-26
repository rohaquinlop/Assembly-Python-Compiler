import sys
sys.path.append("..")
from Logic import lexer as lx

def process(instructions):
  lx.verify(instructions)
  return 0