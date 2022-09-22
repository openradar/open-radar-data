#!/usr/bin/env python3
# flake8: noqa
"""Top-level module for pythia-datasets ."""
from pkg_resources import DistributionNotFound, get_distribution

from .dataset import DATASETS, locate

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:  # pragma: no cover
    # package is not installed
    __version__ = 'unknown'  # pragma: no cover
