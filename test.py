from term import Term
from functions import *
from calculus import *
from symbols import *
from settings import Settings

v = Term("v")
c = Term("c")

result = sym_gamma.equate(1 / sqrt(1 - (v / c)**2))
result.render()

