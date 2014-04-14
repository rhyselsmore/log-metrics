# -*- coding: utf-8 -*-

# Meta

__version__ = "0.0.1"
__author__ = 'Rhys Elsmore'
__email__ = 'me@rhys.io'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2014 Rhys Elsmore'

# Module Namespace

from .core import LogMetrics
from .api import timer, increment, sample, measure, unique

