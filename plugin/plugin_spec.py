from abc import ABCMeta, abstractmethod

import pytest

# 抽象插件类
@pytest.hookspec(firstresult=True)
def pytest_control_run_step(step):
    """
    执行用例中的每一个步骤时，调用pytest_control_run_step
    这意味着对于同一个用例来讲，此hook可能被调用多次，具体调用次数取决于用例中的step数量
    :param step
    :return:
    """
    ...

