import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

epsilon = 0.6
delta = 0.04
x0 = 2

t = np.linspace(0, 40, 100)


def dxdt(t, x):
    return epsilon * x - delta * x ** 2


figure, (ax1, ax2, ax3) = plt.subplots(1, 3)

delta = 0.04
x0 = 2
legend1 = []

for epsilon in range(2, 9):
    epsilon /= 10
    sol_m1 = odeint(dxdt, y0=x0, t=t, tfirst=True)

    v_sol_m1 = sol_m1.T[0]

    ax1.plot(t, v_sol_m1)
    legend1.append(f'ε = {epsilon}')

ax1.set_title('$δ = 0.04, x0 = 2$', fontsize=22)
ax1.legend(legend1, loc="best")

epsilon = 0.6
x0 = 2
legend2 = []

for delta in range(1, 8):
    delta /= 100
    sol_m1 = odeint(dxdt, y0=x0, t=t, tfirst=True)

    v_sol_m1 = sol_m1.T[0]

    ax2.plot(t, v_sol_m1)
    legend2.append(f'δ = {delta}')

ax2.set_title('$ε = 0.6, x0 = 2$', fontsize=22)
ax2.legend(legend2, loc="best")

epsilon = 0.6
delta = 0.04
legend3 = []

for x0 in range(2, 15, 2):
    sol_m1 = odeint(dxdt, y0=x0, t=t, tfirst=True)

    v_sol_m1 = sol_m1.T[0]

    ax3.plot(t, v_sol_m1)
    legend3.append(f'x0 = {x0}')

ax3.set_title('$ε = 0.6, δ = 0.04$', fontsize=22)
ax3.legend(legend3, loc="best")

plt.show()
