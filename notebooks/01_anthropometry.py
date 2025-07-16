import marimo

__generated_with = "0.14.11"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    My approach here has been to take a screenshot of the relevant anthropometry (physical measurement) components of the physical assessment sheets, and to pull in the data from the corresponding SPSS file. I read the labels and field values and get a quick check that the variables in the dataset align with the section of the assessment I'm investigating.

    Next steps will be to dig more deeply into the questions:
    - Check the units of measurement are consistent
    - Verify that the field values correspond to the actual options
    - Check the metadata (labels and field values) align across follow-ups
    - Check the data schema for each variable
        - is the type consistent (always a string, or numeric value)
        - if numeric, is it always an int, or float, and if float, is the rounding consistent?
    """
    )
    return


@app.cell
def _():
    import banksia as bk
    import marimo as mo
    import polars as pl

    return bk, mo, pl


@app.cell
def _():
    from harmonise_pa.config import RAW_DATA

    return (RAW_DATA,)


@app.cell
def _(mo):
    mo.md("""## Y0 - Neonatal (G200 Merged)""")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y0.PNG")
    return


@app.cell
def _(meta_g200, pl):
    meta_g200.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell
def _(df_g200):
    df_g200
    return


@app.cell
def _():
    vars_g200 = [
        "ID",
        "G200_B_LONG",
        "G200_B_HEAD",
        "G200_B_CORON",
        "G200_B_CHEST",
        "G200_B_ABDOM",
        "G200_B_FOOT",
        "G200_B_DIAS",
        "G200_B_SYS",
        "G200_B_MIDARM",
        "G200_B_TRICEP",
        "G200_B_PARASC",
        "G200_B_INFRSC",
        "G200_B_SUCK",
    ]
    return (vars_g200,)


@app.cell
def _(RAW_DATA, bk, vars_g200):
    df_g200, meta_g200 = bk.read_sav(RAW_DATA / "G200_Merged.sav", usecols=vars_g200)
    return df_g200, meta_g200


@app.cell
def _(mo):
    mo.md("""## Y1 (G201_PA)""")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y1.PNG")
    return


@app.cell
def _(meta_g201, pl):
    meta_g201.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell
def _(df_g201):
    df_g201
    return


@app.cell
def _():
    vars_g201 = [
        "ID",
        "G201_A1",  # Exam weight
        "G201_A2",  # Exam Standing height - m
        "G201_A3",  # Exam Sitting height
        "G201_A4",  # Exam Head circumference
        "G201_A5",  # Exam Chest circumference
        "G201_A6",  # Exam Mid arm circumference
        "G201_A7",  # Exam triceps skinfold
        "G201_A8",  # Exam subscapular skinfold
        "G201_A9",  # Exam Suprailiac skinfold
        "G201_A10",  # Exam abdominal skinfold
        "G201_BP1",  # Exam Systolic blood pressure
        "G201_BP2",  # Exam Diastolic blood pressure
        "G201_BP3",  # Exam Blood pressure state
        "G201_BP4",  # Exam blood pressure instrument
    ]
    return (vars_g201,)


@app.cell
def _(RAW_DATA, bk, vars_g201):
    df_g201, meta_g201 = bk.read_sav(RAW_DATA / "G201_Quest_PA.sav", usecols=vars_g201)
    return df_g201, meta_g201


@app.cell
def _(mo):
    mo.md("""## Y2 (G202_PA)""")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y2.PNG")
    return


@app.cell
def _(meta_g202, pl):
    meta_g202.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell
def _(df_g202):
    df_g202
    return


@app.cell(hide_code=True)
def _():
    vars_g202 = [
        "ID",
        "G202_A1",
        "G202_A2",
        "G202_A3",
        "G202_A4",
        "G202_A5",
        "G202_A6",
        "G202_A7",
        "G202_A8",
        "G202_A9",
        "G202_A10",
        "G202_BP1",
        "G202_BP2",
        "G202_BP3",
        "G202_BP4",
    ]
    return (vars_g202,)


@app.cell(hide_code=True)
def _(RAW_DATA, bk, vars_g202):
    df_g202, meta_g202 = bk.read_sav(RAW_DATA / "G202_Quest_PA.sav", usecols=vars_g202)
    return df_g202, meta_g202


