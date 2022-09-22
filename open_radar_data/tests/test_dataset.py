import pathlib

from open_radar_data import DATASETS, locate


def test_registry():
    files = DATASETS.registry_files
    assert len(files) > 0


def test_locate():
    p = locate()
    assert 'open-radar-data' in p
    assert pathlib.Path(p)
