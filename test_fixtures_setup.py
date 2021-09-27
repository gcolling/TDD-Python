import pytest

@pytest.fixture(autouse=True)
def setup():
    print('\nSetup')

def test1(setup):
    print('\nTesting test1!')
    assert True

@pytest.mark.usefixtures("setup")
def test2():
    print('\nTesting test2!')
    assert True