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

   pip install pso_plot

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

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. toctree::
   :maxdepth: 2
   :caption: Examples:

   examples/index


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
