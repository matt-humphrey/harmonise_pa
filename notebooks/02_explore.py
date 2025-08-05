import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path
    from typing import TypeAlias

    import banksia as bk
    import marimo as mo
    import pointblank as pb
    import polars as pl

    return Path, TypeAlias, bk, mo, pb, pl


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
            pl.concat(metas, how="vertical")
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
def _(mo):
    mo.md(r"""### A6 - Mid-arm circumference""")
    return


@app.cell
def _():
    variable = "A6"
    return (variable,)


@app.cell
def _(df, pl, variable):
    df_a6 = df.select(pl.col(f"^.*{variable}$"))
    df_a6
    return (df_a6,)


@app.cell
def _(df_a6, pb):
    pb.Validate(data=df_a6).col_vals_between(
        columns=pb.everything(), left=0, right=45, na_pass=True
    ).interrogate()
    return


@app.cell
def _(df_a6, pl):
    df_a6_new = df_a6.with_columns(pl.all().replace({-99: None, 999: None})).with_columns(
        pl.all().round(decimals=2, mode="half_away_from_zero")
    )

    df_a6_new
    return (df_a6_new,)


@app.cell
def _(df_a6_new, pb):
    validate = (
        pb.Validate(data=df_a6_new)
        .col_vals_between(columns=pb.everything(), left=0, right=50, na_pass=True)
        .interrogate()
    )

    validate
    return


@app.cell
def _(meta, pl, variable):
    meta_a6 = meta.filter(pl.col("basename").eq(variable))
    meta_a6
    return


@app.cell
def _():
    A6 = {
        "basename": r"_A6$",
        "field_label": "Mid-arm circumference (cm)",
        "field_type": "Numeric",
        "field_width": 4,
        "decimals": 1,
        "var_type": "scale",
        "field_values": None,
    }
    return


if __name__ == "__main__":
    app.run()
