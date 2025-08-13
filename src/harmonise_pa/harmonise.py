# This file should define the functions to harmonise each variable/dataset

import polars as pl
from polars import DataFrame

# TODO: create a config file to explicitly define which variables should have which values replaced
# Do this for rounding also
# Perhaps this is unnecessary/overkill, provided it's not incorrectly replacing values

__all__ = [
    "apply_rounding",
    "harmonise_bpcd",
    "harmonise_bmi",
    "harmonise_height",
    "harmonise_mean_height",
    "harmonise_mean_wrist_width",
    "recast_types",
    "replace_missing_values",
]


def replace_missing_values(df: DataFrame, dset: str) -> DataFrame:
    """Replace values for each given column that..."""
    return df.with_columns(
        pl.col(f"^{dset}_WEIGHT$").replace({888: None, 999: None}),
        pl.col(f"^{dset}_HEIGHT$").replace({-99: None, 888: None, 999: None}),
        # pl.col(f"{dset}_A3$").replace({999: None}),
        # pl.col(f"{dset}_A4$").replace({-99: None, 999: None}),
        # pl.col(f"{dset}_A5$").replace({-99: None, 999: None}),
        # pl.col(f"{dset}_A6$").replace({-99: None, 999: None}),
        # pl.col(f"{dset}_A7$").replace({-99: None, 999: None}),
        # pl.col(f"{dset}_A8$").replace({999: None}),
        # pl.col(f"{dset}_A9$").replace({999: None}),
        # pl.col(f"{dset}_A10$").replace({999: None}),
        # pl.col(f"{dset}_A12$").replace({999: None}),
        # pl.col(f"{dset}_A13$").replace({999: None}),
        # pl.col(f"{dset}_A15$").replace({999: None}),
        # pl.col(f"{dset}_BP([125]|4[6-9]|5[0-9]|6[0-3])]$").replace(
        #     {-99: None, -88: None, 999: None}
        # ),
        # pl.col(f"{dset}_BPCD$").replace({-99: None}),
    )


def apply_rounding(df: DataFrame, dset: str) -> DataFrame:
    """Apply rounding to numeric columns"""
    return df.with_columns(
        pl.col(f"{dset}_WEIGHT$").round(2),
        pl.col(f"{dset}_HEIGHT$").round(1),
        pl.col(f"{dset}_A([3-9]|10)$").round(1),
    )


def recast_types(df: DataFrame, dset: str) -> DataFrame:
    """Recast column types as new type"""
    return df.with_columns(
        pl.col(f"{dset}_BP\d+$").cast(pl.Int64),
        pl.col(f"{dset}_BPCD$").cast(pl.Int64),
    )


# TODO: re-write so it can selectively applied to the appropriate dataset
# For instance, it's going to return an error when applied to G214, because it won't contain G217_HEIGHT, nor the other variables
def harmonise_height(df: DataFrame, dset: str) -> DataFrame:
    """
    Harmonise `HEIGHT` variables.

    Height was initially captured in centimetres, but after G214, it was captured in metres.
    For consistency, all columns with height in metres were converted to centimetres.
    Note: G114 and G117 were captured in centimetres still.

    For G0G1 specifically, there were four errant values reported between 78 m and 86 m.
    These values were hence removed.
    """
    return df.with_columns(
        pl.col(
            "G214_HEIGHT",
            "G217_HEIGHT",
            "G220_HEIGHT",
            "G222_HEIGHT",
            "G227_HEIGHT",
            "G126_HEIGHT",
            "G0G1_HEIGHT",
        ).map_batches(lambda x: x * 100)
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
    return df.with_columns(
        pl.mean_horizontal("G228_A2A", "G228_A2B").alias("G228_HEIGHT"),
    ).drop("G228_A2A", "G228_A2B")


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
        (pl.col(f"{dset}_WEIGHT") / (pl.col(f"{dset}_HEIGHT") / 100) ** 2)
        .round(2)
        .alias(f"{dset}_BMI")
    )


def harmonise_bpcd(df: DataFrame) -> DataFrame:
    """
    Re-code string values to integers

    Originally -99="Missing";A="Mother nad";B="Mother pregnant";C="Mother hypertensive";D="Father nad";E="Father hypertensive"
    Harmonised to 0="No abnormality detected";1="Pregnant";2="Increased blood pressure"
    """
    return df.with_columns(pl.col("G105_BPCD").replace({"A": 0, "B": 1, "C": 2, "D": 0, "E": 2}))
