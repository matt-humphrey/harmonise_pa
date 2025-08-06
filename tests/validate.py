# TODO: specify validation config in a separate config/constants file?

from polars import DataFrame
import pointblank as pb


def test_validation(df: DataFrame):
    validation = (
        pb.Validate(data=df)
        .col_vals_between(columns=pb.ends_with("HEIGHT"), left=10, right=210, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A3"), left=30, right=120, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A4"), left=20, right=60, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A5"), left=10, right=100, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A6"), left=0, right=50, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A7"), left=1, right=50, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A8"), left=0.5, right=60, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A9"), left=0, right=60, na_pass=True)  # case with 0
        .col_vals_between(columns=pb.ends_with("A10"), left=0, right=60, na_pass=True)
    )

    return validation.interrogate()
