import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import banksia as bk
    from pathlib import Path
    from typing import Any
    return Any, Path, bk, mo, pl


@app.cell
def _():
    from polars.testing import assert_frame_equal
    return (assert_frame_equal,)


@app.cell
def _():
    from harmonise_pa import make_interim_datasets, transform_datasets, DATA_TRANSFORMS
    from harmonise_pa.config import RAW_DATA, INTERIM_DATA, PROCESSED_DATA, DATASETS, METADATA
    return (
        DATASETS,
        DATA_TRANSFORMS,
        INTERIM_DATA,
        METADATA,
        RAW_DATA,
        transform_datasets,
    )


@app.cell
def _(Any, DATASETS, Path, bk, pl):
    def read_datasets(data_folder: Path, datasets: dict[str, Any]) -> tuple[dict[str, pl.DataFrame], dict[str, pl.DataFrame]]:
        dfs, metas = {}, {}

        for name, dset in DATASETS.items():
            df, meta = bk.read_sav(data_folder / dset["file"])
            dfs[name] = df
            metas[name] = meta

        return dfs, metas
    return (read_datasets,)


@app.cell
def _(DATASETS, INTERIM_DATA, RAW_DATA, read_datasets):
    dfs_raw, metas_raw = read_datasets(RAW_DATA, DATASETS)
    dfs_interim, metas_interim = read_datasets(INTERIM_DATA, DATASETS)
    # dfs_proc, metas_proc = read_datasets(PROCESSED_DATA, DATASETS)
    return dfs_interim, dfs_raw, metas_interim


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Test Interim Data

    Ensure that when comparing interim with raw data:

    - Unaffected variables have identical data and metadata
    - Renamed variables have identical data and metadata
    - "Deleted" variables don't exist in interim
    """
    )
    return


@app.cell
def _():
    # make_interim_datasets(DATASETS)
    return


@app.cell
def _(Any, assert_frame_equal, pl):
    def validate_raw_to_interim_data(dset: dict[str, Any], df_raw, df_interim):
        df_raw = (
            df_raw
            .rename(dset["rename"])
            .drop(dset["delete"])
        )
        assert_frame_equal(df_raw, df_interim)

    def validate_raw_to_interim_metadata(dset: dict[str, Any], meta_raw, meta_interim):
        meta_raw = (
            meta_raw
            .with_columns(pl.col("Variable").replace(dset["rename"]))
            .filter(~pl.col("Variable").is_in(dset["delete"]))
        )
        assert_frame_equal(meta_raw, meta_interim)
    return validate_raw_to_interim_data, validate_raw_to_interim_metadata


@app.cell
def _(
    DATASETS,
    INTERIM_DATA,
    RAW_DATA,
    bk,
    validate_raw_to_interim_data,
    validate_raw_to_interim_metadata,
):
    for name, dset in DATASETS.items():
        print(name)
        df_raw, meta_raw = bk.read_sav(RAW_DATA/dset["file"])
        df_interim, meta_interim = bk.read_sav(INTERIM_DATA/dset["file"])
        try:
            validate_raw_to_interim_data(dset, df_raw, df_interim)
            validate_raw_to_interim_metadata(dset, meta_raw, meta_interim)
        except Exception as e:
            print(e)
    return


@app.cell
def _(DATASETS, dfs_interim, dfs_raw, validate_raw_to_interim_data):
    validate_raw_to_interim_data(DATASETS["G220"], dfs_raw["G220"], dfs_interim["G220"])
    return


@app.cell
def _(DATASETS, dfs_interim, dfs_raw):
    d = DATASETS["G217"]
    df1 = dfs_raw["G217"].rename(d["rename"]).drop(d["delete"])
    df2 = dfs_interim["G217"]

    dtype_diffs = {col: (df1.schema[col], df2.schema[col]) 
                   for col in df1.columns 
                   if col in df2.columns and df1.schema[col] != df2.schema[col]}

    dtype_diffs
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Test Processed Data

    Ensure that:

    - [ ] Unchanged variables have identical data and metadata
        - [ ] Find common columns for metadata (or save processed data, and then read it back into Python)
    """
    )
    return


@app.cell
def _(
    DATA_TRANSFORMS,
    METADATA,
    bk,
    dfs_interim,
    metas_interim,
    transform_datasets,
):
    dfs_proc = transform_datasets(dfs_interim, DATA_TRANSFORMS)
    metas_proc = bk.transform_metadata(metas_interim, METADATA)
    return dfs_proc, metas_proc


@app.cell
def _(Any, assert_frame_equal, meta_i, meta_p, pl):
    def validate_interim_to_proc_data(dset: dict[str, Any], df_interim, df_proc):
        cols_changed = dset["variables"] + list(dset["rename"].values()) + ["G208_BMI", "G210_BMI"]
        assert_frame_equal(df_interim.select(pl.exclude(cols_changed)), df_proc.select(pl.exclude(cols_changed)))

    def validate_interim_to_proc_metadata(dset: dict[str, Any], meta_interim, meta_proc):
        cols_changed = dset["variables"] + list(dset["rename"].values()) + ["G208_BMI", "G210_BMI"]

        s1 = meta_i.select("Variable").to_series().to_list()
        s2 = meta_p.select("Variable").to_series().to_list()
        s = set(s1).intersection(set(s2))

        assert_frame_equal(
            meta_interim.filter(~pl.col("Variable").is_in(cols_changed)),
            meta_proc.filter(~pl.col("Variable").is_in(cols_changed))
        )
    return (validate_interim_to_proc_data,)


@app.cell
def _():
    # for name, dset in DATASETS.items():
    #     print(name)
    #     df_raw, meta_raw = bk.read_sav(RAW_DATA/dset["file"])
    #     df_interim, meta_interim = bk.read_sav(INTERIM_DATA/dset["file"])
    #     try:
    #         validate_raw_to_interim_data(dset, df_raw, df_interim)
    #         validate_raw_to_interim_metadata(dset, meta_raw, meta_interim)
    #     except Exception as e:
    #         print(e)
    return


@app.cell
def _(DATASETS, dfs_interim, dfs_proc, validate_interim_to_proc_data):
    f = "G208"

    ds = DATASETS[f]
    df_i = dfs_interim[f]
    df_p = dfs_proc[f]

    validate_interim_to_proc_data(ds, df_i, df_p)
    return ds, f


@app.cell
def _(ds, f, metas_interim, metas_proc):
    meta_i = metas_interim[f]
    meta_p = metas_proc[f]

    cols_changed = ds["variables"] + list(ds["rename"].values())

    # validate_interim_to_proc_metadata(ds, meta_i, meta_p)
    meta_i #.filter(~pl.col("Variable").is_in(cols_changed))
    return meta_i, meta_p


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _(meta_p, pl, s):
    meta_p.filter(pl.col("Variable").is_in(s))
    return


if __name__ == "__main__":
    app.run()
