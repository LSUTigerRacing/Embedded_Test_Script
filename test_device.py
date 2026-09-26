def test_unknown_command(dut):
    assert dut.query("FOO").startswith("ERR")


def test_add1_zero(dut):
    assert dut.query("ADD1 0") == "1"


def test_add1_positive(dut):
    assert dut.query("ADD1 5") == "6"


def test_add1_negative(dut):
    assert dut.query("ADD1 -1") == "0"


def test_double2_positive(dut):
    assert dut.query("Double 2") == "4"
