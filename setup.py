from importlib.metadata import entry_points
from pathlib import Path

from setuptools import setup

# 读取 requirements.txt 文件
def read_requirements():
    requirements_path = Path(__file__).parent / "requirements.txt"
    with open(requirements_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name = "pytest-xlsx-api",
    version = "0.1",
    author = "ace020",
    description="xlsx文件作为api用例",
    packages=['pytest_xlsx_api'],
    package_data={
        "pytest_xlsx_api": ["*"],  # 包含 pytest-xlsx-api 目录下的所有文件及 data 目录下的文件
    },
    package_dir={"pytest_xlsx_api": "."},
    entry_points={
        'pytest11': [
            'pytest_xlsx_api = entry'
        ]
    },
    install_requires=read_requirements()
)