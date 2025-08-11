# TODO: specify validation config in a separate config/constants file?

from polars import DataFrame
import pointblank as pb


def test_validation(df: DataFrame):
    validation = (
        pb.Validate(data=df)
        .col_vals_between(columns=pb.ends_with("WEIGHT"), left=5, right=200, na_pass=True)
        .col_vals_between(columns=pb.ends_with("HEIGHT"), left=10, right=210, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A3"), left=30, right=120, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A4"), left=20, right=60, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A5"), left=10, right=100, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A6"), left=0, right=50, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A7"), left=1, right=50, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A8"), left=0.5, right=60, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A9"), left=0, right=60, na_pass=True)  # case with 0
        .col_vals_between(columns=pb.ends_with("A10"), left=0, right=60, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A11"), left=1, right=50, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A12"), left=30, right=180, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A13"), left=50, right=180, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A15"), left=10, right=110, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A16"), left=20, right=50, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A17"), left=4, right=8, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A18"), left=3, right=40, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A19"), left=50, right=100, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A20"), left=50, right=100, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A21"), left=50, right=100, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A22"), left=50, right=100, na_pass=True)
        .col_vals_between(columns=pb.ends_with("A23"), left=4, right=8, na_pass=True)
        .col_vals_between(columns=pb.ends_with("BP1"), left=50, right=215, na_pass=True)
        .col_vals_between(columns=pb.ends_with("BP2"), left=0, right=160, na_pass=True)
        # .col_vals_in_set(columns=pb.ends_with("BP3"), set=[1, 2, 3, None])
        # .col_vals_in_set(columns=pb.ends_with("BP4"), set=[1, 2, 3, None])
        .col_vals_between(columns=pb.ends_with("BP5"), left=30, right=140, na_pass=True)
    )

    return validation.interrogate()
