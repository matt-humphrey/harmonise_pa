# This file should define the functions to harmonise each variable/dataset

from functools import partial

import polars as pl
from polars import DataFrame

# TODO: create a config file to explicitly define which variables should have which values replaced
# Do this for rounding also
# Perhaps this is unnecessary/overkill, provided it's not incorrectly replacing values

__all__ = [
    "DATA_TRANSFORMS",
    "apply_rounding",
    "harmonise_bmi",
    "harmonise_bpcd",
    "harmonise_bp_time",
    "harmonise_height",
    "harmonise_height_g0g1",
    "harmonise_mean_blood_pressure",
    "harmonise_mean_height",
    "harmonise_mean_wrist_width",
    "recast_types",
    "replace_missing_values",
]


def sort_by_id(df: DataFrame) -> DataFrame:
    return df.sort(by="ID")


def replace_missing_values(df: DataFrame) -> DataFrame:
    """Replace values for each given column that..."""
    return df.with_columns(
        pl.col(r"^.*_A([3-9]|1[0-9]|2[0-2])$").replace({-99: None, 888: None, 999: None}),
        pl.col(r"^.*_BP([1-5]|4[6-9]|[5-7][0-9]|8[01])$").replace(
            {-99: None, -88: None, 999: None}
        ),
        pl.col(r"^.*_BPCD$").replace({-99: None}),
        pl.col(r"^.*_BP_CUFF$").replace({8: None, 9: None, 99: None}),
        pl.col(r"^.*_BP_TEMP$").replace({-99: None, 999: None}),
        pl.col(r"^.*_HEIGHT$").replace({-99: None, 888: None, 999: None}),
        pl.col(r"^.*_WEIGHT$").replace({888: None, 999: None}),
    )


def apply_rounding(df: DataFrame) -> DataFrame:
    """Apply rounding to numeric columns"""
    return df.with_columns(
        pl.col(r"^.*_A([3-9]|10)$").round(1),
        pl.col(r"^.*_BP_TEMP$").round(1),
        pl.col(r"^.*_HEIGHT$").round(1),
        pl.col(r"^.*_WEIGHT$").round(2),
    )


def recast_types(df: DataFrame) -> DataFrame:
    """Recast column types as new type"""
    return df.with_columns(
        pl.col(r"^.*_BP\d+$").cast(pl.Int64),
        pl.col(r"^.*_BPCD$").cast(pl.Int64),
        pl.col(r"^.*_BP_CUFF$").cast(pl.Int64),
    )


def harmonise_height(df: DataFrame) -> DataFrame:
    """
    Harmonise `HEIGHT` variables.

    Height was initially captured in centimetres, but after G214, it was captured in metres.
    For consistency, all columns with height in metres were converted to centimetres.
    Note: G114 and G117 were captured in centimetres still.
    """
    return df.with_columns(
        pl.col(r"^.*_HEIGHT$").map_batches(lambda x: x * 100, return_dtype=pl.Float64)
    )


def harmonise_height_g0g1(df: DataFrame) -> DataFrame:
    """
    Harmonise `HEIGHT` variables.

    For G0G1 specifically, there were four errant values reported between 78 m and 86 m.
    These values were hence removed.
    """
    return df.with_columns(
        pl.col("G0G1_HEIGHT").map_batches(lambda x: x * 100, return_dtype=pl.Float64)
    ).with_columns(
        pl.when(pl.col("G0G1_HEIGHT") > 210)
        .then(None)
        .otherwise(pl.col("G0G1_HEIGHT"))
        .alias("G0G1_HEIGHT")
    )


def harmonise_mean_height(df: DataFrame) -> DataFrame:
    """
    Return the mean of the two measurements and drop the raw measurements.
    """
    return (
        df.with_columns(pl.col(r"^G228_A2[AB]$").replace({99: None}))
        .with_columns(
            pl.mean_horizontal("G228_A2A", "G228_A2B").alias("G228_HEIGHT"),
        )
        .drop("G228_A2A", "G228_A2B")
    )


def harmonise_mean_wrist_width(df: DataFrame) -> DataFrame:
    """
    Return the mean of the two measurements and drop the raw measurements.
    """
    return df.with_columns(
        pl.mean_horizontal("G220_A17A", "G220_A17B").alias("G220_A17"),
        pl.mean_horizontal("G220_A23A", "G220_A23B").alias("G220_A23"),
    ).drop("G220_A17A", "G220_A17B", "G220_A23A", "G220_A23B")


