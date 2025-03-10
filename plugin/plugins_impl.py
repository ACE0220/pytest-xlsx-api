import json
from abc import ABCMeta, abstractmethod

# import allure
import allure
import pytest
from pytest import FixtureRequest, Config


# 抽象插件类
class ABCPlugin(metaclass=ABCMeta):
    def __init__(self, config: Config):
        self.config = config
        self.__name__ = self.__class__.__name__

    @abstractmethod
    def pytest_control_run_step(self, step):
        """"""

# allure 插件
class AllurePlugin(ABCPlugin):
    @pytest.hookimpl(tryfirst=True)
    def pytest_control_run_step(self, step):
        allure.dynamic.feature(step["feature"])
        allure.dynamic.story(step["story"])
        allure.dynamic.title(step["title"])
        allure.dynamic.severity(step["severity"])
        allure.attach(str(step["url"]),"url")
        allure.attach(str(step["keyword"]),"keyword")
        allure.attach(str(step["headers"]),"headers")
        allure.attach(str(step["params"]),"params")
        allure.attach(str(step["params_type"]),"params_type")
        allure.attach(str(step["assertFields"]),"assertFields")
        allure.attach(str(step["expected_value"]),"expected_value")
        allure.attach(str(step["extract"]),"extract")
        allure.attach(str(step["json_express"]),"json_express")
        with allure.step(step["step"]):
            ...
        # pass

# print 插件
class PrintPlugin(ABCPlugin):
    @pytest.hookimpl(trylast=True)
    def pytest_control_run_step(self, step):
        print(f"feature:{step['feature']}")
        print(f"story:{step['story']}")
        print(f"case title:{step['title']}")
        print(f"step:{step['step']}")
        print(f"case_number:{step['case_number']}")
        print(f"severity:{step['severity']}")
        print(f"step_number:{step['step_number']}")
        print("-" * 20)

