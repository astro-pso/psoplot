"""
PSO Colormaps
=============

This example illustrates the colormaps available in ``psoplot.cmaps`` and
shows how to use them in a plot.

Usage
-----
.. code-block:: python

    import matplotlib.pyplot as plt
    from psoplot import cmaps as pcm

    plt.imshow(data, cmap=pcm.midnight_ice)
"""

import matplotlib.pyplot as plt
import numpy as np

import psoplot.cmaps as pcm

cmap_items = list(pcm.COLORMAPS.items())

n = len(cmap_items)
fig, axes = plt.subplots(nrows=n, figsize=(6, max(1.2 * n, 1.6)))

if n == 1:
    axes = [axes]

gradient = np.linspace(0, 1, 256)
gradient = np.vstack([gradient, gradient])

for ax, (name, cmap) in zip(axes, cmap_items):
    ax.imshow(gradient, aspect="auto", cmap=cmap)
    ax.set_axis_off()
    ax.set_title(name, loc="left", fontsize=10)

plt.tight_layout()
plt.show()
