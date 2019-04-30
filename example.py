#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

import local_mpl_config as lmc

lmc.initialize()
lmc.set_colors('vibrant')

fig, ax = plt.subplots(1, 1, sharey=False, figsize=(9,6))

x = np.linspace(0, 2, 100)

ax.plot(x, x   , label=r'$x^1$')
ax.plot(x, x**2, label=r'$x^2$')
ax.plot(x, x**3, label=r'$x^3$')
ax.plot(x, x**4, label=r'$x^4$')
ax.plot(x, x**5, label=r'$x^5$')
ax.plot(x, x**6, label=r'$x^6$')

ax.set_xlabel('x label')
ax.set_ylabel('y label')

ax.set_ylim(0, 70)

ax.legend(loc=(0.05,0.6))

lmc.set_title(r'title of the graph $x^n$')
lmc.adjust_spines(ax, ['left', 'bottom'], zero=False)
lmc.adjust_ticks(ax)
lmc.savefig() # run "example.py", saves to "example.pdf"