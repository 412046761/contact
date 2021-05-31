# -*- codeing = utf-8 -*-
# @Time     :2021/4/30
# @Author   :ly
# @File     :downloadTest.py
# @Spftware :PyCharm

# 下载

import urllib.request

IMAGE_URL = "https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg"

local_filename, headers = urllib.request.urlretrieve(IMAGE_URL,"../jpg/p480747492.jpg")
html = open(local_filename)
html.close()
