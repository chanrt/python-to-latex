from term import Term
from functions import *
from symbols import *
from settings import Settings

a = Term("a")
b = Term("b")
c = Term("c")

result = log((a + b) ** 2 / c, 3) - sym_alpha
result.decorate("abs").enumerate(2).latex()

