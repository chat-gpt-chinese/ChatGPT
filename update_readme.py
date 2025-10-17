import datetime
import re

# 获取 README.md 内容
with open('README.md', 'r', encoding='utf-8') as f:
    readme_content = f.read()

# 获取当前 UTC+8 时间
# GitHub Actions 默认使用 UTC 时间，我们需要转换为东八区时间
# 如果你不需要转换，可以直接使用 datetime.datetime.utcnow()
utc_now = datetime.datetime.utcnow()
cst_now = utc_now + datetime.timedelta(hours=8)
current_date = cst_now.strftime('%Y-%m-%d %H:%M:%S')

# 使用正则表达式替换占位符
new_readme_content = re.sub(r'<!--DATE-->', f'{current_date} (UTC+8)', readme_content)

# 将新内容写回 README.md
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_readme_content)

print(f"README updated with date: {current_date}")