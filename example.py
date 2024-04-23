#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

import local_mpl_config as lmc

# initialize and set the colors before creating a figure
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

# manually set bounds as set_smart_bounds no longer exists
ax.set_xlim(0, 2)
ax.set_ylim(0, 70)

ax.legend(loc=(0.05,0.6))

# see local_mpl_config.set_title() documentation
lmc.set_title(r'title of the graph $x^n$')

# display only the left and bottom axes, and move them outward a bit
lmc.adjust_spines(ax, ['left', 'bottom'], amounts={'left': 10, 'bottom': 10})
lmc.adjust_ticks(ax)

# run "example.py", saves to "example.pdf"
lmc.savepdf()

# run "example.py", saves to "example.png"
lmc.savepng()
