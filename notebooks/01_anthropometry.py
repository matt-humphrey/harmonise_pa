import marimo

__generated_with = "0.14.11"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    My approach here has been to take a screenshot of the relevant anthropometry (physical measurement) components of the physical assessment sheets, and to pull in the data from the corresponding SPSS file. I read the labels and field values and get a quick check that the variables in the dataset align with the section of the assessment I'm investigating.

    - Next steps will be to dig more deeply into the questions:
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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
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
    mo.md("""### Gen 2""")
    return


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


@app.cell
def _(mo):
    mo.md("""## Y10""")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y10.PNG")
    return


@app.cell
def _(meta_g210, pl):
    meta_g210.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell(hide_code=True)
def _():
    vars_g210 = [
        "ID",
        "G210_A1",
        "G210_A2",
        "G210_A4",
        "G210_A6",
        "G210_A7",
        "G210_A8",
        "G210_A9",
        "G210_A10",
        "G210_BP4",
        "G210_BP1",
        "G210_BP2",
        "G210_BP5",
        "G210_BP3",
    ]
    return (vars_g210,)


@app.cell(hide_code=True)
def _(RAW_DATA, bk, vars_g210):
    df_g210, meta_g210 = bk.read_sav(RAW_DATA / "G210_PA.sav", usecols=vars_g210)
    return (meta_g210,)


@app.cell
def _(mo):
    mo.md("""## Y14""")
    return


@app.cell
def _(mo):
    mo.md("""### Gen 1""")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y14_PQ.PNG")
    return


@app.cell
def _(meta_g114, pl):
    meta_g114.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell(hide_code=True)
def _():
    vars_g114 = [
        "ID",
        "G114_A1",
        "G114_A2",
        "G114_A6",
        "G114_BP1",
        "G114_BP2",
        "G114_BP3",
        "G114_BP5",
        "G114_BP4",
    ]
    return (vars_g114,)


@app.cell(hide_code=True)
def _(RAW_DATA, bk, vars_g114):
    df_g114, meta_g114 = bk.read_sav(RAW_DATA / "G114_PA.sav", usecols=vars_g114)
    return (meta_g114,)


@app.cell
def _(mo):
    mo.md("""### Gen 2""")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y14.PNG")
    return


@app.cell
def _(meta_g214, pl):
    meta_g214.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell(hide_code=True)
def _():
    vars_g214 = [
        "ID",
        "G214_A1",
        "G214_A1A",
        "G214_A1B",
        "G214_A2",
        "G214_A2A",
        "G214_A2B",
        "G214_A6",
        "G214_A12",
        "G214_A12A",
        "G214_A12B",
        "G214_A13",
        "G214_A13A",
        "G214_A13B",
        "G214_A14",
        "G214_BP46",
        "G214_BP47",
        "G214_BP48",
        "G214_BP49",
        "G214_BP50",
        "G214_BP51",
        "G214_BP52",
        "G214_BP53",
        "G214_BP54",
        "G214_BP55",
        "G214_BP56",
        "G214_BP57",
        "G214_BP58",
        "G214_BP59",
        "G214_BP60",
        "G214_BP61",
        "G214_BP62",
        "G214_BP63",
        "G214_BP1",
        "G214_BP2",
        "G214_BP3",
        "G214_BP4",
        "G214_BP5",
        "G214_CBP6",
        "G214_CBP7",
        "G214_CBP8",
        "G214_CBP9",
        "G214_CBP10",
        "G214_CBP11",
    ]
    return (vars_g214,)


@app.cell(hide_code=True)
def _(RAW_DATA, bk, vars_g214):
    df_g214, meta_g214 = bk.read_sav(RAW_DATA / "G214_PA.sav", usecols=vars_g214)
    return (meta_g214,)


@app.cell
def _(mo):
    mo.md("""## Y17""")
    return


@app.cell
def _(mo):
    mo.md("""### Gen 1""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    Can't find actual examination sheet for Y17 parent physical assessment (in IRDS anyway).
    Based on the protocol, it was quite simple.
    """
    )
    return


@app.cell
def _(meta_g117, pl):
    meta_g117.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell(hide_code=True)
def _():
    vars_g117 = [
        "ID",
        "G117_A1",
        "G117_A2",
        "G117_A6",
        "G117_BP1",
        "G117_BP2",
        "G117_BP3",
        "G117_BP5",
        "G117_BP4",
    ]
    return (vars_g117,)


