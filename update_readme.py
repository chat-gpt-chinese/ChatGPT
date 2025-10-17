import datetime
import re

# 定义开始和结束标记
start_tag = "<!--START_DATE-->"
end_tag = "<!--END_DATE-->"

# 获取 README.md 内容
with open('README.md', 'r', encoding='utf-8') as f:
    readme_content = f.read()

# 获取当前 UTC+8 时间
utc_now = datetime.datetime.utcnow()
cst_now = utc_now + datetime.timedelta(hours=8)
current_date_str = cst_now.strftime('%Y-%m-%d %H:%M:%S')

# 要插入的新内容
new_date_content = f"{current_date_str} (UTC+8)"

# 使用正则表达式查找并替换标记之间的内容
# re.DOTALL 标志让 D. 匹配包括换行符在内的任意字符
pattern = f"({re.escape(start_tag)})(.*?)({re.escape(end_tag)})"
replacement = f"\\1{new_date_content}\\3"

new_readme_content = re.sub(pattern, replacement, readme_content, flags=re.DOTALL)

# 将新内容写回 README.md
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_readme_content)

print(f"README updated successfully with date: {current_date_str}")
