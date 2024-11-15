import importlib.resources
from functools import wraps

import pooch

import open_radar_data

DATASETS = pooch.create(
    path=pooch.os_cache('open-radar-data'),
    base_url='https://github.com/openradar/open-radar-data/raw/main/data/',
    env='OPEN_RADAR_DATA_DIR',
)

with open(importlib.resources.files('open_radar_data') / 'registry.txt') as registry_file:
    DATASETS.load_registry(registry_file)


def locate():
    """The absolute path to the sample data storage location on disk.
    This is where the data are saved on your computer. The location is
    dependent on the operating system. The folder locations are defined by the
    ``appdirs``  package (see the `appdirs documentation
    <https://github.com/ActiveState/appdirs>`__).
    The location can be overwritten by the ``PYTHIA_DATASETS_DIR`` environment
    variable to the desired destination.
    Returns
    -------
    path : str
        The local data storage location.
    """
    return str(DATASETS.abspath)


def open_radar_downloader(url, output_file, mypooch):
    """Create Downloader which adds request-headers"""
    headers = {'User-Agent': f'open-radar-data {open_radar_data.__version__}'}
    https = pooch.HTTPDownloader(headers=headers)
    https(url, output_file, mypooch)


# preserve current fetch
DATASETS._fetch = DATASETS.fetch


# wrap new fetch
@wraps(DATASETS._fetch)
def fetch(*args, **kwargs):
    kwargs.setdefault('downloader', open_radar_downloader)
    return DATASETS._fetch(*args, **kwargs)


# override original fetch with overridden fetch
DATASETS.fetch = fetch
