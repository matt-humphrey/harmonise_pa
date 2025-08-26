import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell
def _():
    from dataclasses import asdict
    from functools import partial
    from pathlib import Path
    from typing import Any
    import re
    import banksia as bk
    import marimo as mo
    import polars as pl
    import pyreadstat

    return (bk,)


@app.cell
def _():
    from harmonise_pa import (
        DATA_TRANSFORMS,
        read_sav,
        transform_datasets,
        make_interim_datasets,
    )
    from harmonise_pa.config import DATASETS, METADATA, PROCESSED_DATA, RAW_DATA, INTERIM_DATA

    return (
        DATASETS,
        DATA_TRANSFORMS,
        INTERIM_DATA,
        METADATA,
        PROCESSED_DATA,
        transform_datasets,
    )


@app.cell
def _():
    # make_interim_datasets(DATASETS)
    return


@app.cell
def _(DATASETS, INTERIM_DATA, bk):
    dfs, metas = {}, {}

    for name, dset in DATASETS.items():
        df, meta = bk.read_sav(INTERIM_DATA/dset["file"])
        dfs[name] = df
        metas[name] = meta
    return dfs, metas


@app.cell
def _(DATA_TRANSFORMS, METADATA, bk, dfs, metas, transform_datasets):
    transformed_dfs = transform_datasets(dfs, DATA_TRANSFORMS)
    transformed_metas = bk.transform_metadata(metas, METADATA)
    return transformed_dfs, transformed_metas


@app.cell
def _(DATASETS, PROCESSED_DATA, bk, transformed_dfs, transformed_metas):
    for n, ds in DATASETS.items():
        final_df = transformed_dfs[n]
        m = transformed_metas[n]
        final_metadata = bk.convert_metadata_to_dict(m)
        bk.write_sav(PROCESSED_DATA/ds["file"], final_df, final_metadata)
    return


if __name__ == "__main__":
    app.run()
