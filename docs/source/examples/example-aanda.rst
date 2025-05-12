.. _example-aanda:

A&A Publication Style
=================================

This example demonstrates the use of the ``psoplot.aanda_publication`` style.

.. code-block:: python

   import matplotlib.pyplot as plt
   import numpy as np
   import psoplot # Import psoplot to register the styles

   plt.style.use("psoplot.aanda_publication")

   # Data for plotting
   t = np.arange(0.0, 2.0, 0.01)
   s = 1 + np.sin(2 * np.pi * t)

   fig, ax = plt.subplots()
   ax.plot(t, s)

   ax.set(xlabel='time (s)', ylabel='voltage (mV)',
          title='A&A Publication Style Example')
   ax.grid()

   plt.show()