@app.cell
def _(mo):
    mo.md("""## Y3 (G203_PA)""")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y3.PNG")
    return


@app.cell
def _(meta_g203, pl):
    meta_g203.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell(hide_code=True)
def _():
    vars_g203 = [
        "ID",
        "G203_A1",
        "G203_A2",
        "G203_A3",
        "G203_A4",
        "G203_A5",
        "G203_A6",
        "G203_A7",
        "G203_A8",
        "G203_A9",
        "G203_A10",
        "G203_BP1",
        "G203_BP2",
        "G203_BP3",
        "G203_BP4",
    ]
    return (vars_g203,)


@app.cell(hide_code=True)
def _(RAW_DATA, bk, vars_g203):
    df_g203, meta_g203 = bk.read_sav(RAW_DATA / "G203_Quest_PA.sav", usecols=vars_g203)
    return (meta_g203,)


@app.cell
def _(mo):
    mo.md("""## Y5""")
    return


@app.cell
def _(mo):
    mo.md("""### Gen 1""")
    return


@app.cell
def _(mo):
    mo.md("""### Gen 2""")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y5_2.PNG")
    return


@app.cell
def _(meta_g105, pl):
    meta_g105.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell(hide_code=True)
def _():
    vars_g105 = [
        "ID",
        "G105_A1",
        "G105_A2",
        "G105_BP1",
        "G105_BP2",
        "G105_BP3",
        "G105_BP4",
        "G105_BP5",
        "G105_BPCD",
    ]
    return (vars_g105,)


@app.cell(hide_code=True)
def _(RAW_DATA, bk, vars_g105):
    df_g105, meta_g105 = bk.read_sav(RAW_DATA / "G105_PA.sav", usecols=vars_g105)
    return (meta_g105,)


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y5.PNG")
    return


@app.cell
def _(meta_g205, pl):
    meta_g205.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell(hide_code=True)
def _():
    vars_g205 = [
        "ID",
        "G205_A1",
        "G205_A2",
        "G205_A3",
        "G205_A4",
        "G205_A5",
        "G205_A6",
        "G205_A7",
        "G205_A8",
        "G205_A9",
        "G205_A10",
        "G205_BP1",
        "G205_BP2",
        "G205_BP3",
        "G205_BP4",
        "G205_BP5",
    ]
    return (vars_g205,)


@app.cell(hide_code=True)
def _(RAW_DATA, bk, vars_g205):
    df_g205, meta_g205 = bk.read_sav(RAW_DATA / "G205_PA.sav", usecols=vars_g205)
    return (meta_g205,)


@app.cell
def _(mo):
    mo.md("""## Y8""")
    return


@app.cell
def _(mo):
    mo.md("""### Gen 1""")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y8.PNG")
    return


@app.cell
def _(meta_g108, pl):
    meta_g108.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell(hide_code=True)
def _():
    vars_g108 = [
        "ID",
        "G108_A1",
        "G108_A2",
        "G108_BMI",
        "G108_BP1",
        "G108_BP2",
        "G108_BP5",
        "G108_BP3",
        "G108_BP5_1",
    ]
    return (vars_g108,)


@app.cell(hide_code=True)
def _(RAW_DATA, bk, vars_g108):
    df_g108, meta_g108 = bk.read_sav(RAW_DATA / "G108_PA.sav", usecols=vars_g108)
    return (meta_g108,)


@app.cell
def _(mo):
    mo.md("""### Gen 2""")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y8.PNG")
    return


@app.cell
def _(meta_g208, pl):
    meta_g208.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell(hide_code=True)
def _():
    vars_g208 = [
        "ID",
        "G208_A1",
        "G208_A2",
        "G208_BMI",
        "G208_A4",
        "G208_A5",
        "G208_A6",
    ]
    return (vars_g208,)


@app.cell(hide_code=True)
def _(RAW_DATA, bk, vars_g208):
    df_g208, meta_g208 = bk.read_sav(RAW_DATA / "G208_PA.sav", usecols=vars_g208)
    return (meta_g208,)


if __name__ == "__main__":
    app.run()
