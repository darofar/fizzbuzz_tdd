def test_environment():
    import sys
    assert sys.version_info.major == 3
    assert sys.version_info.minor == 7
