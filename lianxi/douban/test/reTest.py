# -*- codeing = utf-8 -*-
# @Time     :2021/4/29
# @Author   :ly
# @File     :reTest.py
# @Spftware :PyCharm
# 正则

import re

# 创建模式对象
pat = re.compile("AA")        # 用来去验证其他的字符串
m = pat.search("CBA")         # 校验是否符合  不符合 None
print(m)
m = pat.search("CBAA")        # 符合 <re.Match object; span=(2, 4), match='AA'>
print(m)
# 没有模式对象
m = re.search("asd","AAasd")  # 前面的字符串是规则（模板），后面的字符串是被校验的对象
print(m)

# 查出符合的对象
print(re.findall("[A-Z]","ASDaSIAa"))
print(re.findall("[A-Z]+","ASDaSIAa"))

# sub    将 a 换成A  被换对象
m = re.sub("a","A","abcda")
print(m)

# 建议正则中，被比较的字符串前加r，不用担心转义字符的问题
a = r"\aabd-;\'"
print(a)