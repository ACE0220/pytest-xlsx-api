# pytest-xlsx-api

## 实现功能
1. xlsx文件sheet作为feature, row作为用例step,多个row组成case
    - control sheet可以作为控制开关
    - 通过pytest.ini配置可以和test_\*.py共存，也可以单独识别test_\*.xlsx
2. 模板字符串替换，自动查找全局变量（例如调用login后，其他接口的header替换token值）
3. 自定义hook方便接入关键字层，通过hook实现更高的自由度
4. 接入allure报告

## 待实现功能

1. 未接入pytest的前后置夹具（但全局变量的保存功能可以暂时替代一下）
2. 用例跳过功能未接入，当前只能控制sheet级别的启动与关闭
3. xlsx用例文件不支持读取动态表头与扩展

## 项目运行

python version 3.11

```
# 设置完虚拟环境记得配置一下pycharm的python解释器
python -m venv venv
pip install -r requirements.txt
# 本地测试
python install -e .
python entry.py
```




## API参考

TODO~

### 配置项
### hook钩子