@app.cell(hide_code=True)
def _(RAW_DATA, bk, vars_g117):
    df_g117, meta_g117 = bk.read_sav(RAW_DATA / "G117_PA.sav", usecols=vars_g117)
    return (meta_g117,)


@app.cell
def _(mo):
    mo.md("""### Gen 2""")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y17_1.PNG")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y17_2.PNG")
    return


@app.cell
def _(meta_g217, pl):
    meta_g217.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell(hide_code=True)
def _():
    vars_g217 = [
        "ID",
        "G217_BP_TIM",
        "G217_BP_TMP",
        "G217_BP46",
        "G217_BP47",
        "G217_BP48",
        "G217_BP49",
        "G217_BP50",
        "G217_BP51",
        "G217_BP52",
        "G217_BP53",
        "G217_BP54",
        "G217_BP55",
        "G217_BP56",
        "G217_BP57",
        "G217_BP58",
        "G217_BP59",
        "G217_BP60",
        "G217_BP61",
        "G217_BP62",
        "G217_BP63",
        "G217_BP1",
        "G217_BP2",
        "G217_BP3",
        "G217_BP5",
        "G217_A1",
        "G217_A2",
        "G217_BMI",
        "G217_A6",
        "G217_A7",
        "G217_A8",
        "G217_A9",
        "G217_A10",
        "G217_A12",
        "G217_A13",
        "G217_A14",
        "G217_A15",
    ]
    return (vars_g217,)


@app.cell(hide_code=True)
def _(RAW_DATA, bk, vars_g217):
    df_g217, meta_g217 = bk.read_sav(RAW_DATA / "G217_PA.sav", usecols=vars_g217)
    return (meta_g217,)


@app.cell
def _(mo):
    mo.md("""## Y20""")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y20_1.PNG")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y20_2.PNG")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y20_3.PNG")
    return


@app.cell
def _(meta_g220, pl):
    meta_g220.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell(hide_code=True)
def _():
    vars_g220 = [
        "ID",
        "G220_BP_TIM",
        "G220_BP_TMP",
        "G220_CUFF",
        "G220_BP46",
        "G220_BP47",
        "G220_BP48",
        "G220_BP49",
        "G220_BP50",
        "G220_BP51",
        "G220_BP52",
        "G220_BP53",
        "G220_BP54",
        "G220_BP55",
        "G220_BP56",
        "G220_BP57",
        "G220_BP58",
        "G220_BP59",
        "G220_BP60",
        "G220_BP61",
        "G220_BP62",
        "G220_BP63",
        "G220_BP1",
        "G220_BP2",
        "G220_BP5",
        "G220_A2",
        "G220_A1",
        "G220_BMI",
        "G220_A12A",
        "G220_A12B",
        "G220_A12",
        "G220_A13A",
        "G220_A13B",
        "G220_A13",
        "G220_A14",
        "G220_A15A",
        "G220_A15B",
        "G220_A15C",
        "G220_A15",
        "G220_A16A",
        "G220_A16B",
        "G220_A16",
        "G220_A17A",
        "G220_A17B",
        "G220_A23A",
        "G220_A23B",
        "G220_SF_RA",
        "G220_A7A",
        "G220_A7B",
        "G220_A7",
        "G220_A8A",
        "G220_A8B",
        "G220_A8C",
        "G220_A10A",
        "G220_A10B",
        "G220_A10C",
        "G220_A9A",
        "G220_A9B",
        "G220_A9C",
        "G220_A18A",
        "G220_A18B",
        "G220_A18",
        "G220_A19",
        "G220_A20",
        "G220_A21",
        "G220_A22",
    ]
    return (vars_g220,)


@app.cell(hide_code=True)
def _(RAW_DATA, bk, vars_g220):
    df_g220, meta_g220 = bk.read_sav(RAW_DATA / "G220_PAdata.sav", usecols=vars_g220)
    return (meta_g220,)


@app.cell
def _(mo):
    mo.md("""## Y22""")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y22.PNG")
    return


@app.cell
def _(meta_g222, pl):
    meta_g222.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell(hide_code=True)
