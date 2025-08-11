# This file should define the functions to harmonise each variable/dataset

import polars as pl
from polars import DataFrame

# TODO: create a config file to explicitly define which variables should have which values replaced
# Do this for rounding also
# Perhaps this is unnecessary/overkill, provided it's not incorrectly replacing values


def replace_missing_values(df: DataFrame) -> DataFrame:
    """Replace values for each given column that..."""
    return df.with_columns(
        pl.col("^.*WEIGHT$").replace({888: None, 999: None}),
        pl.col("^.*HEIGHT$").replace({-99: None, 888: None, 999: None}),
        pl.col("^.*A3$").replace({999: None}),  # 999 for all
        pl.col("^.*A4$").replace({-99: None, 999: None}),  # -99 for G200, 999 for G201 to G210
        pl.col("^.*A5$").replace({-99: None, 999: None}),  # -99 for G200, 999 for G201 on
        pl.col("^.*A6$").replace({-99: None, 999: None}),  # -99 for G200, 999 for all bar G114/G227
        pl.col("^.*A7$").replace({-99: None, 999: None}),  # -99 for G200, 999 for all bar G220/G227
        pl.col("^.*A8$").replace({999: None}),  # 999 for all bar G220 and G227
        pl.col("^.*A9$").replace({999: None}),  # 999 for all bar G220 and G227
        pl.col("^.*A10$").replace({999: None}),  # 999 for all bar G220 and G227
        pl.col("^.*A12$").replace({999: None}),
        pl.col("^.*A13$").replace({999: None}),
        pl.col("^.*A15$").replace({999: None}),
        pl.col("^.*BP[1-2]$").replace({-99: None, -88: None, 999: None}),
    )


def apply_rounding(df: DataFrame) -> DataFrame:
    """Apply rounding to numeric columns"""
    return df.with_columns(
        pl.col("^.*WEIGHT$").round(decimals=2, mode="half_away_from_zero"),
        pl.col("^.*HEIGHT$").round(decimals=1, mode="half_away_from_zero"),
        pl.col("^.*A([3-9]|10)$").round(decimals=1, mode="half_away_from_zero"),
    )


def recast_types(df: DataFrame) -> DataFrame:
    """Recast column types as new type"""
    return df.with_columns(
        pl.col("^.*BP[1-5]$").cast(pl.Int64),
    )


def harmonise_height(df: DataFrame) -> DataFrame:
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
