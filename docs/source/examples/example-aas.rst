.. _example-aas:

AAS Publication Style
=================================

This example demonstrates the use of the ``psoplot.aas_publication`` style.

.. code-block:: python

   import matplotlib.pyplot as plt
   import numpy as np
   import psoplot # Import psoplot to register the styles

   plt.style.use("psoplot.aas_publication")

   # Data for plotting
   x = np.linspace(0, 10, 100)
   y = np.cos(x)

   fig, ax = plt.subplots()
   ax.plot(x, y)

   ax.set(xlabel='position (m)', ylabel='amplitude',
          title='AAS Publication Style Example')
   ax.grid(True)

   plt.show()
