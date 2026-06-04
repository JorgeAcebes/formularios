import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.weight": "bold",
    "text.latex.preamble": r"\usepackage{lmodern}\renewcommand{\familydefault}{\rmdefault}\bfseries"
})

plt.figure(figsize=(8,8))
plt.axis('square')
plt.xlim([-2, 2])
plt.ylim([-2, 2])

dr = 0.25
dt = 0.25        # paso normal para rojas
dt_blue = 0.1    # paso más fino para azules
r_limite = 2
t_limite = 14

t = np.arange(-t_limite, t_limite+dt, dt)
t_blue = np.arange(-t_limite, t_limite+dt_blue, dt_blue)

def dibujar_zona(signo_x, signo_y, hip=False, relleno=False, con_flechas=False):
    if hip:
        r = np.arange(1, 0-dr, -dr)
        R, T = np.meshgrid(r, t)
        rho = np.sqrt(1-R)*np.exp(0.5*R)
        X = signo_x * rho * np.sinh(0.5*T)
        Y = signo_y * rho * np.cosh(0.5*T)
    else:
        r = np.arange(1, r_limite+dr, dr)
        R, T = np.meshgrid(r, t)
        rho = np.sqrt(R-1)*np.exp(0.5*R)
        X = signo_x * rho * np.cosh(0.5*T)
        Y = signo_y * rho * np.sinh(0.5*T)

    # Dibujar rojas
    for i in range(X.shape[0]):
        plt.plot(X[i,:], Y[i,:], 'r')

    # Dibujar azules con t_blue
    if hip:
        Rb, Tb = np.meshgrid(r, t_blue)
        rho_b = np.sqrt(1-Rb)*np.exp(0.25*Rb)
        Xb = signo_x * rho_b * np.sinh(0.25*Tb)
        Yb = signo_y * rho_b * np.cosh(0.25*Tb)
    else:
        Rb, Tb = np.meshgrid(r, t_blue)
        rho_b = np.sqrt(Rb-1)*np.exp(0.25*Rb)
        Xb = signo_x * rho_b * np.cosh(0.25*Tb)
        Yb = signo_y * rho_b * np.sinh(0.25*Tb)

    # Dibujar curvas azules
    for i in range(Xb.shape[1]):
        plt.plot(Xb[:,i], Yb[:,i], 'b')

    # --- FLECHAS NEGRAS SOLO SI con_flechas=True ---
    if con_flechas:
        arrow_length = 0.15
        for i in range(0, Xb.shape[1], 1):  # más flechas (menor salto)
            # varios puntos a lo largo de cada curva
            for idx in range(5, Xb.shape[0]-5, 10):
                dX = Xb[idx+1, i] - Xb[idx-1, i]
                dY = Yb[idx+1, i] - Yb[idx-1, i]
                norm = np.sqrt(dX**2 + dY**2)
                if norm == 0:
                    continue
                dx = (dX / norm) * arrow_length
                dy = (dY / norm) * arrow_length
                plt.arrow(Xb[idx, i]-dx/2, Yb[idx, i]-dy/2, dx, dy,
                          head_width=0.04, head_length=0.07, fc='k', ec='k')

    # Rellenos
    if relleno and hip:
        Xc = np.linspace(-2, 2, 400)
        Yc = np.sqrt(1 + Xc**2)
        X_poly = np.concatenate([Xc, [2, -2]])
        Y_poly = np.concatenate([Yc, [2, 2]])
        plt.fill(X_poly, Y_poly, color='thistle', alpha=0.6, zorder=-1)
        plt.plot(Xc, Yc, color='orchid', linewidth=2)

    if relleno and hip and signo_y < 0:
        Xc = np.linspace(-2, 2, 400)
        Yc = -np.sqrt(1 + Xc**2)
        X_poly = np.concatenate([Xc, [2, -2]])
        Y_poly = np.concatenate([Yc, [-2, -2]])
        plt.fill(X_poly, Y_poly, color='gainsboro', alpha=0.75, zorder=-1)
        plt.plot(Xc, Yc, color='gainsboro', linewidth=2)

# Zona 1 (con flechas)
dibujar_zona(+1, +1, con_flechas=True)

# Zona 2 (sin flechas)
dibujar_zona(+1, +1, hip=True, relleno=True, con_flechas=False)

# Zona 3 (con flechas)
dibujar_zona(-1, -1, con_flechas=True)

# Zona 4 (sin flechas)
dibujar_zona(-1, -1, hip=True, relleno=True, con_flechas=False)

# Etiquetas
plt.text(1.2, 0,  r"\textbf{Zona I}", fontsize=12, ha='center', va='center', backgroundcolor='w')
plt.text(0, 1.2, r"\textbf{Zona II}", fontsize=12, ha='center', va='center', backgroundcolor='w')
plt.text(0.7, 1.8, "SINGULARIDAD", fontsize=12, ha='center', va='center',color='purple')
plt.text(0.69, 1.65, "AGUJERO NEGRO", fontsize=10, ha='center', va='center',color='black')
plt.text(-1.2, 0, r"\textbf{Zona III}", fontsize=12, ha='center', va='center', backgroundcolor='w')
plt.text(0, -1.2, r"\textbf{Zona IV}", fontsize=12, ha='center', va='center', backgroundcolor='w')
plt.text(0.7, -1.65, "SINGULARIDAD", fontsize=12, ha='center', va='center',color='purple')
plt.text(0.69,- 1.8, "AGUJERO BLANCO", fontsize=10, ha='center', va='center',color='dimgrey')

# Ejes
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)

# Flechas de ejes
plt.arrow(1.75, 0, 0.1, 0, head_width=0.05, head_length=0.125, fc='k')
plt.arrow(0, 1.75, 0, 0.1, head_width=0.05, head_length=0.125, fc='k')

# Etiquetas ejes
plt.text(1.85, -0.15, r"$X$", fontsize=14, ha="left", va="center")
plt.text(-0.15, 1.85, r"$T$", fontsize=14, ha="center", va="bottom")

# Quitar marcas
plt.xticks([])
plt.yticks([])

# plt.show()

plt.savefig("diagrama.pdf", bbox_inches='tight', pad_inches=0)
