import pytest

@pytest.fixture(scope="function", autouse= True)

def result_fixture():
    print("\n Start")
    yield
    print("\n End")

levels = ["first", "second", "third", "fourth", "fifth"]
space = ["star", "sun", "moon", "earth", "comet"]
months = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]

@pytest.mark.param
@pytest.mark.parametrize("all_levels", ["first", "second", "third", "fourth", "fifth"])
def test_levels(all_levels):
    assert all_levels in levels

@pytest.mark.param
@pytest.mark.parametrize("month_numbers", [winter, spring, summer, fall])
def test_levels(month_numbers):
    assert month_numbers in months


@pytest.mark.param
@pytest.mark.parametrize("spaces", ["star", "sun", "moon", "earth", "comet"])
def test_levels(spaces):
    assert spaces in space








