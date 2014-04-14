import time
import logging
from functools import wraps
import sys

EXC = (None, None, None)


class ContextDecorator(object):
    before = None
    after = None

    def __call__(self, f):
        @wraps(f)
        def inner(*args, **kw):
            if self.before is not None:
                self.before()
            exc = EXC
            try:
                result = f(*args, **kw)
            except Exception:
                exc = sys.exc_info()
            catch = False
            if self.after is not None:
                catch = self.after(*exc)
            if not catch and exc is not EXC:
                _reraise(*exc)
            return result
        return inner

    def __enter__(self):
        if self.before is not None:
            return self.before()

    def __exit__(self, *exc):
        catch = False
        if self.after is not None:
            catch = self.after(*exc)
        return catch


class Timer(ContextDecorator):
    def __init__(self, name, source, metrics):
        self.name = name
        self.metrics = metrics
        self.source = source

    def before(self):
        self.start = time.time()

    def after(self, *exc):
        duration = (time.time() - self.start)*1000
        self.metrics.measure(self.name, "%sms" % duration, self.source)


class LogMetrics(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(message)s'))
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)

    def _log(self, source, prefix, name, value):
        val = "%s#%s=%s" % (prefix, name, value)
        if source:
            val = "source=%s %s" % (source, val)
        self.logger.info(val)

    def timer(self, name, source=None):
        return Timer(name, source, self)

    def count(self, name, val=None, source=None):
        val = val or 1
        self._log(source, "count", name, val)

    def sample(self, name, val, source=None):
        self._log(source, "sample", name, val)

    def measure(self, name, val, source=None):
        self._log(source, "measure", name, val)

    def unique(self, name, val, source=None):
        self._log(source, "unique", name, val)
