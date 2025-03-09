import re

from global_context.context import get_from_context

def _replace_variables(text):
    """
    替换文本中的变量占位符（如 {TOKEN}）
    :param text: 原始文本
    :return: 替换后的文本
    """
    new_text = get_from_context(text)
    fn_text = text.replace(text, new_text if new_text else text)
    return str(fn_text)

def replace_placeholders(data):
    if isinstance(data, dict):
        # 处理字典
        return {key: replace_placeholders(value) for key, value in data.items()}
    elif isinstance(data, list):
        # 处理列表
        return [replace_placeholders(item) for item in data]
    elif isinstance(data, str):
        # 处理字符串
        def replace_match(match):
            placeholder = match.group(0)  # 获取占位符，如 "{user_id}"
            key = placeholder[1:-1]  # 去掉 {}，获取 key，如 "user_id"
            return _replace_variables(key)  # 替换为上下文中的值，如果不存在则保留占位符
        return re.sub(r"\{.*?}", replace_match, data)
    else:
        # 其他类型（如数字、布尔值）直接返回
        return data