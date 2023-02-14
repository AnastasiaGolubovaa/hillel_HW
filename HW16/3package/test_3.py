import pytest

@pytest.fixture(scope="function", autouse= True)

def result_fixture():
    print("\n Start")
    yield
    print("\n End")

@pytest.mark.pack()
@pytest.mark.joint()
def test_1():
    print("1")

@pytest.mark.pack()
@pytest.mark.joint()
def test_2():
    print("2")

@pytest.mark.pack()
@pytest.mark.rest()
def test_3():
    print("3")

@pytest.mark.pack()
@pytest.mark.rest()
def test_levels():
    assert list(reversed([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]