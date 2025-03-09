import json
from typing import List, Any
import pandas as pd
from pandas import DataFrame
from models.models import Case, Suite
from tools.replace_var import replace_placeholders


def read_active_sheet_name(excel_file_path, sheet_name: str | None = None):
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    return df

class ExcelDataIntegration:

    def __init__(self, df:DataFrame):
        self.excel_data = df
        self.heads = self._get_headers()
        self.contents = self._get_contents()


    def _get_headers(self) -> List[str]:
        return self.excel_data.columns.tolist()

    def _get_contents(self) -> List[List[str]]:
        return self.excel_data.values.tolist()

    def _convert_params(self, params, params_type):
        """
        根据 params_type 转换 params
        :param params: 参数值
        :param params_type: 参数类型
        :return: 转换后的参数值
        """
        if params_type == "json" and isinstance(params, str):
            try:
                return json.loads(params)  # 转换为字典
            except json.JSONDecodeError:
                return params  # 转换失败，保留原始值
        return params  # 非 json 类型，保留原始值

    def integration(self):
        cases = []
        grouped = self.excel_data.groupby("case_number")
        for case_number,group in grouped:
            _meta = {
                "case_number":case_number,
                "feature": group["feature"].iloc[0],
                "story": group["story"].iloc[0],
                "severity": group["severity"].iloc[0],
            }
            _steps = []
            for _, row in group.iterrows():
                step = {
                    "feature": row["feature"],
                    "story": row["story"],
                    "title": row["title"],
                    "step": row["step"],
                    "case_number": row["case_number"],
                    "step_number": row["step_number"],
                    "severity": row["severity"],
                    "url": row["url"],
                    "keyword": row["keyword"],
                    "headers": json.loads(row["headers"]),
                    "params": self._convert_params(row["params"], row["params_type"]),
                    "params_type": row["params_type"],
                    "assertFields": row["assertFields"],
                    "expected_value": row["expected_value"],
                    "extract": row["extract"],
                    "json_express": row["json_express"]
                }
                step = replace_placeholders(step)
                _steps.append(step)
            case = Case(
                id=str(case_number),
                meta=_meta,
                steps=_steps
            )
            cases.append(case)
        return dict(Suite(
            name= "",
            cases = cases
        ))







if __name__ == '__main__':
    read_active_sheet_name("E:\\test_learning\pytest-xlsx-control\\tests\\test_cases_users.xlsx")
