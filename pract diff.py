import matplotlib.pyplot as plt

figure, (ax1, ax2) = plt.subplots(1, 2)

calc = [4.99, 7.50, 9.99, 12.50, 15, 17.5, 20]
e_list = [e/10 for e in range(2, 9)]

ax1.plot(e_list, calc, '.-', label='x_CT(ε)', color='green')
ax1.set_title('$δ = 0.04, x0 = 2$', fontsize=22)
ax1.legend(loc='best')

calc = [60, 29.99, 19.99, 15, 12, 10, 8.50]
d_list = [d/100 for d in range(1, 8)]

ax2.plot(d_list, calc, '.-', label='x_CT(δ)', color='purple')
ax2.set_title('$ε = 0.6, x0 = 2$', fontsize=22)
ax2.legend(loc='best')

plt.show()
