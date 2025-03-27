import re

# 定义目标字符串
string = "Hello, World! 123"
# 定义正则表达式，用于匹配数字
pattern = r'\d+'

# 使用 re.search 进行搜索
match = re.search(pattern, string)

if match:
    print("找到匹配项:", match.group())  # 输出匹配的内容
    print("匹配的起始位置:", match.start())  # 输出匹配的起始位置
    print("匹配的结束位置:", match.end())  # 输出匹配的结束位置
else:
    print("未找到匹配项")