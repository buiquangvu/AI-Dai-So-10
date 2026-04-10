# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:52:00 2026

@author: Admin
"""

from sympy import symbols, solve

x, y = symbols('x y')

def solve_inequality(a, b, c, sign):
    return f"{a}x + {b}y + {c} {sign} 0"


def solve_system(system):
    return [solve_inequality(*ineq) for ineq in system]