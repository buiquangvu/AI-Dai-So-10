# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:09:06 2026

@author: Admin
"""

from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations, implicit_multiplication_application
)

def parse_math(expr):
    transformations = standard_transformations + (implicit_multiplication_application,)
    expr = expr.replace("^", "**")
    return parse_expr(expr, transformations=transformations)