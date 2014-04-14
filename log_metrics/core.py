from .api import LogMetrics


def timer(name, source=None):
    return LogMetrics().timer(name, source)


def count(name, val=None, source=None):
    return LogMetrics().count(name, val, source)


def sample(name, val, source=None):
    return LogMetrics().sample(name, val, source)


def measure(name, val, source=None):
    return LogMetrics().measure(name, val, source)


def unique(name, val, source=None):
    return LogMetrics().unique(name, val, source)
