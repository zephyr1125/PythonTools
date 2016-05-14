
# coding=utf-8

import os
import shutil
import codecs
import re
from bs4 import BeautifulSoup

rawFolder = "D:\\my\\python\\PythonTools\\DownloadFiles\\raw\\"
publishFolder = "D:\\my\\python\\PythonTools\\DownloadFiles\\publish\\"

targetJobs = ["iOS", "Java", "UI", "产品经理", "PHP"]
    
def FindKeyWord(soup):
    #使用全文搜索，只要找到关键字返回
    #因此无需判断不同的招聘网站
    for target in targetJobs:
        found = soup.find_all(text=re.compile(target, re.IGNORECASE))
        if(found):
            return target
    return "其他"

for folderName, subfolders, filenames in os.walk(rawFolder):
    for filename in filenames:
        fullPath = folderName+'\\'+filename
        if not filename.startswith("CV"):
            soup = BeautifulSoup(open(fullPath, encoding='utf-8'), "html.parser", from_encoding="utf-8")
            #转移文件夹
            keyWord = FindKeyWord(soup)
            shutil.move(fullPath, publishFolder+keyWord+'\\'+newFileName)


