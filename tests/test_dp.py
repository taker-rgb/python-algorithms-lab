from src.dp import fibonacci

def test_fibonacci():
    assert fibonacci(10) == 55
    assert fibonacci(0) == 0
