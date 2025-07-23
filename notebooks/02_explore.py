import marimo

__generated_with = "0.14.12"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path
    from typing import TypeAlias

    import banksia as bk
    import polars as pl

    return Path, TypeAlias, bk, pl


@app.cell
def _():
    from harmonise_pa.config import DATASETS, RAW_DATA

    return DATASETS, RAW_DATA


@app.cell
def _(Path, RAW_DATA, TypeAlias, bk, pl):
    Dataset: TypeAlias = dict[str, str | list | dict[str, str]]

    def read_dataset(
        file: Dataset, data_folder: Path = RAW_DATA
    ) -> tuple[pl.DataFrame, pl.DataFrame]:
        "Create a wrapper around `banksia.read_sav()` to simplify process of reading data."
        file_name = file["file"]
        variables = file["variables"]
        rename = file["rename"]
        # delete = file["delete"]

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
            lfs.append(df.lazy())
            metas.append(meta)

        combined_lf = join_lazy_frames(lfs)
        combined_meta = (
            pl.concat(metas, how='vertical')
            .filter(pl.col("Variable").ne("ID"))
            .with_columns(basename=pl.col("Variable").str.slice(5))
        )

        return combined_lf, combined_meta

    def join_lazy_frames(lfs: list[pl.LazyFrame]) -> pl.LazyFrame:
        joined_lf = lfs[0]
        for lf in lfs[1:]:
            joined_lf = joined_lf.join(lf, on="ID", how="left")
        return joined_lf.collect()

    return (read_all_datasets,)


@app.cell
def _(DATASETS, read_all_datasets):
    df, meta = read_all_datasets(DATASETS)
    return df, meta


@app.cell
def _():
    variable = "A10"
    return (variable,)


@app.cell
def _(df, pl, variable):
    df.select(pl.col(f"^.*{variable}$"))
    return


@app.cell
def _(meta, pl, variable):
    meta.filter(pl.col("basename").eq(variable))
    return


if __name__ == "__main__":
    app.run()
