# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:12:16 2026

@author: Admin
"""

def check_point(system, x, y):
    for (a, b, c, sign) in system:
        val = a*x + b*y + c

        if sign == ">=" and val < 0:
            return False
        if sign == "<=" and val > 0:
            return False

    return True