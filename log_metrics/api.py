# -*- coding: utf-8 -*-

"""
log_metrics.api
~~~~~~~~~~~~~~~~~

This module implements the log-metrics API.
"""

from .core import LogMetrics


def timer(name):
    return LogMetrics().timer(name)


def increment(name, val=None):
    return LogMetrics().increment(name, val)


def sample(name, val):
    return LogMetrics().sample(name, val)


def measure(name, val):
    return LogMetrics().measure(name, val)


def unique(name, val):
    return LogMetrics().unique(name, val)
