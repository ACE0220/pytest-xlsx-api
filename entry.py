# entry.py
import inspect
import os
from pathlib import Path
import logging

import pytest
from pluggy import PluginManager
from collector.cases_collector import ExcelFileCollector
from plugin import plugins_impl, plugin_spec

logger = logging.getLogger(__name__)


# 注册插件阶段 注册control_run_step规范
def pytest_addhooks(pluginmanager: PluginManager):
    pluginmanager.add_hookspecs(plugin_spec)


# 配置阶段 注册PrintPlugin和AllurePlugin
def pytest_configure(config: pytest.Config):
    for cln, cl in inspect.getmembers(
            plugins_impl,
            lambda x: isinstance(x, type)
                      and issubclass(x, plugins_impl.ABCPlugin)
                      and x is not plugins_impl.ABCPlugin
    ):
        config.pluginmanager.register(cl(config))


# 注册option阶段
def pytest_addoption(parser):
    parser.addini(
        "is_control_sheet_active",
        default="True",
        help="控制表是否启动test，excel表的每个sheet name可以作为一个feature",
    )
    parser.addini(
        "control_sheet_name",
        default="control",
        help="控制表名，可以在pytest.ini里面配置，默认control",
    )
    parser.addini(
        "keyword_column_name",
        default="keyword",
        help="关键字列的表头名称",
    )
    parser.addini(
        "is_execute_py",
        default="False",
        help="是否执行python格式测试用例",
    )


# pytest 收集文件阶段钩子
def pytest_collect_file(parent, file_path: Path):
    if file_path.suffix == '.xlsx' and file_path.name.startswith("test_"):
        logger.debug(f"xlsx_file:{file_path.absolute()}")
        return ExcelFileCollector.from_parent(parent=parent , path=file_path)

# pytest 忽略收集文件阶段钩子，可以在pytest.ini内进行配置
def pytest_ignore_collect(collection_path, config):
    if collection_path.suffix == '.py' and collection_path.name.startswith("test_") and config.getini("is_execute_py") == "False":
        return True  # 忽略 test_*.py 文件
    return None




if __name__ == '__main__':
    # pytest.main(["-vs"])
    pytest.main(["-vs","--alluredir=reports\\json", "--clean-alluredir"])
    os.system("allure serve reports\\json -p 4000")
