import plotly.graph_objects as go
import numpy as np
from scipy.special import hermite
from math import factorial, pi, sqrt

x = np.linspace(-3, 3, 500)
n_levels = 3  # first 3 energy levels
fig = go.Figure()

# Normalized wavefunctions for harmonic oscillator
for n in range(n_levels):
    Hn = hermite(n)
    psi_n = (1/sqrt(2**n * factorial(n))) * (1/pi)**0.25 * np.exp(-x**2/2) * Hn(x)
    fig.add_trace(go.Scatter(
        x=x, y=psi_n, mode='lines', name=f"n={n}", line=dict(width=3)
    ))

fig.update_layout(
    title="Harmonic Oscillator Wavefunctions",
    xaxis_title="Position x",
    yaxis_title="ψ_n(x)",
    template="plotly_white",
    plot_bgcolor='rgb(255,230,240)',
    paper_bgcolor='rgb(255,245,248)',
    font=dict(family="Georgia, serif", color="#ff69b4", size=16)
)

fig.write_html("harmonic_plot.html")
print("✨ harmonic_plot.html created! Open it in a browser to see your cute plot! ✨")