"""
A&A Publication Style Example
=============================

This example demonstrates how to use the A&A publication style
through the `aanda_plot` wrapper.

.. warning::

    Due to the way matplotlib handles figure sizes, you need to
    specify the `bbox_inches="tight"` parameter when saving the figure.
    Do NOT use `plt.tight_layout()` before saving, as this will
    mess up the aspect ratio. matplotlib just does not support
    calling this outside of the `plt.savefig()` function.
    In this example, `plt.tight_layout()` is used to avoid
    cutting off the labels when displaying the figure. This
    changes the aspect ratio of the figure, in a production
    environment it should respect the aspect ratio of the figure.

"""

import matplotlib.pyplot as plt
import numpy as np

import psoplot.aanda_plot as aplt

# Alternatively, only import the stylesheet without
# the subplots function:
# > import psoplot
# > plt.style.use("psoplot.aanda_publication")

# make the data
np.random.seed(3)
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))
# size and color:
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))

# plot
fig, ax = aplt.subplots(1, 1)

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100, label=r"$\mathcal{N}(x,y)$")

ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

ax.set_xlabel(r"$x$ (cm)")
ax.set_ylabel(r"$y$ (cm)")

ax.set_title(r"A\&A Publication Style")

ax.legend()

### IMPORTANT ###
# To get the correct aspect ratio etc, you need to specify
# the `bbox_inches="tight"` parameter when saving the figure.
# Do NOT use `plt.tight_layout()` before saving, as this will
# mess up the aspect ratio.
# matplotlib just does not support calling this outside
# of the `plt.savefig()` function.

# > plt.savefig("aanda_style_example.png", bbox_inches="tight")

plt.tight_layout()  # Do NOT use this before saving!
plt.show()
