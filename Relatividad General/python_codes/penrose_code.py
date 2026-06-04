import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.weight": "bold",
    "text.latex.preamble": r"\usepackage{lmodern}\renewcommand{\familydefault}{\rmdefault}\bfseries"
})

def coord(t, r):
    T_aux = 0.5 * (np.tanh(t + r) + np.tanh(t - r))
    X_aux = 0.5 * (np.tanh(t + r) - np.tanh(t - r))
    return T_aux, X_aux

plt.figure(figsize=(6,6))
plt.axis('square')
plt.xlim([-0.1, 1.3])
plt.ylim([-1.2, 1.2])

# Curvas azules (variando r)
t_vals = np.arange(-10, 10.1, 0.1)
for r in np.arange(0, 5.1, 0.1):
    T = 0.5 * (np.tanh(t_vals + r) + np.tanh(t_vals - r))
    X = 0.5 * (np.tanh(t_vals + r) - np.tanh(t_vals - r))
    plt.plot(X, T, 'b')

# Curvas rojas (variando t)
r_vals = np.arange(0, 5.1, 0.1)
for t in np.arange(-5, 5.1, 0.1):
    T = 0.5 * (np.tanh(t + r_vals) + np.tanh(t - r_vals))
    X = 0.5 * (np.tanh(t + r_vals) - np.tanh(t - r_vals))
    plt.plot(X, T, 'r')

# Etiquetas
plt.text(1.15, 0.0, '$i_0$', fontsize=14)
plt.text(1.025, -0.125,  r'$(r=\infty)$', fontsize=14)
plt.text(0, 1.15, '$i_+$', fontsize=14)
plt.text(-0.125, 1.04,  r'$(t=\infty)$', fontsize=14)
plt.text(0, -1.075, '$i_-$', fontsize=14)
plt.text(-0.15,-1.2,  r'$(t=-\infty)$', fontsize=14)
plt.text(0.55, 0.55, r'$\mathcal{I}^+$', fontsize=14)
plt.text(0.55, -0.55, r'$\mathcal{I}^-$', fontsize=14)

# Rayo de luz
s_vals = np.arange(0, 5.1, 0.1)
T, X = coord(s_vals, s_vals)
plt.plot(X, T, 'k')
plt.plot(X, -T, 'k')


# Quitar marcas
plt.xticks([])
plt.yticks([])

# Quitar marco (spines)
for spine in plt.gca().spines.values():
    spine.set_visible(False)


plt.savefig("F2_penrose_diag.pdf", bbox_inches='tight', pad_inches=0)

plt.show()
