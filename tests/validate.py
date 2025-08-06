# TODO: specify validation config in a separate config/constants file?

from polars import DataFrame
import pointblank as pb


def test_validation(df: DataFrame):
    validation = (
        pb.Validate(data=df)
        .col_vals_between(columns=pb.ends_with("HEIGHT"), left=10, right=210, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A6"), left=0, right=50, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A10"), left=0, right=60, na_pass=True)
    )

    return validation.interrogate()
