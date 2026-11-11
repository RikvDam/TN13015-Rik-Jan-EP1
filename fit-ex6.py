import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

q = -1.602176634e-19      # C
T, uT = 295.0, 1.0        # K
n, un = 2.0, 0.1

R1, uR1 = 10e3, 3.0       # Ohm, TODO, eigen metingen toevoegen (?)
R2 = 220.0                # Ohm TODO, eigen metingen toevoegen (?)
R3 = 100.0                # Ohm TODO, eigen metingen toevoegen (?)
f = R3 / (R2 + R3)        # spanningsdeler: U = f * U_bron

u_Ubron = 0.01            # V, TODO uit de handleiding bevestigen , voor nu gegokt
u_UR = 1e-5               # V, TODO uit de handleiding bevestigen , voor nu gegokt

# Ruwe data, TODO eigen data!
UD_voorbeeld = np.linspace(0.1, 0.6, 14)
I_voorbeeld = 1e-9 * np.expm1(19.7 * UD_voorbeeld)
U_R = I_voorbeeld * R1                         # V, over R1 (5.5 DMM)
Ubron = (UD_voorbeeld + U_R) / f               # V, spanningsbron (3.5 DMM)

# Bewerkte data
U_D = f * Ubron - U_R
I_D = U_R / R1

u_UD = np.sqrt((f * u_Ubron) ** 2 + u_UR ** 2)
u_ID = I_D * np.sqrt((u_UR / U_R) ** 2 + (uR1 / R1) ** 2)

#Plotten
plt.errorbar(U_D, I_D, xerr=u_UD, yerr=u_ID, fmt="o")
plt.yscale("log")
plt.xlabel("$U_D$ (V)")
plt.ylabel("$I_D$ (A)")
plt.show()

# Fitten
def model(U, I0, b):
    return I0 * np.expm1(b * U)

popt, pcov = curve_fit(model, U_D, I_D, p0=[1e-9, 20], sigma=u_ID, absolute_sigma=True)
I0, b = popt
ub = np.sqrt(pcov[1, 1])

plt.errorbar(U_D, I_D, xerr=u_UD, yerr=u_ID, fmt="o")
plt.plot(U_D, model(U_D, *popt))
plt.yscale("log")
plt.show()

# Boltzmann-constante (pls laat dit goed zijn)
kB = -q / (b * n * T)
u_kB = kB * np.sqrt((ub / b) ** 2 + (un / n) ** 2 + (uT / T) ** 2)
print(f"kB = ({kB:.3e} +- {u_kB:.1e}) J/K")