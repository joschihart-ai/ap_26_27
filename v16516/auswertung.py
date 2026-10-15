import matplotlib.pyplot as plt
import numpy as np

############## Einlesen von Daten

# Messwerte der Bahn in cm
l_bahn = np.genfromtxt("data/Messwerte_Bahn.txt")
l_bahn *= 1e-2

# FPS auflösung der Kamera
fps = np.genfromtxt("data/Messwerte_Kamera.txt")

# Daten zur Kugel Masse m und Umfang U
m_b, U_b = np.genfromtxt("data/Messwerte_Kugel.txt", delimiter=",", unpack=True)
m_b *= 1e4
U_b *= 1e-2

# Daten zum Zylinder Masse m, Umfang U und Wanddicke d
m_c, U_c, d_c = np.genfromtxt("data/Messwerte_Zylinder.txt", delimiter=",", unpack=True)
U_c *= 1e-2
m_c *= 1e4
d_c *= 1e-3

# Messwerte Frames der Kugel (h / cm, Anfangsframe, Endframe)
h_b, Fi_b, Ff_b = np.genfromtxt(
    "data/Messwerte_Frames_Kugel.txt", delimiter=",", unpack=True
)
h_b *= 1e-2

# Messwerte Frames der Zylinder (h / cm, Anfangsframe, Endframe)
h_c, Fi_c, Ff_c = np.genfromtxt(
    "data/Messwerte_Frames_Zylinder.txt", delimiter=",", unpack=True
)
h_c *= 1e-2

######## Print
# print(f"{fps = }")
#
# print(f"{m_b= }, {U_b = }")
# print(f"{m_c= }, {U_c = }, {d_c = }")
#
# print(f"{l_bahn = }")
#
# print(f"{h_b = }, {Fi_b = }, {Ff_b = }")
# print(f"{h_c = }, {Fi_c = }, {Ff_c = }")
########

######### Berechnungen

# Radius von der Kugel
r_b = U_b / (2 * np.pi)

# äußerer Radius des Zylinders
ro_c = U_c / (2 * np.pi)

# innerer Radius des Zylinders
ri_c = ro_c - d_c

# Trägheitsmoment der Kugel
I_b = 2 / 5 * m_b * r_b**2

# Trägheitsmoment des Zylinders
I_c = 1 / 2 * m_c * (ro_c**2 + ri_c**2)

# Ausgabe von den Trägheitsmomenten
# print("Trägheitsmoment (Kugel)")
print("Trägheitsmoment (Zylinder)")
print(I_b)

print("Trägheitsmoment (Zylinder)")
print(I_c)

# Berechne vergangene Zeit
t_b = (Ff_b - Fi_b) / fps
t_c = (Ff_c - Fi_c) / fps


# berechnung von Mittelwerten der Zeit fpr den Ball
t_b_mean = t_b.reshape(-1, 3).mean(axis=1)
h_b_mean = h_b.reshape(-1, 3)[:, 0]


# berechnung von Mittelwerten der Zeit fpr den Ball
t_c_mean = t_c.reshape(-1, 3).mean(axis=1)
h_c_mean = h_c.reshape(-1, 3)[:, 0]

# Ausgabe

print("Messwerte (Kugel)")
print("alle Zeiten")
print(t_b)
print("alle Höhen")
print(h_b)
print("Höhe")
print(h_b_mean)
print("gemittlelte Zeit")
print(t_b_mean)
print("\n")


print("Messwerte (Zylinder)")
print("alle Höhen")
print(h_c)
print("alle Zeiten")
print(t_c)
print("Höhe")
print(h_c_mean)
print("gemittlelte Zeit")
print(t_c_mean)
print("\n")


# t vs h Plot Ball
fig, ax = plt.subplots(1, 1, layout="constrained")
ax.plot(t_b_mean, h_b_mean, "k+", label="daten")
ax.set_xlabel(r"$t / s $")
ax.set_ylabel(r"$h / m $")
ax.legend()
fig.savefig("build/plot_kugel.pdf")

# t vs h Plot Zylinder
fig, ax = plt.subplots(1, 1, layout="constrained")
ax.plot(t_c_mean, h_c_mean, "k+", label="daten")
ax.set_xlabel(r"$t / s $")
ax.set_ylabel(r"$h / m $")
ax.legend()
fig.savefig("build/plot_zylinder.pdf")
