Custom colormaps
================

psoplot provides a small collection of custom Matplotlib colormaps under
``psoplot.cmaps``. Import the module and pass a colormap to any Matplotlib
function that accepts the ``cmap`` argument.

Usage
-----
.. code-block:: python

   import matplotlib.pyplot as plt
   from psoplot import cmaps as pcm

   plt.imshow(data, cmap=pcm.BlackBlueWhite)

Available colormaps
-------------------
The module exposes named colormaps and a small helper API:

.. code-block:: python

   import psoplot.cmaps as pcm

   pcm.list_colormaps()  # -> ("BlackBlueWhite", ...)
   pcm.get_colormap("BlackBlueWhite")

Defining new colormaps
----------------------
Colormaps are defined using ``LinearSegmentedColormap.from_list``. For
example:

.. code-block:: python

   from matplotlib.colors import LinearSegmentedColormap

   BlackBlueWhite = LinearSegmentedColormap.from_list(
       "BlackBlueWhite",
       (
           # Edit this gradient at https://eltos.github.io/gradient/#000000-00AAB2-E7E4CA
           (0.000, (0.000, 0.000, 0.000)),
           (0.500, (0.000, 0.667, 0.698)),
           (1.000, (0.906, 0.894, 0.792)),
       ),
   )
