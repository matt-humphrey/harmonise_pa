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

    return mo, pb, pl


@app.cell
def _():
    from harmonise_pa.config import DATASETS, RAW_DATA
    from harmonise_pa import read_all_datasets
    return DATASETS, read_all_datasets


@app.cell
def _(DATASETS):
    gen1 = [DATASETS[k] for k in DATASETS.keys() if k.startswith("G1")]
    gen2 = [k for k in DATASETS.keys() if k.startswith("G2")]
    # DATASETS["G0G1"]
    return


@app.cell
def _(DATASETS, read_all_datasets):
    df, meta = read_all_datasets(DATASETS)
    return df, meta


@app.cell
def _(df):
    df
    return


@app.cell
def _(mo):
    mo.md(r"""### HEIGHT""")
    return


@app.cell
def _():
    variable = "HEIGHT"
    return (variable,)


@app.cell
def _(df, pl, variable):
    dfx = df.select(pl.col(f"^.*{variable}$"))
    dfx
    return (dfx,)


@app.cell
def _(dfx, pb):
    pb.Validate(data=dfx).col_vals_between(
        columns=pb.everything(), left=10, right=200, na_pass=True
    ).interrogate()
    return


@app.cell
def _(dfx, pl):
    dfx_new = dfx.with_columns(pl.all().replace({-99: None, 999: None})).with_columns(
        pl.all().round(decimals=2, mode="half_away_from_zero")
    )

    dfx_new
    return (dfx_new,)


@app.cell
def _(dfx_new, pb):
    validate = (
        pb.Validate(data=dfx_new)
        .col_vals_between(columns=pb.everything(), left=10, right=200, na_pass=True)
        .interrogate()
    )

    validate
    return (validate,)


@app.cell
def _(validate):
    validate.get_step_report(i=18)
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
