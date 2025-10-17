#!/bin/bash

# 设置时区为亚洲/上海
export TZ='Asia/Shanghai'

# 获取当前日期和时间，并更新 README.md
# 使用 sed 命令进行文本替换
# 注意：macOS 和 Linux 的 sed 命令语法可能略有不同，但在 GitHub Actions (Linux) 环境下这个是可行的
sed -i "s|<!--DATE-->|$(date '+%Y-%m-%d %H:%M:%S') (UTC+8)|g" README.md

echo "README updated successfully."