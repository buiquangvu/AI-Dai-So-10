# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:11:43 2026

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_system(system):
    fig, ax = plt.subplots()

    x = np.linspace(-10, 10, 400)
    colors = ["red", "blue", "green", "orange", "purple"]

    for i, (a, b, c, sign) in enumerate(system):
        color = colors[i % len(colors)]

        if b != 0:
            y = (-a*x - c)/b
            ax.plot(x, y, color=color)

            # ===== Tô miền =====
            if sign == ">=":
                ax.fill_between(x, y, 10, color=color, alpha=0.2)
            else:
                ax.fill_between(x, y, -10, color=color, alpha=0.2)

        else:
            # Đường thẳng đứng
            x_line = -c / a
            ax.axvline(x=x_line, color=color)

            if sign == ">=":
                ax.fill_betweenx(np.linspace(-10,10,400), x_line, 10, color=color, alpha=0.2)
            else:
                ax.fill_betweenx(np.linspace(-10,10,400), -10, x_line, color=color, alpha=0.2)

    ax.axhline(0)
    ax.axvline(0)
    ax.grid(True)

    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)

    return fig