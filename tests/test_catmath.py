from catinabox import catmath


def test__cat_years_to_hooman_years__middle_age__succeeds():
    assert catmath.cat_years_to_hooman_years(3) == 15
    assert catmath.cat_years_to_hooman_years(100) == 500
    assert catmath.cat_years_to_hooman_years(20) == 100


def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    assert catmath.cat_years_to_hooman_years(0.5) == 2.5
    assert catmath.cat_years_to_hooman_years(0.1) == 0.5
    assert catmath.cat_years_to_hooman_years(0.001) == 0.005


def test__cat_years_to_hooman_years__0__returns_0():
    assert catmath.cat_years_to_hooman_years(0) == 0


# BONUS MATERIAL FOR STEP 2


def test__is_cat_leap_year__succeeds():
    assert catmath.is_cat_leap_year(2016) is True
    assert catmath.is_cat_leap_year(2012) is True
