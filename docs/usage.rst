=====
Usage
=====

To use Project Test in a project::

    import project_test


Scientific libraries conventionally use radians. Numpy provides convenience
functions for converting between radians and degrees.

.. autofunction:: project_test.apps.snell

.. code-block:: python

   import numpy as np


   np.deg2rad(90)  # pi / 2
   np.rad2deg(np.pi / 2)  # 90.0

.. math::

    \int_0^a x\,dx = \frac{1}{2}a^2


.. plot::

   import matplotlib.pyplot as plt
   fig, ax = plt.subplots()
   ax.plot([1, 1, 2, 3, 5, 8])

.. ipython:: python

   1 + 1

.. NOTE: RTD does not allow modules that requires C code to
   run on their server. Therefore any module, such as numpy,
   that rely on C code cannot be imported and executed using
   ipython on RTD servers.
.. .. ipython:: python
    from project_test.apps.snell import snell
    snell(1, 1, 1)

.. autosummary::
   :toctree: _build/

   project_tree.apps.snell