def _():
    vars_g222 = [
        "ID",
        "G222_A6_1",
        "G222_BPTM",
        "G222_BPTP",
        "G222_BP46",
        "G222_BP47",
        "G222_BP48",
        "G222_BP49",
        "G222_BP50",
        "G222_BP51",
        "G222_BP52",
        "G222_BP53",
        "G222_BP54",
        "G222_BP55",
        "G222_BP56",
        "G222_BP57",
        "G222_BP58",
        "G222_BP59",
        "G222_BP60",
        "G222_BP61",
        "G222_BP62",
        "G222_BP63",
        "G222_A1",
        "G222_A2",
        "G222_BMI",
        "G222_A12",
        "G222_A12A",
        "G222_A12B",
        "G222_A13",
        "G222_A13A",
        "G222_A13B",
        "G222_A14",
        "G222_A7A",
        "G222_A7B",
        "G222_A7C",
        "G222_A8A",
        "G222_A8B",
        "G222_A8C",
        "G222_A10A",
        "G222_A10B",
        "G222_A10C",
        "G222_A9A",
        "G222_A9B",
        "G222_A9C",
    ]
    return (vars_g222,)


@app.cell(hide_code=True)
def _(RAW_DATA, bk, vars_g222):
    df_g222, meta_g222 = bk.read_sav(RAW_DATA / "G222_PA.sav", usecols=vars_g222)
    return (meta_g222,)


@app.cell
def _(mo):
    mo.md("""## Y27""")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y27_1.PNG")
    return


@app.cell
def _(mo):
    mo.image(src="projects/anthropometry/img/Y27_2.PNG")
    return


@app.cell
def _(meta_g227, pl):
    meta_g227.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell(hide_code=True)
def _():
    vars_g227 = [
        "ID",
        "G227_BP_TIM",
        "G227_BP_TMP",
        "G227_CUFF",
        "G227_A6",
        "G227_BP46",
        "G227_BP47",
        "G227_BP48",
        "G227_BP49",
        "G227_BP50",
        "G227_BP51",
        "G227_BP52",
        "G227_BP53",
        "G227_BP54",
        "G227_BP55",
        "G227_BP56",
        "G227_BP57",
        "G227_BP58",
        "G227_BP59",
        "G227_BP60",
        "G227_BP61",
        "G227_BP62",
        "G227_BP63",
        "G227_AvSBP",
        "G227_AvDBP",
        "G227_AvHR",
        "G227_A2",
        "G227_A1",
        "G227_A2B",
        "G227_BMI",
        "G227_BP10_1",
        "G227_BP11_1",
        "G227_BP12_1",
        "G227_BP13_1",
        "G227_BP14_1",
        "G227_BP15_1",
        "G227_BP16_1",
        "G227_BP17_1",
        "G227_BP18_1",
        "G227_BP19_1",
        "G227_BP20_1",
        "G227_BP21_1",
        "G227_BP22_1",
        "G227_BP23_1",
        "G227_BP24_1",
        "G227_BP25_1",
        "G227_BP26_1",
        "G227_BP27_1",
        "G227_A12A",
        "G227_A12B",
        "G227_A12",
        "G227_A13A",
        "G227_A13B",
        "G227_A13",
        "G227_A14",
        "G227_A7A",
        "G227_A7B",
        "G227_A7",
        "G227_A11A",
        "G227_A11B",
        "G227_A11",
        "G227_A8A",
        "G227_A8B",
        "G227_A8C",
        "G227_A10A",
        "G227_A10B",
        "G227_A10C",
        "G227_A9A",
        "G227_A9B",
        "G227_A9C",
    ]
    return (vars_g227,)


@app.cell(hide_code=True)
def _(RAW_DATA, bk, vars_g227):
    df_g227, meta_g227 = bk.read_sav(RAW_DATA / "G227_PA.sav", usecols=vars_g227)
    return (meta_g227,)


@app.cell
def _(mo):
    mo.md("""## Y28""")
    return


@app.cell
def _():
    # mo.image(src="projects/anthropometry/img/Y28.PNG")
    return


@app.cell
def _(meta_g228, pl):
    meta_g228.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell(hide_code=True)
