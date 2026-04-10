# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 21:59:40 2026

@author: Admin
"""

import numpy as np
from utils.checker import check_point

def check_region(system, polygon):
    for (x, y) in polygon:
        if not check_point(system, x, y):
            return False
    return True