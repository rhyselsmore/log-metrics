# -*- coding: utf-8 -*-

"""
log_metrics.api
~~~~~~~~~~~~~~~~~

This module implements the log-metrics API.
"""

from .core import MetricsLogger, GroupMetricsLogger


def timer(name, **kwargs):
    return MetricsLogger(**kwargs).timer(name)


def increment(name, val=None, **kwargs):
    return MetricsLogger(**kwargs).increment(name, val)


def sample(name, val, **kwargs):
    return MetricsLogger(**kwargs).sample(name, val)


def measure(name, val, **kwargs):
    return MetricsLogger(**kwargs).measure(name, val)


def unique(name, val, **kwargs):
    return MetricsLogger(**kwargs).unique(name, val)


def group(**kwargs):
    return GroupMetricsLogger(**kwargs)