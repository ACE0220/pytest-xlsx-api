from abc import ABCMeta, abstractmethod

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
    @pytest.hookimpl(trylast=True)
    def pytest_control_run_step(self, step):
        allure.feature(step["feature"])
        allure.story(step["story"])
        allure.title(step["title"])
        allure.step(step["step"])
        allure.severity(step["severity"])
        allure.description(step["case_number"])

# print 插件
class PrintPlugin(ABCPlugin):
    @pytest.hookimpl(tryfirst=True)
    def pytest_control_run_step(self, step):
        print("-" * 10)
        print(f"feature:{step['feature']}")
        print(f"story:{step['story']}")
        print(f"case title:{step['title']}")
        print(f"step:{step['step']}")
        print(f"case_number:{step['case_number']}")
        print(f"severity:{step['severity']}")
        print(f"step_number:{step['step_number']}")
        print("=" * 20)

