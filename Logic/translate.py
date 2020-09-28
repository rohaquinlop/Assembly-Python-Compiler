import sys, re
sys.path.append("..")

from Logic.Types import typeR as R
from Logic.Types import typeI as I
from Logic.Types import typeJ as J
from Logic.Types import registers as rgstr
from Logic import lexer as lx


def translate(instructions):
  return 0