def _():
    vars_g228 = [
        "ID",
        "G228_A1",
        "G228_A2A",
        "G228_A2B",
        "G228_A6",
        "G228_A12",
        "G228_A12A",
        "G228_A12B",
        "G228_A13",
        "G228_A13A",
        "G228_A13B",
        "G228_A14",
        "G228_BP46",
        "G228_BP47",
        "G228_BP48",
        "G228_BP49",
        "G228_BP50",
        "G228_BP51",
        "G228_BP52",
        "G228_BP53",
        "G228_BP54",
        "G228_BP55",
        "G228_BP56",
        "G228_BP57",
        "G228_BP58",
        "G228_BP59",
        "G228_BP60",
        "G228_BP61",
        "G228_BP62",
        "G228_BP63",
        "G228_BP_TIM",
        "G228_BP_TMP",
        "G228_CUFF",
        "G228_BMI",
    ]
    return (vars_g228,)


@app.cell(hide_code=True)
def _(RAW_DATA, bk, vars_g228):
    df_g228, meta_g228 = bk.read_sav(RAW_DATA / "G228_PA.sav", usecols=vars_g228)
    return (meta_g228,)


@app.cell
def _(mo):
    mo.md("""## G126""")
    return


@app.cell
def _():
    # mo.image(src="projects/anthropometry/img/G126.PNG")
    return


@app.cell
def _(meta_g126, pl):
    meta_g126.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell(hide_code=True)
def _():
    vars_g126 = [
        "ID",
        "G126_CUFF",
        "G126_BP_TIM",
        "G126_BP_TMP",
        "G126_BP46",
        "G126_BP47",
        "G126_BP48",
        "G126_BP49",
        "G126_BP50",
        "G126_BP51",
        "G126_BP52",
        "G126_BP53",
        "G126_BP54",
        "G126_BP55",
        "G126_BP56",
        "G126_BP57",
        "G126_BP58",
        "G126_BP59",
        "G126_BP60",
        "G126_BP61",
        "G126_BP62",
        "G126_BP63",
        "G126_A2",
        "G126_A1",
        "G126_BMI",
        "G126_A12A",
        "G126_A12B",
        "G126_A12",
        "G126_A13A",
        "G126_A13B",
        "G126_A13",
        "G126_A14",
    ]
    return (vars_g126,)


@app.cell(hide_code=True)
def _(RAW_DATA, bk, vars_g126):
    df_g126, meta_g126 = bk.read_sav(RAW_DATA / "G126_PAdata.sav", usecols=vars_g126)
    return (meta_g126,)


@app.cell
def _(mo):
    mo.md("""## G0G1""")
    return


@app.cell
def _():
    # mo.image(src="projects/anthropometry/img/G0G1.PNG")
    return


@app.cell
def _(meta_g0g1, pl):
    meta_g0g1.select(pl.col("Variable", "Label", "Field Values"))
    return


@app.cell(hide_code=True)
def _():
    vars_g0g1 = [
        "ID",
        "G0G1_WEIGHT",
        "G0G1_HEIGHT1",
        "G0G1_HEIGHT2",
        "G0G1_HEIGHT_AV",
        "G0G1_WAIST1",
        "G0G1_WAIST2",
        "G0G1_WAIST_AV",
        "G0G1_HIP1",
        "G0G1_HIP2",
        "G0G1_HIP_AV",
        "G0G1_WAIST_HIP_RATIO",
        "G0G1_BMI",
        "G0G1_BP_DONE",
        "G0G1_BP_TIME",
        "G0G1_BP_CUFF",
        "G0G1_BPS0",
        "G0G1_BPD0",
        "G0G1_BPP0",
        "G0G1_BPS2",
        "G0G1_BPD2",
        "G0G1_BPP2",
        "G0G1_BPS4",
        "G0G1_BPD4",
        "G0G1_BPP4",
        "G0G1_BPS6",
        "G0G1_BPD6",
        "G0G1_BPP6",
        "G0G1_BPS8",
        "G0G1_BPD8",
        "G0G1_BPP8",
        "G0G1_BPS10",
        "G0G1_BPD10",
        "G0G1_BPP10",
    ]
    return (vars_g0g1,)


@app.cell(hide_code=True)
def _(RAW_DATA, bk, vars_g0g1):
    df_g0g1, meta_g0g1 = bk.read_sav(RAW_DATA / "G0G1_PA.sav", usecols=vars_g0g1)
    return (meta_g0g1,)


if __name__ == "__main__":
    app.run()
