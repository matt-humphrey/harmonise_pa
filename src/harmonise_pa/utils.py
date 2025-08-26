from functools import reduce
from pathlib import Path
from typing import Callable, TypeAlias

import banksia as bk
import polars as pl
from polars import DataFrame

from harmonise_pa.config import INTERIM_DATA, RAW_DATA

__all__ = [
    "apply_pipeline",
    "make_interim_datasets",
    "read_dataset",
    "read_all_datasets",
    "read_sav",
    "transform_datasets",
]

Dataset: TypeAlias = dict[str, str | list | dict[str, str]]
Transform: TypeAlias = Callable[[DataFrame], DataFrame]


def read_sav(file: Dataset, data_folder: Path = RAW_DATA) -> tuple[pl.DataFrame, pl.DataFrame]:
    """
    Create a wrapper around `banksia.read_sav()` for reading files and performing transformations
    like renaming and deleting variables for harmonising.
    """
    file_name = file["file"]
    rename = file["rename"]
    delete = file["delete"]

    df, meta = bk.read_sav(data_folder / file_name)

    df = df.rename(rename).drop(delete)
    meta = meta.with_columns(pl.col("Variable").replace(rename))

    return df, meta


def read_dataset(file: Dataset, data_folder: Path = RAW_DATA) -> tuple[pl.DataFrame, pl.DataFrame]:
    """
    Create a wrapper around `banksia.read_sav()` for reading and renaming specific variables for
    initial data exploration.
    """
    file_name = file["file"]
    variables = file["variables"]
    rename = file["rename"]

    input_cols = variables + list(rename.keys())
    output_cols = variables + list(rename.values())

    df, meta = bk.read_sav(data_folder / file_name, usecols=input_cols)

    df = df.rename(rename).select(output_cols)
    meta = meta.with_columns(pl.col("Variable").replace(rename))

    return df, meta


def read_all_datasets(
    files: dict[Dataset], data_folder: Path = RAW_DATA
) -> tuple[pl.DataFrame, pl.DataFrame]:
    "Read and merge all datasets."
    lfs, metas = [], []
    for file in files:
        df, meta = read_dataset(files[file], data_folder)
        lfs.append(df)
        metas.append(meta)

    combined_lf = _concat_lazy_frames(lfs)
    combined_meta = (
        pl.concat(metas, how="vertical")
        .filter(pl.col("Variable").ne("ID"))
        .with_columns(basename=pl.col("Variable").str.slice(5))
    )

    return combined_lf, combined_meta


def _join_lazy_frames(lfs: list[pl.LazyFrame]) -> pl.LazyFrame:
    joined_lf = lfs[0]
    for lf in lfs[1:]:
        joined_lf = joined_lf.join(lf, on="ID", how="full")
    return joined_lf.collect()


def _concat_lazy_frames(lfs: list[pl.LazyFrame]) -> pl.LazyFrame:
    return pl.concat(lfs, how="align")


def apply_pipeline(df: DataFrame, transforms: list[Transform]) -> DataFrame:
    "Selectively apply functions in a composable pipeline"
    return reduce(lambda result, fn: fn(result), transforms, df)


def transform_datasets(
    datasets: dict[str, DataFrame], pipelines: dict[str, Transform]
) -> dict[str, DataFrame]:
    "Apply defined transformations to the datasets"
    return {
        dset: apply_pipeline(df, pipelines[dset])
        for dset, df in datasets.items()
        if dset in pipelines
    }


def make_interim(file: Dataset, raw: Path = RAW_DATA) -> tuple[pl.DataFrame, pl.DataFrame]:
    """
    Create a wrapper around `banksia.read_sav()` for reading files and performing transformations
    like renaming and deleting variables for harmonising.
    """
    file_name = file["file"]
    rename = file["rename"]
    delete = file["delete"]

    df, meta = bk.read_sav(raw / file_name)

    df = df.rename(rename).drop(delete)
    meta = meta.with_columns(pl.col("Variable").replace(rename))

    return df, meta


def make_interim_datasets(
    datasets: dict[str, Dataset],
):
    for name, dset in datasets.items():
        df, meta = make_interim(dset, RAW_DATA)
        bk.write_sav(INTERIM_DATA / dset["file"], df, meta)
