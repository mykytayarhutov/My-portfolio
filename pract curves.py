import matplotlib.pyplot as plt

figure, ([ax1, ax2, ax3], [ax4, ax5, ax6]) = plt.subplots(2, 3)

xk = [2.5, 3.75, 5, 6.25, 7.5, 8.74, 9.99]
e_list = [e/10 for e in range(2, 9)]

ax1.plot(e_list, xk, '.-', color='green')
ax1.set_title('$x_k(ε)$', fontsize=22)

xk = [30, 14.9, 9.98, 7.51, 6, 4.99, 4.28]
d_list = [d/100 for d in range(1, 8)]

ax2.plot(d_list, xk, '.-', color='purple')
ax2.set_title('$x_k(δ)$', fontsize=22)

xk = [7.52, 7.5, 7.51]
d_list = [x for x in range(2, 7, 2)]

ax3.plot(d_list, xk, '.-', color='black')
ax3.set_title('$x_k(x0)$', fontsize=22)
ax3.set_ylim([0, 15])

tk = [2.01, 3.27, 3.43, 3.28, 3.13, 2.91, 2.66]
e_list = [e/10 for e in range(2, 9)]

ax4.plot(e_list, tk, '.-', color='green')
ax4.set_title('$t_k(ε)$', fontsize=22)

tk = [5.61, 4.38, 3.65, 3.09, 2.69, 2.29, 1.95]
d_list = [d/100 for d in range(1, 8)]

ax5.plot(d_list, tk, '.-', color='purple')
ax5.set_title('$t_k(δ)$', fontsize=22)

tk = [3.09, 1.70, 0.61]
d_list = [x for x in range(2, 7, 2)]

ax6.plot(d_list, tk, '.-', color='black')
ax6.set_title('$t_k(x0)$', fontsize=22)

plt.show()
