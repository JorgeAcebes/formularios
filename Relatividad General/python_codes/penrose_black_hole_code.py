import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.weight": "bold",
    "text.latex.preamble": r"\usepackage{lmodern}\renewcommand{\familydefault}{\rmdefault}\bfseries"
})

escala = 3.5
dr = 0.04
dt = 0.3
r_limite = 15
t_limite = 9

plt.figure(figsize=(20, 25))   # ancho=10, alto=6 pulgadas
plt.axis("square")
plt.xlim([-escala, escala])
plt.ylim([-escala*0.55, escala*0.55])

# ---------- Funciones auxiliares ----------
def zona_I(r_vals, t_vals):
    R_all, tao_all = [], []
    for r in r_vals:
        t = t_vals
        X = np.sqrt(r - 1) * np.exp(0.5 * r) * np.cosh(0.5 * t)
        T = np.sqrt(r - 1) * np.exp(0.5 * r) * np.sinh(0.5 * t)
        p, q = X + T, -X + T
        u, v = np.arctan(p), np.arctan(q)
        tao, R = u + v, u - v
        plt.plot(R, tao, color=[0, 0.4, 0.6])
    for t in t_vals:
        r = r_vals
        X = np.sqrt(r - 1) * np.exp(0.5 * r) * np.cosh(0.5 * t)
        T = np.sqrt(r - 1) * np.exp(0.5 * r) * np.sinh(0.5 * t)
        p, q = X + T, -X + T
        u, v = np.arctan(p), np.arctan(q)
        tao, R = u + v, u - v
        plt.plot(R, tao, "r")

def zona_II(r_vals, t_vals):
    for r in r_vals:
        t = t_vals
        X = np.sqrt(1 - r) * np.exp(0.5 * r) * np.sinh(0.5 * t)
        T = np.sqrt(1 - r) * np.exp(0.5 * r) * np.cosh(0.5 * t)
        p, q = X + T, -X + T
        u, v = np.arctan(p), np.arctan(q)
        tao, R = u + v, u - v
        plt.plot(R, tao, color=[0, 0.4, 0.6])
    for t in t_vals:
        r = r_vals
        X = np.sqrt(1 - r) * np.exp(0.5 * r) * np.sinh(0.5 * t)
        T = np.sqrt(1 - r) * np.exp(0.5 * r) * np.cosh(0.5 * t)
        p, q = X + T, -X + T
        u, v = np.arctan(p), np.arctan(q)
        tao, R = u + v, u - v
        plt.plot(R, tao, "r")

def zona_III(r_vals, t_vals):
    for r in r_vals:
        t = t_vals
        X = -np.sqrt(r - 1) * np.exp(0.5 * r) * np.cosh(-0.5 * t)
        T = -np.sqrt(r - 1) * np.exp(0.5 * r) * np.sinh(-0.5 * t)
        p, q = X + T, -X + T
        u, v = np.arctan(p), np.arctan(q)
        tao, R = u + v, u - v
        plt.plot(R, tao, color=[0, 0.4, 0.6])
    for t in t_vals:
        r = r_vals
        X = -np.sqrt(r - 1) * np.exp(0.5 * r) * np.cosh(-0.5 * t)
        T = -np.sqrt(r - 1) * np.exp(0.5 * r) * np.sinh(-0.5 * t)
        p, q = X + T, -X + T
        u, v = np.arctan(p), np.arctan(q)
        tao, R = u + v, u - v
        plt.plot(R, tao, "r")

