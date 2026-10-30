import numpy as np
import pandas as pd

MU = 398600.4418          # Earth gravity constant, km^3/s^2
RE = 6378.137             # Earth radius, km
W_EARTH = 7.2921159e-5    # Earth rotation, rad/s

ALTITUDE = 500.0          # km
INCLINATION = np.radians(97.4)   # sun-synchronous at 500 km

a = RE + ALTITUDE
n = np.sqrt(MU / a**3)               # orbital angular speed, rad/s
period = 2 * np.pi / n               # seconds
speed = np.sqrt(MU / a)              # km/s

t = np.arange(0, 3 * period, 30)     # 3 orbits, one point every 30 s
u = n * t

# Position in space (inertial frame)
x = a * np.cos(u)
y = a * np.sin(u) * np.cos(INCLINATION)
z = a * np.sin(u) * np.sin(INCLINATION)

# Rotate with the Earth to get the ground position
theta = W_EARTH * t
xe = x * np.cos(theta) + y * np.sin(theta)
ye = -x * np.sin(theta) + y * np.cos(theta)

lat = np.degrees(np.arcsin(z / a))
lon = np.degrees(np.arctan2(ye, xe))

df = pd.DataFrame({"minutes": t / 60, "lat": lat, "lon": lon})
df.to_csv("orbit.csv", index=False)

print(f"Altitude : {ALTITUDE:.0f} km")
print(f"Period   : {period / 60:.1f} minutes per orbit")
print(f"Speed    : {speed:.2f} km/s")
print(f"Orbits/day: {86400 / period:.1f}")
print("Saved orbit.csv")