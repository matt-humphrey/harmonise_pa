import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import banksia as bk
    import marimo as mo
    import pointblank as pb
    import polars as pl
    import pyreadstat

    from pointblank import Validate

    return Validate, bk, pl


@app.cell
def _():
    from harmonise_pa.config import DATASETS, PROCESSED_DATA, RAW_DATA, INTERIM_DATA
    from harmonise_pa import make_interim_datasets, DATA_TRANSFORMS, VALIDATIONS
    return DATASETS, PROCESSED_DATA, VALIDATIONS


@app.cell
def _(DATASETS, PROCESSED_DATA, bk):
    dfs, metas = {}, {}

    for name, dset in DATASETS.items():
        file = dset["file"]
        df, meta = bk.read_sav(PROCESSED_DATA / file)
        dfs[name] = df
        metas[name] = meta
    return (dfs,)


@app.cell
def _(VALIDATIONS, dfs):
    FINAL_VALIDATIONS = {}

    for n, dfx in dfs.items():
        vals = [fn for var, fn in VALIDATIONS.items() if f"{n}_{var}" in dfx.columns]
        FINAL_VALIDATIONS[n] = vals
    return (FINAL_VALIDATIONS,)


@app.cell
def _():
    from harmonise_pa import transform_datasets, apply_pipeline
    return (apply_pipeline,)


@app.cell
def _(FINAL_VALIDATIONS, Validate, apply_pipeline, dfs):
    dx = "G220"
    v = Validate(data=dfs[dx])
    apply_pipeline(v, FINAL_VALIDATIONS[dx]).interrogate()
    return


@app.cell
def _(dfs, pl):
    dfs["G0G1"].filter(~pl.col("G0G1_BP_CUFF").is_between(1, 4)).select("ID", pl.col("^G0G1_BP_CUFF$")) # 148
    return


@app.cell
def _(dfs, pl):
    dfs["G201"].filter(pl.col("G201_BP2").lt(25)).select("ID", "G201_BP2")
    return


@app.cell
def _(dfs, pl):
    dfs["G205"].filter(pl.col("G205_BP2").lt(25)).select("ID", "G205_BP2")
    return


@app.cell
def _(dfs, pl):
    dfs["G214"].filter(pl.col("G214_BP47").lt(30)).select("ID", "G214_BP47")
    dfs["G214"].filter(pl.col("G214_BP53").lt(30)).select("ID", "G214_BP53")
    dfs["G214"].filter(pl.col("G214_BP56").lt(30)).select("ID", "G214_BP56") # 0
    dfs["G214"].filter(pl.col("G214_BP57").lt(30)).select("ID", "G214_BP57") # 0
    dfs["G214"].filter(pl.col("G214_BP60").gt(140)).select("ID", "G214_BP60")
    return


@app.cell
def _(dfs, pl):
    dfs["G117"].filter(~pl.col("G117_BP2").is_between(25, 220)).select("ID", "G117_BP2")
    return


@app.cell
def _(dfs, pl):
    # One instance of 0 for each
    dfs["G220"].filter(~pl.col("G220_A9").is_between(1.5, 60)).select("ID", pl.col("^G220_A9$"))
    dfs["G220"].filter(~pl.col("G220_A10").is_between(1.5, 60)).select("ID", pl.col("^G220_A10$"))
    dfs["G220"].filter(~pl.col("G220_A16").is_between(12, 50)).select("ID", pl.col("^G220_A16$"))
    dfs["G220"].filter(~pl.col("G220_A22").is_between(50, 100)).select("ID", pl.col("^G220_A22$"))
    return


@app.cell
def _(dfs, pl):
    dfs["G222"].filter(~pl.col("G222_BP50").is_between(30, 220)).select("ID", pl.col("^G222_BP50$")) # 22
    return


@app.cell
def _(dfs, pl):
    dfs["G126"].filter(~pl.col("G126_BP60").is_between(30, 140)).select("ID", pl.col("^G126_BP60$")) # 148
    return


if __name__ == "__main__":
    app.run()
