from kadai_01 import formatter

def test_formatter():
    testtitele = "star wars : the empire strikes back"
    assert formatter(testtitele).startwith() == "S"