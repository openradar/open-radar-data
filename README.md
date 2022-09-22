# Open-Radar-Data

A place to share radar data with the community, shared between the open radar packages

## Sample data sets

These files are used as sample data in Pythia Project examples/notebooks and are downloaded by `pythia_datasets` package:

- `sample_sgp_data.nc`

## Adding new datasets

To add a new dataset file, please follow these steps:

1. Add the dataset file to the `data/` directory
2. From the command line, run `python make_registry.py` script to update the registry file residing in `open_radar_data/registry.txt`
3. Commit and push your changes to GitHub

## Using datasets in notebooks and/or scripts

- Ensure the `open_radar_data` package is installed in your environment

  ```bash
  python -m pip install open-radar-data

  # or

  python -m pip install git+https://github.com/openradar/open-radar-data
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
