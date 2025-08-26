import pointblank as pb
from pointblank import Validate


def validate_weight(v: Validate) -> Validate:
    return v.col_vals_between(
        columns=pb.matches(r"G\w{3}_WEIGHT$"), left=5, right=200, na_pass=True
    )


def validate_height(v: Validate) -> Validate:
    return v.col_vals_between(
        columns=pb.matches(r"G\w{3}_HEIGHT$"), left=10, right=210, na_pass=True
    )


def validate_a3(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A3$"), left=30, right=120, na_pass=True)


def validate_a4(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A4$"), left=20, right=60, na_pass=True)


def validate_a5(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A5$"), left=10, right=100, na_pass=True)


def validate_a6(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A6$"), left=4, right=65, na_pass=True)


def validate_a7(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A7$"), left=1, right=50, na_pass=True)


def validate_a8(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A8$"), left=0.5, right=60, na_pass=True)


def validate_a9(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A9$"), left=1.5, right=60, na_pass=True)


def validate_a10(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A10$"), left=1.5, right=60, na_pass=True)


def validate_a11(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A11$"), left=1, right=50, na_pass=True)


def validate_a12(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A12$"), left=30, right=180, na_pass=True)


def validate_a13(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A13$"), left=50, right=180, na_pass=True)


def validate_a15(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A15$"), left=10, right=110, na_pass=True)


def validate_a16(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A16$"), left=20, right=50, na_pass=True)


def validate_a17(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A17$"), left=4, right=8, na_pass=True)


def validate_a18(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A18$"), left=3, right=40, na_pass=True)


def validate_a19(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A19$"), left=50, right=100, na_pass=True)


def validate_a20(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A20$"), left=50, right=100, na_pass=True)


def validate_a21(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A21$"), left=50, right=100, na_pass=True)


def validate_a22(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A22$"), left=50, right=100, na_pass=True)


def validate_a23(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_A23$"), left=4, right=8, na_pass=True)


def validate_bp1(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_BP1$"), left=40, right=220, na_pass=True)


def validate_bp2(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_BP2$"), left=25, right=220, na_pass=True)


def validate_bp3(v: Validate) -> Validate:
    return v.col_vals_in_set(columns=pb.matches(r"G\w{3}_BP3$"), set=[1, 2, 3, None])


def validate_bp4(v: Validate) -> Validate:
    return v.col_vals_in_set(columns=pb.matches(r"G\w{3}_BP4$"), set=[1, 2, 3, None])


def validate_bp5(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_BP5$"), left=30, right=140, na_pass=True)


def validate_bp_sys(v: Validate) -> Validate:
    return v.col_vals_between(
        columns=pb.matches(r"G\w{3}_BP(4[69]|5[258]|61)$"), left=30, right=220, na_pass=True
    )


def validate_bp_dias(v: Validate) -> Validate:
    return v.col_vals_between(
        columns=pb.matches(r"G\w{3}_BP(47|5[0369]|62)$"), left=30, right=220, na_pass=True
    )


def validate_bp_hr(v: Validate) -> Validate:
    return v.col_vals_between(
        columns=pb.matches(r"G\w{3}_BP(48|5[147]|6[03])$"), left=30, right=140, na_pass=True
    )


def validate_bp_temp(v: Validate) -> Validate:
    return v.col_vals_between(
        columns=pb.matches(r"G\w{3}_BP_TEMP$"), left=10, right=35, na_pass=True
    )


def validate_bp_cuff(v: Validate) -> Validate:
    return v.col_vals_between(columns=pb.matches(r"G\w{3}_BP_CUFF$"), left=1, right=4, na_pass=True)


# .col_vals_between(
#     columns=pb.ends_with("BP_TIME$"), left=time(8), right=time(17), na_pass=True
# )

VALIDATIONS = {
    "WEIGHT": validate_weight,
    "HEIGHT": validate_height,
    "A3": validate_a3,
    "A4": validate_a4,
    "A5": validate_a5,
    "A6": validate_a6,
    "A7": validate_a7,
    "A8": validate_a8,
    "A9": validate_a9,
    "A10": validate_a10,
    "A11": validate_a11,
    "A12": validate_a12,
    "A13": validate_a13,
    "A15": validate_a15,
    "A16": validate_a16,
    "A17": validate_a17,
    "A18": validate_a18,
    "A19": validate_a19,
    "A20": validate_a20,
    "A21": validate_a21,
    "A22": validate_a22,
    "A23": validate_a23,
    "BP1": validate_bp1,
    "BP2": validate_bp2,
    "BP3": validate_bp3,
    # "BP4": validate_bp4,
    "BP5": validate_bp5,
    "BP46": validate_bp_sys,
    "BP47": validate_bp_dias,
    "BP48": validate_bp_hr,
    "BP_TEMP": validate_bp_temp,
    "BP_CUFF": validate_bp_cuff,
    # "BP_TIME": validate_bp_time,
}
