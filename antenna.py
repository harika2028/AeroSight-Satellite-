import numpy as np
import matplotlib.pyplot as plt

C = 299_792_458        # speed of light, m/s
F = 437e6              # frequency, Hz (UHF)
lam = C / F            # wavelength
arm = 0.95 * lam / 4   # one arm, shortened 5% for real wire


def pattern(theta):
    """Half-wave dipole field pattern (theta measured from the antenna axis)."""
    return np.abs(np.cos(np.pi / 2 * np.cos(theta)) / np.sin(theta))


theta = np.linspace(0.001, np.pi - 0.001, 400)
E = pattern(theta)
E = E / E.max()

# Half-power beamwidth (where power falls to half)
inside = theta[E >= 0.7071]
hpbw = np.degrees(inside.max() - inside.min())

print(f"Frequency     : {F / 1e6:.0f} MHz")
print(f"Wavelength    : {lam * 100:.1f} cm")
print(f"Total length  : {2 * arm * 100:.1f} cm ({arm * 100:.1f} cm per arm)")
print(f"Peak gain     : 2.15 dBi (ideal half-wave dipole)")
print(f"Beamwidth     : {hpbw:.0f} degrees")

fig = plt.figure(figsize=(11, 5))

# Side view (polar)
ax1 = fig.add_subplot(1, 2, 1, projection="polar")
angles = np.concatenate([theta, 2 * np.pi - theta[::-1]])
values = np.concatenate([E, E[::-1]])
ax1.plot(angles, values, linewidth=2)
ax1.set_theta_zero_location("N")
ax1.set_theta_direction(-1)
ax1.set_title("Side view: signal strength\n(0 degrees = along the antenna)")

# 3D donut shape
ax2 = fig.add_subplot(1, 2, 2, projection="3d")
phi = np.linspace(0, 2 * np.pi, 60)
TH, PH = np.meshgrid(theta, phi)
R = pattern(TH)
R = R / R.max()
ax2.plot_surface(R * np.sin(TH) * np.cos(PH),
                 R * np.sin(TH) * np.sin(PH),
                 R * np.cos(TH), cmap="viridis", linewidth=0)
ax2.set_title("3D radiation pattern")
ax2.set_box_aspect((1, 1, 1))

plt.tight_layout()
plt.savefig("antenna_pattern.png", dpi=150)
plt.show()