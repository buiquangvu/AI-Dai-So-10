# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:51:10 2026

@author: Admin
"""

import random

def generate_system():
    system = []
    for _ in range(2):
        a = random.randint(-5, 5) or 1
        b = random.randint(-5, 5) or 1
        c = random.randint(-10, 10)
        sign = random.choice([">=", "<="])
        system.append((a, b, c, sign))
    return system