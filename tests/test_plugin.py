import allure


@allure.feature("fea")
@allure.story("st")
@allure.title("t")
@allure.severity("blocker")
class Test_one:
    @allure.step("test_step_1")
    def test_step_1(self):
        assert  1 == 2

    @allure.step("test_step_2")
    def test_step_2(self):
        assert  1 == 1