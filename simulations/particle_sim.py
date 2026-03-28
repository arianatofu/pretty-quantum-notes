# particle_sim.py
import plotly.graph_objects as go
import numpy as np

x = np.linspace(0, 1, 500)
n_levels = 3  # first 3 energy levels
fig = go.Figure()

for n in range(1, n_levels + 1):
    y = np.sqrt(2) * np.sin(n * np.pi * x)
    fig.add_trace(go.Scatter(
        x=x, y=y, mode='lines', name=f"n={n}",
        line=dict(width=3)
    ))

fig.update_layout(
    title="Particle in a Box Wavefunctions",
    xaxis_title="x",
    yaxis_title="ψ_n(x)",
    template="plotly_white",
    plot_bgcolor='rgb(255,230,240)',
    paper_bgcolor='rgb(255,245,248)',
    font=dict(family="Georgia, serif", color="#ff69b4", size=16)
)

# Save as standalone HTML
fig.write_html("particle_box_plot.html")
print("✨ particle_box_plot.html created! Open it in a browser to see your cute plot! ✨")