import pytest

@pytest.fixture(scope="class", autouse= True)

def result_fixture():
    print("\n Start")
    yield
    print("\n End")

class Test_1:

    @pytest.mark.from_class()
    def test_1(self):
        print("1")

    @pytest.mark.from_class()
    def test_2(self):
        print("2")

    @pytest.mark.from_class()
    def test_3(self):
        print("3")

    @pytest.mark.from_class()
    def test_4(self):
        print("4")

    @pytest.mark.from_class()
    def test_5(self):
        print("5")