def zona_IV(r_vals, t_vals):
    for r in r_vals:
        t = t_vals
        X = -np.sqrt(1 - r) * np.exp(0.5 * r) * np.sinh(0.5 * t)
        T = -np.sqrt(1 - r) * np.exp(0.5 * r) * np.cosh(0.5 * t)
        p, q = X + T, -X + T
        u, v = np.arctan(p), np.arctan(q)
        tao, R = u + v, u - v
        plt.plot(R, tao, color=[0, 0.4, 0.6])
    for t in t_vals:
        r = r_vals
        X = -np.sqrt(1 - r) * np.exp(0.5 * r) * np.sinh(0.5 * t)
        T = -np.sqrt(1 - r) * np.exp(0.5 * r) * np.cosh(0.5 * t)
        p, q = X + T, -X + T
        u, v = np.arctan(p), np.arctan(q)
        tao, R = u + v, u - v
        plt.plot(R, tao, "r")

# ---------- Ejecución ----------
r_vals1 = np.arange(1.0000001, r_limite, dr)
r_vals2 = np.arange(0.999999, 0.00001, -dr)
t_vals = np.arange(-t_limite, t_limite, dt)

zona_I(r_vals1, t_vals)
zona_II(r_vals2, t_vals)
zona_III(r_vals1, t_vals)
zona_IV(r_vals2, t_vals)

# ---------- Textos ----------
plt.text(3.1, 0.1, '$i_0$', fontsize=14)
plt.text(1.5, 1.7, '$i_+$', fontsize=14)
plt.text(1.5, -1.7, '$i_-$', fontsize=14)
plt.text(2.3, 0.9, r'$\mathcal{I}^+$', fontsize=14)
plt.text(2.3, -1, r'$\mathcal{I}^-$', fontsize=14)

plt.text(-3.2, 0.1, '$i_0$', fontsize=14)
plt.text(-1.5, 1.7, '$i_+$', fontsize=14)
plt.text(-1.5, -1.7, '$i_-$', fontsize=14)
plt.text(-2.4, 0.9, r'$\mathcal{I}^+$', fontsize=14)
plt.text(-2.4, -1, r'$\mathcal{I}^-$', fontsize=14)

# ---------- Singularidad ----------
s_vals = np.arange(-np.pi/2, np.pi/2, 0.1)
X = s_vals
Tup = np.full_like(s_vals, np.pi/2)
Tdown = -Tup

plt.plot(X, Tup, "go", linewidth=2)    # Línea verde, punteada, más gruesa
plt.plot(X, Tdown, "go", linewidth=2)

# Ejes
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)

# Flechas de ejes
plt.arrow(3.275, 0, 0.1, 0, head_width=0.05, head_length=0.125, fc='k')
plt.arrow(0, 1.7, 0, 0.1, head_width=0.05, head_length=0.125, fc='k')

# Etiquetas ejes
plt.text(3.35, -0.15, r"$X$", fontsize=14, ha="left", va="center")
plt.text(-0.15, 1.8, r"$T$", fontsize=14, ha="center", va="bottom")

# Etiquetas
plt.text(1.6, 0,  r"\textbf{Zona I}", fontsize=12, ha='center', va='center', backgroundcolor='w')
plt.text(0, 1.2, r"\textbf{Zona II}", fontsize=12, ha='center', va='center', backgroundcolor='w')
plt.text(0.7, 1.8, "SINGULARIDAD", fontsize=14, ha='center', va='center',color='purple')
plt.text(0.69, 1.65, "AGUJERO NEGRO", fontsize=12, ha='center', va='center',color='black')
plt.text(-1.6, 0, r"\textbf{Zona III}", fontsize=12, ha='center', va='center', backgroundcolor='w')
plt.text(0, -1.2, r"\textbf{Zona IV}", fontsize=12, ha='center', va='center', backgroundcolor='w')
plt.text(0.7, -1.7, "SINGULARIDAD", fontsize=14, ha='center', va='center',color='purple')
plt.text(0.69,- 1.85, "AGUJERO BLANCO", fontsize=12, ha='center', va='center',color='dimgrey')




# Quitar marcas
plt.xticks([])
plt.yticks([])

# Quitar marco (spines)
for spine in plt.gca().spines.values():
    spine.set_visible(False)


plt.savefig("F3_penrose_diag_schwar.pdf", bbox_inches='tight', pad_inches=0)

#plt.show()
