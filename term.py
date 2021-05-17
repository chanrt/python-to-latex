from settings import Settings
from commons import *


class Term:
    """Anything that can be incorporated into an expression written in latex code"""
    def __init__(self, name: str, decorator=None):
        if decorator is None:
            self.name = name

        if decorator == "vec":
            self.name = "\\vec{" + name + "}"
        elif decorator == "mod" or decorator == "abs":
            self.name = "\\left|" + name + "\\right|"
        elif decorator == "brac":
            self.name = "\\left(" + name + "\\right)"
        elif decorator == "brace":
            self.name = "\\left\\lbrace" + name + "\\right\\rbrace"
        elif decorator == "angle":
            self.name = "\\left\\langle" + name + "\\right\\rangle"
        elif decorator == "box":
            self.name = "\\left[" + name + "\\right]"
        elif decorator == "floor":
            self.name = "\\lfloor" + name + "\\rfloor"
        elif decorator == "ceil":
            self.name = "\\lceil" + name + "\\rceil"

    def latex(self, mode=None):
        if mode is None:
            print(self.name)
        elif mode == "inline":
            print("$ \t" + self.name + "\t $")
        elif mode == "block":
            print("$$ \t" + self.name + "\t $$")

    def decorate(self, decorator):
        if decorator == "vec":
            self.name = "\\vec{" + self.name + "}"
        elif decorator == "mod" or decorator == "abs":
            self.name = "\\left|" + self.name + "\\right|"
        elif decorator == "brac":
            self.name = "\\left(" + self.name + "\\right)"
        elif decorator == "brace":
            self.name = "\\left\\lbrace" + self.name + "\\right\\rbrace"
        elif decorator == "angle":
            self.name = "\\left\\langle" + self.name + "\\right\\rangle"
        elif decorator == "box":
            self.name = "\\left[" + self.name + "\\right]"
        elif decorator == "floor":
            self.name = "\\lfloor" + self.name + "\\rfloor"
        elif decorator == "ceil":
            self.name = "\\lceil" + self.name + "\\rceil"

        return Term(self.name)

    def enumerate(self, number: int):
        self.name = self.name + " \\ \\dots \\ " + str(number)
        return Term(self.name)

    def __add__(self, other):
        if isinstance(other, Term):
            return Term(self.name + " + " + other.name)
        elif is_num(other):
            return Term(self.name + " + " + str(other))

    def __radd__(self, other):
        if is_num(other):
            return Term(str(other) + " + " + self.name)

    def __neg__(self):
        return Term(" - " + self.name)

    def __sub__(self, other):
        if isinstance(other, Term):
            return Term(self.name + " - " + other.name)
        elif is_num(other):
            return Term(self.name + " - " + str(other))

    def __rsub__(self, other):
        if is_num(other):
            return Term(str(other) + " - " + self.name)

    def __mul__(self, other):
        if isinstance(other, Term):
            return Term(self.name + Settings.get_mul_symbol() + other.name)
        elif isinstance(other, int) or isinstance(other, float):
            return Term(self.name + Settings.get_mul_symbol() + str(other))

    def __rmul__(self, other):
        if is_num(other):
            return Term(str(other) + Settings.get_mul_symbol() + self.name)

    def __truediv__(self, other):
        if isinstance(other, Term):
            return Term(Settings.get_frac() + "{" + self.name + "}{" + other.name + "}")
        elif is_num(other):
            return Term(Settings.get_frac() + "{" + self.name + "}{" + str(other) + "}")

    def __rtruediv__(self, other):
        if is_num(other):
            return Term(Settings.get_frac() + "{" + str(other) + "}{" + self.name + "}")

    def __pow__(self, power, modulo=None):
        if isinstance(power, Term):
            if len(self.name) > 1:
                return Term(Settings.get_left_brac() + Term(self.name + Settings.get_right_brac() + "^{" + power.name + "}"))
            else:
                return Term(self.name + "^{" + power.name + "}")
        elif is_num(power):
            if len(self.name) > 1:
                return Term(Settings.get_left_brac() + self.name + Settings.get_right_brac() + "^{" + str(power) + "}")
            else:
                return Term(self.name + "^{" + str(power) + "}")

    def __rpow__(self, other):
        if is_num(other):
            return Term(str(other) + "^{" + self.name + "}")

    def __str__(self):
        return self.name
