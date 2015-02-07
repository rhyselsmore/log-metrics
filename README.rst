log-metrics
===========

log-metrics is a tiny metrics logger, based on the [l2met](https://github.com/ryandotsmith/l2met) format. Meant for use on
Heroku, this allows you to send custom metrics to `Librato <http://librato.com>`_.

You can find more information on these custom metrics `here <https://devcenter.heroku.com/articles/librato#custom-log-based-metrics>`_.


Installation
------------

.. code-block:: bash

    $ pip install log-metrics


Usage
-----

Everything takes place from the log_metrics module, which can be imported like
so:

.. code-block:: pycon

    >>> import log_metrics


Samples
*******

.. code-block:: pycon

    >>> log_metrics.sample('process.foo.memory.mb', '52.54')
    sample#process.foo.memory.mb=52.54


Measurements
************

.. code-block:: pycon

    >>> log_metrics.measure('myfoo.ms', '150')
    measure#myfoo.ms=150


Uniques
*******

.. code-block:: pycon

    >>> log_metrics.unique('user.clicked', 'bob')
    unique#user.clicked=bob
    >>> log_metrics.unique('user.clicked', 'joey')
    unique#user.clicked=joey
    >>> log_metrics.unique('user.clicked', 'jenny')
    unique#user.clicked=jenny


Counters
********

.. code-block:: pycon

    >>> log_metrics.increment('myfoo')
    count#myfoo=1


.. code-block:: pycon

    >>> log_metrics.increment('myfoo', 3)
    count#myfoo=3


Timers
******

.. code-block:: pycon

    >>> with log_metrics.timer('my-timed-context'):
    ...     time.sleep(1)
    measure#my-timed-context.ms=1001.20


.. code-block:: pycon

    >>> @log_metrics.timer('my-timed-decorator'):
    ... def my_func():
    ...     time.sleep(0.5)
    >>> my_func()
    measure#my-timed-decorator.ms=504.20


Metric Groups
*************

.. code-block:: pycon

    >>> with log_metrics.group() as g:
    ...     g.measure('my-measurement', 2)
    ...     g.increment('my-counter')
    measure#my-measurement=2 count#my-counter=1


.. code-block:: pycon

    >>> g = log_metrics.group()
    >>> g.measure('my-measurement', 2)
    >>> g.increment('my-counter')
    >>> g.emit()
    measure#my-measurement=2 count#my-counter=1


Sources and Prefixes
********************

Sources and prefixes can be defined like so:

.. code-block:: pycon

    >>> log_metrics.increment('my-counter', prefix='awesome')
    count#awesome.my-counter=1
    >>> log_metrics.measure('my-measurement', 50, source='testing')
    source=testing measure#my-measurement=50


These arguments are also supported for group functions:

.. code-block:: pycon

    >>> g = log_metrics.group(prefix='my-prefix', source='my-metric-source')
    >>> g.increment('my-amount')
    >>> g.increment('my-measurement')
    >>> g.emit()
    source=my-metric-source count#my-prefix.my-amount=1 count#my-prefix.my-amount1=1 count#my-prefix.my-amount2=1
