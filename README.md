# Open-Radar-Data
[![CI](https://github.com/openradar/open-radar-data/actions/workflows/ci.yaml/badge.svg)](https://github.com/openradar/open-radar-data/actions/workflows/ci.yaml)
[![PyPI Version](https://img.shields.io/pypi/v/open-radar-data.svg)](https://pypi.python.org/pypi/open-radar-data)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/open-radar-data.svg)](https://anaconda.org/conda-forge/open-radar-data)

A place to share radar data with the community, shared between the open radar packages

## Sample data sets

The files contained in this repository are used as sample data in openradar examples/notebooks and are downloaded by `open-radar-data` package. It includes single sweep PPI and RHI as well as complete volume files of weather radar (and lidar) in many different source formats. You can explore the contents in the [open_radar_data/registry.txt](open_radar_data/registry.txt).

## Adding new datasets

To add a new dataset file, please follow these steps:

1. Add the dataset file to the `data/` directory
2. From the command line, run `python make_registry.py` script to update the registry file residing in `open_radar_data/registry.txt`
3. Commit and push your changes to GitHub

## Data sources and licenses

Files from third-party sources are listed here with their origin and license. Please add an entry when contributing such a file.

| File | Instrument / scan | Source | License |
|------|-------------------|--------|---------|
| `WLS200s-218_2022-10-07_00-51-38_dbs_1823_75m.nc` | Vaisala (Leosphere) WindCube 200S scanning Doppler lidar `WLS200s-218`, NetCDF-4 (`CF/Radial 2.0 , CF-1.7`, WindCube Lidar server 3.3.3); DBS scan, 4 beams at 75° elevation (azimuth 0, 90, 180, 270°) and a vertical beam, 50 rays, 188 gates of 75 m; 2022-10-07 00:51:38–00:56:08 UTC; site 51.968° N, 4.929° E | José Dias Neto, *Wind radial observations: sample data*, Zenodo, 2022, [doi:10.5281/zenodo.7366881](https://doi.org/10.5281/zenodo.7366881) (file from `wc_long_dbs.zip`, unmodified) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| `WLS400s-118_2025-02-20_02-46-06_rhi_45_150m.nc` | Vaisala WindCube 400S scanning Doppler lidar `WLS400s-118`, NetCDF-4 (`CF/Radial 2.0 , CF-1.7`, WindCube Lidar server 3.3.4); RHI at azimuth 320°, elevation 0–14.5°, 30 rays, 141 gates of 100 m from 300 m; 2025-02-20 02:46:06–02:46:35 UTC; Port of Genoa, Italy, 44.4175° N, 8.7768° E, 5 m (from the dataset description, the file has no site coordinates) | Kozmar, H., Burlando, M., Romanic, D., Ricci, A., Ivancic, I., Grisogono, B., Hadžić, N.: *ERIES-LIDAR: Lidar measurements of Ligurian downslope windstorms*, Zenodo, 2026, [doi:10.5281/zenodo.20160278](https://doi.org/10.5281/zenodo.20160278) (file from `Tramontana_20250219-20250220.zip`, unmodified) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| `WLS400s-118_2025-02-06_22-26-47_ppi_50_150m.nc` | Vaisala WindCube 400S scanning Doppler lidar `WLS400s-118`, NetCDF-4 (`CF/Radial 2.0 , CF-1.7`, WindCube Lidar server 3.3.4); sector PPI at 2.5° elevation, azimuth 295–329.5°, 70 rays, 141 gates of 100 m from 300 m; 2025-02-06 22:26:47–22:27:56 UTC; Port of Genoa, Italy, 44.4175° N, 8.7768° E, 5 m (from the dataset description, the file has no site coordinates) | Kozmar, H., Burlando, M., Romanic, D., Ricci, A., Ivancic, I., Grisogono, B., Hadžić, N.: *ERIES-LIDAR: Lidar measurements of Ligurian downslope windstorms*, Zenodo, 2026, [doi:10.5281/zenodo.20160278](https://doi.org/10.5281/zenodo.20160278) (file from `Tramontana_20250206-20250210.zip`, unmodified) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |

## Using datasets in notebooks and/or scripts

- Ensure the `open_radar_data` package is installed in your environment

  ```bash
  python -m pip install open-radar-data

  # or

  python -m pip install git+https://github.com/openradar/open-radar-data

  # or

  conda install -c conda-forge open-radar-data
  ```

- Import `DATASETS` and inspect the registry to find out which datasets are available

  ```python
  In [1]: from open_radar_data import DATASETS

  In [2]: DATASETS.registry_files
  Out[2]: ['sample_sgp_data.nc`]
  ```

- To fetch a data file of interest, use the `.fetch` method and provide the filename of the data file. This will

  - download and cache the file if it doesn't exist already.
  - retrieve and return the local path

  ```python
  In [4]: filepath = DATASETS.fetch('sample_sgp_data.nc')

  In [5]: filepath
  Out[5]: '/Users/mgrover/Library/Caches/open-radar-data/sample_sgp_data.nc'
  ```

- Once you have access to the local filepath, you can then use it to load your dataset into pandas or xarray or your package of choice:

  ```python
  In [6]: radar = pyart.io.read(filepath)
  ```

## Changing the default data cache location

The default cache location (where the data are saved on your local system) is dependent on the operating system. You can use the `locate()` method to identify it:

```python
from open_radar_data import locate
locate()
```

The location can be overwritten by the `OPEN_RADAR_DATA_DIR` environment
variable to the desired destination.
