# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:42:30 2026

@author: Admin
"""

import numpy as np
import plotly.graph_objects as go

# ===== Vẽ bằng Plotly =====
def plot_interactive(system, highlight_point=None):
    fig = go.Figure()
    x = np.linspace(-10, 10, 400)

    colors = ["red", "blue", "green", "orange", "purple"]

    for i, (a, b, c, sign) in enumerate(system):
        color = colors[i % len(colors)]

        if b != 0:
            y = (-a*x - c)/b

            # ===== Đường =====
            fig.add_trace(go.Scatter(
                x=x,
                y=y,
                mode='lines',
                name=f"{a}x + {b}y + {c} {sign} 0",
                line=dict(color=color)
            ))

            # ===== Miền =====
            if sign == ">=":
                fig.add_trace(go.Scatter(
                    x=np.concatenate([x, x[::-1]]),
                    y=np.concatenate([y, np.full_like(y, 10)]),
                    fill='toself',
                    fillcolor=color,
                    opacity=0.2,
                    line=dict(color='rgba(0,0,0,0)'),
                    showlegend=False
                ))
            else:
                fig.add_trace(go.Scatter(
                    x=np.concatenate([x, x[::-1]]),
                    y=np.concatenate([y, np.full_like(y, -10)]),
                    fill='toself',
                    fillcolor=color,
                    opacity=0.2,
                    line=dict(color='rgba(0,0,0,0)'),
                    showlegend=False
                ))

        else:
            # x = -c/a
            x_line = -c / a

            fig.add_trace(go.Scatter(
                x=[x_line]*len(x),
                y=x,
                mode='lines',
                name=f"{a}x + {b}y + {c} {sign} 0",
                line=dict(color=color)
            ))

    # ===== Highlight điểm =====
    if highlight_point:
        fig.add_trace(go.Scatter(
            x=[highlight_point[0]],
            y=[highlight_point[1]],
            mode='markers',
            marker=dict(size=10, color='black'),
            name="Điểm chọn"
        ))

    fig.update_layout(
        xaxis=dict(range=[-10,10]),
        yaxis=dict(range=[-10,10]),
        title="📊 Đồ thị (Plotly)",
        hovermode="closest"
    )

    return fig


