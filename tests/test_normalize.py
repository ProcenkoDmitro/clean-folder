import pytest

from clean_folder.clean import normalize


def load_normalize(a):
    return ''.join(normalize(a))


@pytest.mark.parametrize(
    "a, b", [('ї', 'yi'), ('Ї', 'Yi'), ('ь', '')]
)
def test_rename(a, b):
    assert load_normalize(a) == b
