import banksia as bk
import polars as pl

from harmonise_pa import (
    DATA_TRANSFORMS,
    read_sav,
    transform_datasets,
)
from harmonise_pa.config import DATASETS, METADATA, PROCESSED_DATA, RAW_DATA

datasets = {k: v for k, v in DATASETS.items()}

dfs, metas = {}, {}

for name, dset in datasets.items():
    df, meta = read_sav(dset, RAW_DATA)
    dfs[name] = df
    metas[name] = meta

transformed_dfs = transform_datasets(dfs, DATA_TRANSFORMS)

new_metas = bk.transform_metadata(metas, METADATA)
