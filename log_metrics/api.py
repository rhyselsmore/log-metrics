# -*- coding: utf-8 -*-

"""
log_metrics.api
~~~~~~~~~~~~~~~~~

This module implements the log-metrics API.
"""

from .api import LogMetrics


def timer(name, source=None):
    return LogMetrics().timer(name, source)


def increment(name, val=None, source=None):
    return LogMetrics().increment(name, val, source)


def sample(name, val, source=None):
    return LogMetrics().sample(name, val, source)


def measure(name, val, source=None):
    return LogMetrics().measure(name, val, source)


def unique(name, val, source=None):
    return LogMetrics().unique(name, val, source)
