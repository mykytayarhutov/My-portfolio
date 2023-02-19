import matplotlib.pyplot as plt

figure, (ax1, ax2, ax3) = plt.subplots(1, 3)

t = [15.7, 13.1, 11.9, 10.9, 10.0, 9.1, 8.4]
e_list = [e/10 for e in range(2, 9)]

ax1.plot(e_list, t, '.-', color='green')
ax1.set_title('$T 0,9(ε)$', fontsize=22)

t = [13.8, 10.8, 9.6, 8.8, 7.8, 7.1, 6.2]
d_list = [d/100 for d in range(1, 8)]

ax2.plot(d_list, t, '.-', color='purple')
ax2.set_title('$T 0,9(δ)$', fontsize=22)

t = [11.7, 9.6, 7.9, 6.9, 6.2, 5.5, 4.4]
d_list = [x for x in range(2, 15, 2)]

ax3.plot(d_list, t, '.-', color='black')
ax3.set_title('$T 0,9(x0)$', fontsize=22)

plt.show()
