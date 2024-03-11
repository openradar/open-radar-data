#!/usr/bin/env python3
# flake8: noqa
"""Top-level module for pythia-datasets ."""
import importlib.metadata as _importlib_metadata

from .dataset import DATASETS, locate

try:
    __version__ = _importlib_metadata.version("open-radar-data")
except _importlib_metadata.PackageNotFoundError:  # pragma: no cover
    # package is not installed
    __version__ = 'unknown'  # pragma: no cover
