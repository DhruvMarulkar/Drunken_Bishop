from drunken_bishop.core import drunken_bishop


def test_same_input_same_output():
    """
    Same input should always produce the same fingerprint
    (deterministic behavior).
    """
    out1 = drunken_bishop("hello", animate=False)
    out2 = drunken_bishop("hello", animate=False)
    assert out1 == out2


def test_different_input_different_output():
    """
    Small change in input should change the fingerprint
    (avalanche effect).
    """
    out1 = drunken_bishop("hello", animate=False)
    out2 = drunken_bishop("hello!", animate=False)
    assert out1 != out2


def test_output_not_empty():
    """
    Function should always return a non-empty fingerprint.
    """
    output = drunken_bishop("test", animate=False)
    assert output is not None
    assert len(output.strip()) > 0
