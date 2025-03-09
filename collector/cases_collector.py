import logging
from typing import Iterable
import pytest
from _pytest import nodes
from pandas import DataFrame

from tools.excel_tool import read_active_sheet_name, ExcelDataIntegration
logger = logging.getLogger(__name__)

class ExcelFileCollector(pytest.Module):

    def collect(self) -> Iterable[nodes.Item | nodes.Collector]:
        is_control_str = self.config.getini("is_control_sheet_active")
        df: DataFrame = read_active_sheet_name(self.path)
        if is_control_str == "True":
            control_sheet_name = self.config.getini("control_sheet_name")
            control_sheet_content = df[control_sheet_name]
            for sheet_name in control_sheet_content[control_sheet_content["execute"] == "Y"]["module_name"].tolist():
                yield ExcelSheet.from_parent(self, name=f"{sheet_name}_sheet", data=df[sheet_name])
        else:
            for sheet_name in list(df.keys()):
                yield ExcelSheet.from_parent(self, name=f"{sheet_name}_sheet", data=df[sheet_name])

class ExcelSheet(pytest.Class):

    def __init__(self, *, data, **kwargs):
        super().__init__(**kwargs)
        self.data = ExcelDataIntegration(data).integration()
        self.data["name"] = kwargs.get("name")

    def collect(self) -> Iterable[nodes.Item | nodes.Collector]:
        for case in self.data["cases"]:
            yield  SheetCase.from_parent(self, name=case.id, data=case)

class SheetCase(pytest.Class):
    def __init__(self, *, data, **kwargs):
        super().__init__(**kwargs)
        self.data = data

    def collect(self) -> Iterable[nodes.Item | nodes.Collector]:
        for step in self.data.steps:
            yield SheetStep.from_parent(self, name=f"{step['title']}\n", data=step)

class SheetStep(pytest.Item):
    def __init__(self, *, data, **kwargs):
        super().__init__(**kwargs)
        self.data = data
    def runtest(self) -> None:
        self.config.pluginmanager.hook.pytest_control_run_step(step=self.data)
