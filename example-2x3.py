#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

import local_mpl_config as lmc

# initialize before creating a figure
lmc.initialize()

fig, axes = plt.subplots(nrows=2, ncols=3, sharex=False, sharey=False, figsize=(10,6))

# add some vertical padding between subplots
fig.tight_layout(h_pad=3.00)

x = np.linspace(0, 10)

np.random.seed(123456)

# possible color cycles to iterate through
colors = ['solarized', 'bright', 'high contrast', 'vibrant', 'muted', 'light']
k = 0

for i in range(0, 2):
  for j in range(0, 3):
    axes[i, j].set_prop_cycle(lmc.get_color_cycle(colors[k]))

    axes[i, j].plot(x, np.sin(x) + x + np.random.randn(50))
    axes[i, j].plot(x, np.sin(x) + 0.5 * x + np.random.randn(50))
    axes[i, j].plot(x, np.sin(x) + 2 * x + np.random.randn(50))
    axes[i, j].plot(x, np.sin(x) - 0.5 * x + np.random.randn(50))
    axes[i, j].plot(x, np.sin(x) - 2 * x + np.random.randn(50))
    axes[i, j].plot(x, np.sin(x) + np.random.randn(50))

    axes[i, j].set_xlabel(colors[k])
    axes[i, j].set_ylim(-25,25)

    # display only the left and bottom axes
    lmc.adjust_spines(axes[i,j], ['left', 'bottom'])
    lmc.adjust_ticks(axes[i,j])

    k = k + 1

lmc.set_suptitle("demonstrating different color cyclers")

lmc.savepdf()
lmc.savepng()
