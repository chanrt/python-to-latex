from term import Term
from commons import *


def limit(expression, variable, tends_to):
    string = "\\lim\\limits_{" + variable.name + " \\rightarrow "

    if is_num(tends_to):
        string += str(tends_to) + "} "
    elif isinstance(tends_to, Term):
        string += tends_to.name + "} "

    return Term(string + " {" + expression.name + "} ")


def derivative(of, respect_to, order=1, partial=False):
    if partial:
        diff_string = "\\partial"
    else:
        diff_string = "d"

    if order == 1:
        order_string = " "
    else: 
        order_string = "^{" + str(order) + "} "

    return Term("\\frac{" + diff_string + order_string + of.name + "}{" + diff_string + respect_to.name + order_string + "}")


def integral(expression, variables, lower_limit=None, upper_limit=None, num_integrals = 1):
    string = ""
    for num in range(0, num_integrals):
        string += "\\int"

    if is_num(lower_limit):
        string += "_{" + str(lower_limit) + "}"
    elif isinstance(lower_limit, Term):
        string += "_{" + lower_limit.name + "}"
    elif lower_limit is None:
        pass

    if is_num(upper_limit):
        string += "^{" + str(upper_limit) + "}"
    elif isinstance(upper_limit, Term):
        string += "^{" + upper_limit.name + "}"
    elif upper_limit is None:
        pass

    string = string + " {" + expression.name + "} \\ "

    for variable in variables:
        string += " d" + variable.name

    return Term(string)


def limits(expression, lower_limit, upper_limit):
    string = expression.decorate("abs").name

    if is_num(lower_limit):
        string += "_{" + str(lower_limit) + "}"
    elif isinstance(lower_limit, Term):
        string += "_{" + lower_limit.name + "}"

    if is_num(upper_limit):
        string += "^{" + str(upper_limit) + "}"
    elif isinstance(upper_limit, Term):
        string += "^{" + upper_limit.name + "}"
    elif upper_limit is None:
        pass

    return Term(string)


