.. psoplot documentation master file, created by
   sphinx-quickstart on Mon Jun 24 10:13:58 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to psoplot's documentation!
===================================

PSO Plotting Utils

Installation
------------
.. code-block:: bash

   pip install psoplot

Usage
-----

If you only want to use a style, you can use the following code:
.. code-block:: python

   import matplotlib.pyplot as plt
   import psoplot

   plt.style.use("psoplot.aanda_publication")

   # [Your plotting code here]


If you want to use e.g. a convenient wrapper for generating subplots, you can use the following code:
.. code-block:: python

   import psoplot.aanda_plot as aplt

   fig, (ax1, ax2) = aplt.subplots(2, 1)


Which is essentially a wrapper around ``plt.subplots`` with some convenience settings regarding the
size of the figure.

Available styles
----------------
* ``psoplot.aanda_publication``: A style for A&A publication
* ``psoplot.aas_publication``: A style for AAS publication, e.g. ApJ, ApJL, ApJS

For example plots, see the example page.

CLI: make-movie
---------------
Use ``make-movie`` to build an MP4 from image frames sharing the same base name.

.. code-block:: bash

   make-movie frame_ --extension png --fps 24 --output movie.mp4

The command searches for matching frames like ``frame_*.<extension>`` in the same directory,
sorts them, and runs ``ffmpeg`` to produce the MP4 file.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   colormaps

.. toctree::
   :maxdepth: 2
   :caption: Examples:

   styles_examples/index
   colormaps_examples/index


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
