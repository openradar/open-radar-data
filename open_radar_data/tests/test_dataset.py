import pathlib

import pytest

from open_radar_data import DATASETS, locate


def test_registry():
    files = DATASETS.registry_files
    assert len(files) > 0


def test_locate():
    p = locate()
    assert 'open-radar-data' in p
    assert pathlib.Path(p)


def test_fetch():
    fi = '2013051000000600dBZ.vol'
    fo = DATASETS.fetch(fi)
    assert fi == pathlib.Path(fo).name


@pytest.mark.xfail(strict=False, reason='possible 403')
def test_original_fetch():
    fi = 'T_PAGZ35_C_ENMI_20170421090837.hdf'
    fo = DATASETS._fetch(fi)
    assert fi == pathlib.Path(fo).name
