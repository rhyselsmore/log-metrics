log-metrics
===========

log-metrics is a tiny metrics logger, based on the l2met format.


Installation
------------

.. code-block:: bash

    $ pip install log-metrics


Usage
-----

Everything takes place from the log_metrics module, which can be imported like
so

.. code-block:: pycon

    >>> import log_metrics


Counts
******

.. code-block:: pycon

    >>> log_metrics.count('myfoo')
    count#myfoo=1


.. code-block:: pycon
    >>> log_metrics.count('myfoo', 3)
    count#myfoo=3
