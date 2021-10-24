from dg_calculations.conversions import volumes


def test_teaspoons_to_millimetres():
    t_millimetres = volumes.teaspoons_to_millimetres(1)
    expected = 5
    assert t_millimetres == expected


def test_millimetres_to_fluid_ounces():
    t_fluid_ounces = volumes.millimetres_to_fluid_ounces(100)
    expected = 3.381470
    assert t_fluid_ounces == expected
