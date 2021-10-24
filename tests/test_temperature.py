from dg_calculations.conversions import temperature


def test_centigrade_to_fahrenheit():
    t_fahrenheit = temperature.centigrade_to_fahrenheit(35)
    expected = 95
    assert t_fahrenheit == expected


def test_fahrenheit_to_centigrade():
    t_centigrade = temperature.fahrenheit_to_centigrade(95)
    expected = 35
    assert t_centigrade == expected
