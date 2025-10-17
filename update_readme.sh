#!/bin/bash

# 设置时区
export TZ='Asia/Shanghai'

# 获取当前日期和时间
CURRENT_DATE="$(date '+%Y-%m-%d %H:%M:%S')"
NEW_CONTENT="<!--START_DATE-->${CURRENT_DATE} (UTC+8)<!--END_DATE-->"

# 使用 awk 进行替换，这种方法比 sed 更健壮
awk -v new_content="$NEW_CONTENT" '
BEGIN {p=1}
/<!--END_DATE-->/ {print new_content; p=1; next}
/<!--START_DATE-->/ {p=0}
p {print}
' README.md > README.md.tmp && mv README.md.tmp README.md

echo "README updated successfully."