def harmonise_bmi(df: DataFrame, dset: str) -> DataFrame:
    """
    Create BMI variable from height (H) and weight (W)

    $$BMI = W/H^2$$
    """
    return df.with_columns(
        pl.when(pl.col(f"{dset}_WEIGHT").is_null() | pl.col(f"{dset}_HEIGHT").is_null())
        .then(None)
        .otherwise((pl.col(f"{dset}_WEIGHT") / (pl.col(f"{dset}_HEIGHT") / 100) ** 2).round(2))
        .alias(f"{dset}_BMI")
    )


def harmonise_bpcd(df: DataFrame) -> DataFrame:
    """
    Re-code string values to integers

    Originally -99="Missing";A="Mother nad";B="Mother pregnant";C="Mother hypertensive";
    D="Father nad";E="Father hypertensive"
    Harmonised to 0="No abnormality detected";1="Pregnant";2="Increased blood pressure"
    """
    return df.with_columns(pl.col("G105_BPCD").replace({"A": 0, "B": 1, "C": 2, "D": 0, "E": 2}))


def harmonise_mean_blood_pressure(df: DataFrame) -> DataFrame:
    """
    Return the mean systolic and diastolic blood pressures, and heart rate, for G208.

    In most cases, BP3 was the same, except 10 instances where it differed.
    For simplicity, I assumed the first instance of BP3 was correct.
    """
    return (
        df.with_columns(pl.col(r"^G208_BP[1-5]_2ND$").replace({-99: None, -88: None}))
        .with_columns(
            G208_BP1=pl.mean_horizontal("G208_BP1", "G208_BP1_2ND"),
            G208_BP2=pl.mean_horizontal("G208_BP2", "G208_BP2_2ND"),
            G208_BP5=pl.mean_horizontal("G208_BP5", "G208_BP5_2ND"),
        )
        .drop("G208_BP1_2ND", "G208_BP2_2ND", "G208_BP3_2ND", "G208_BP5_2ND")
    )


def harmonise_bp_time(df: DataFrame) -> DataFrame:
    """
    Convert G0G1_BP_TIME from seconds (Float) to Time.

    Correct two timestamps that were wrongly input.
    """
    return df.with_columns(
        pl.when(pl.col("ID").eq(185901))  # ID 185901 from 1315:00:00 to 13:15:00
        .then(47700)
        .when(pl.col("ID").eq(141701))  # ID 141701 from 1030:00:00 to 10:30:00
        .then(37800)
        .otherwise(pl.col("G0G1_BP_TIME"))
        .alias("G0G1_BP_TIME")
    ).with_columns(
        (pl.col("G0G1_BP_TIME").cast(pl.Int64) * 1000000000).cast(pl.Time).alias("G0G1_BP_TIME")
    )


initial_transforms = [replace_missing_values]
final_transforms = [apply_rounding, recast_types, sort_by_id]

dataset_transforms = {
    "G200": [],
    "G201": [partial(harmonise_bmi, dset="G201")],
    "G202": [partial(harmonise_bmi, dset="G202")],
    "G203": [partial(harmonise_bmi, dset="G203")],
    "G105": [partial(harmonise_bmi, dset="G105"), harmonise_bpcd],
    "G205": [partial(harmonise_bmi, dset="G205")],
    "G108": [partial(harmonise_bmi, dset="G108")],
    "G208": [partial(harmonise_bmi, dset="G208"), harmonise_mean_blood_pressure],
    "G210": [partial(harmonise_bmi, dset="G210")],
    "G114": [partial(harmonise_bmi, dset="G114")],
    "G214": [harmonise_height, partial(harmonise_bmi, dset="G214")],
    "G117": [partial(harmonise_bmi, dset="G117")],
    "G217": [harmonise_height, partial(harmonise_bmi, dset="G217")],
    "G220": [harmonise_height, partial(harmonise_bmi, dset="G220"), harmonise_mean_wrist_width],
    "G222": [harmonise_height, partial(harmonise_bmi, dset="G222")],
    "G227": [harmonise_height, partial(harmonise_bmi, dset="G227")],
    "G228": [harmonise_mean_height, harmonise_height, partial(harmonise_bmi, dset="G228")],
    "G126": [harmonise_height, partial(harmonise_bmi, dset="G126")],
    "G0G1": [harmonise_height_g0g1, partial(harmonise_bmi, dset="G0G1")],
}

DATA_TRANSFORMS = {
    dset: initial_transforms + transforms + final_transforms
    for dset, transforms in dataset_transforms.items()
}
