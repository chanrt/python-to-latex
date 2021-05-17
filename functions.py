from term import Term
from settings import Settings
from commons import *


# trigonometric functions
def sin(term):
    if isinstance(term, Term):
        return Term("\\sin" + Settings.get_left_brac() + term.name + Settings.get_right_brac())
    elif is_num(term):
        return Term("\\sin" + Settings.get_left_brac() + str(term) + Settings.get_right_brac())


def cos(term):
    if isinstance(term, Term):
        return Term("\\cos" + Settings.get_left_brac() + term.name + Settings.get_right_brac())
    elif is_num(term):
        return Term("\\cos" + Settings.get_left_brac() + str(term) + Settings.get_right_brac())


def tan(term):
    if isinstance(term, Term):
        return Term("\\tan" + Settings.get_left_brac() + term.name + Settings.get_right_brac())
    elif is_num(term):
        return Term("\\tan" + Settings.get_left_brac() + str(term) + Settings.get_right_brac())


def cot(term):
    if isinstance(term, Term):
        return Term("\\cot" + Settings.get_left_brac() + term.name + Settings.get_right_brac())
    elif is_num(term):
        return Term("\\cot" + Settings.get_left_brac() + str(term) + Settings.get_right_brac())


def sec(term):
    if isinstance(term, Term):
        return Term("\\sec" + Settings.get_left_brac() + term.name + Settings.get_right_brac())
    elif is_num(term):
        return Term("\\sec" + Settings.get_left_brac() + str(term) + Settings.get_right_brac())


def csc(term):
    if isinstance(term, Term):
        return Term("\\csc" + Settings.get_left_brac() + term.name + Settings.get_right_brac())
    elif is_num(term):
        return Term("\\csc" + Settings.get_left_brac() + str(term) + Settings.get_right_brac())


# inverse trigonometric functions
def arcsin(term):
    if isinstance(term, Term):
        return Term("\\arcsin" + Settings.get_left_brac() + term.name + Settings.get_right_brac())
    elif is_num(term):
        return Term("\\arcsin" + Settings.get_left_brac() + str(term) + Settings.get_right_brac())


def arccos(term):
    if isinstance(term, Term):
        return Term("\\arccos" + Settings.get_left_brac() + term.name + Settings.get_right_brac())
    elif is_num(term):
        return Term("\\arccos" + Settings.get_left_brac() + str(term) + Settings.get_right_brac())


def arctan(term):
    if isinstance(term, Term):
        return Term("\\arctan" + Settings.get_left_brac() + term.name + Settings.get_right_brac())
    elif is_num(term):
        return Term("\\arctan" + Settings.get_left_brac() + str(term) + Settings.get_right_brac())


# hyperbolic functions
def sinh(term):
    if isinstance(term, Term):
        return Term("\\sinh" + Settings.get_left_brac() + term.name + Settings.get_right_brac())
    elif is_num(term):
        return Term("\\sinh" + Settings.get_left_brac() + str(term) + Settings.get_right_brac())


def cosh(term):
    if isinstance(term, Term):
        return Term("\\cosh" + Settings.get_left_brac() + term.name + Settings.get_right_brac())
    elif is_num(term):
        return Term("\\cosh" + Settings.get_left_brac() + str(term) + Settings.get_right_brac())


def tanh(term):
    if isinstance(term, Term):
        return Term("\\tanh" + Settings.get_left_brac() + term.name + Settings.get_right_brac())
    elif is_num(term):
        return Term("\\tanh" + Settings.get_left_brac() + str(term) + Settings.get_right_brac())


# logarithmic functions
def ln(term):
    if isinstance(term, Term):
        return Term("\\ln" + Settings.get_left_brac() + term.name + Settings.get_right_brac())
    elif is_num(term):
        return Term("\\ln" + Settings.get_left_brac() + str(term) + Settings.get_right_brac())


def log(term, base=""):
    if isinstance(term, Term):
        if base == "":
            return Term("\\log" + Settings.get_left_brac() + term.name + Settings.get_right_brac())
        else:
            return Term("\\log_" + str(base) + Settings.get_left_brac() + term.name + Settings.get_right_brac())
    elif is_num(term):
        if base == "":
            return Term("\\log" + Settings.get_left_brac() + str(term) + Settings.get_right_brac())
        else:
            return Term("\\log_" + str(base) + Settings.get_left_brac() + str(term) + Settings.get_right_brac())


def exp(term):
    if isinstance(term, Term):
        return Term("exp" + Settings.get_left_brac() + term.name + Settings.get_right_brac())
    elif is_num(term):
        return Term("exp" + Settings.get_left_brac() + str(term) + Settings.get_right_brac())
