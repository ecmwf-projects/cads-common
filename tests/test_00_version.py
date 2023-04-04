import cads_common


def test_version() -> None:
    assert cads_common.__version__ != "999"
