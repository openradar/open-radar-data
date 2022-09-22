import os
import pathlib

import pooch

if __name__ == '__main__':
    here = pathlib.Path(os.path.dirname(__file__))
    data_dir = here / 'data'

    pooch.make_registry(data_dir, here / 'open_radar_data/registry.txt')
