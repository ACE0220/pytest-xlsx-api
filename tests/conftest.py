import random
import time

import allure


def pytest_control_run_step(step):
    num1 = random.random()
    num2= random.random()
    allure.attach(str({"test:1"}), "返回数据")
    time.sleep(5)
    assert  num1 >= num2

