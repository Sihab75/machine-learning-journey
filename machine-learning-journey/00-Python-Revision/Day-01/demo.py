
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Petal generation
def petal(u, v, phi, open_factor=1.0):
    theta = open_factor * u**1.2 * 1.4

    width = np.sin(np.pi * u**0.8)

    # Petal length and width
    r = 2.5 * u

    # Curved petal surface
    x = r * np.cos(theta) 
    y = v * width * 0.85
    z = 0.45 * np.sin(np.pi * u) + 0.2 * u

    # Rotate each petal around Z axis
    X = x * np.cos(phi) - y * np.sin(phi)
    Y = x * np.sin(phi) + y * np.cos(phi)

    return X, Y, z


# Create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")

# Custom flower colors
cmap = LinearSegmentedColormap.from_list(
    "lily",
    ["#ffffff", "#ffb6d9", "#ff4fa3", "#8b008b"]
)

# Generate petal coordinates
u = np.linspace(0.01, 1, 100)
v = np.linspace(-1, 1, 60)

U, V = np.meshgrid(u, v)

# Create 6 petals
for i in range(6):
    phi = np.radians(i * 60)

    X, Y, Z = petal(U, V, phi)

    ax.plot_surface(
        X, Y, Z,
        cmap=cmap,
        edgecolor="none",
        alpha=0.95,
        antialiased=True
    )

# Flower center
ax.scatter(
    0, 0, 0.45,
    color="gold",
    s=150,
    depthshade=False
)

# Flower stamens
for i in range(6):
    angle = np.radians(i * 60)

    x = 0.35 * np.cos(angle)
    y = 0.35 * np.sin(angle)

    ax.plot(
        [0, x],
        [0, y],
        [0.45, 0.75],
        color="gold",
        linewidth=2
    )

    ax.scatter(
        x, y, 0.75,
        color="orange",
        s=35
    )

# Appearance
ax.set_facecolor("#080016")
fig.patch.set_facecolor("#080016")

ax.set_axis_off()
ax.set_box_aspect([1, 1, 0.55])

ax.view_init(elev=30, azim=45)

plt.title(
    "Glowing Lily Flower",
    color="white",
    fontsize=20,
    pad=20
)

plt.tight_layout()
plt.show()
