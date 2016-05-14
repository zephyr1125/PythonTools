
# coding=utf-8

# 潘洁：英语导致找不到“期望从事职业”

import os
import shutil
import codecs
import re
from bs4 import BeautifulSoup

rawFolder = "D:\\my\\python\\PythonTools\\DownloadFiles\\raw\\"
publishFolder = "D:\\my\\python\\PythonTools\\DownloadFiles\\publish\\"

targetJobs = ["iOS", "Java", "UI", "产品经理", "PHP"]

def GetName(soup):
    name = "未知"
    ##猎聘网
    name = soup.find("td", width="140", style="font-size:12px")
    ##智联招聘
    if(name == "未知"):
        name = soup.find("div", class_="name")
    
    return name
    
def GetJob(soup):
    jobName = "未知"
    ##猎聘网
    currentJobNode = soup.find(string="所任职位：") #从指定的表格项查找下一个即为所任职位
    if(currentJobNode!=None):
        jobName = currentJobNode.find_next("td").string
    
    return jobName
    
def GetCompany(soup):
    companyName = "未知"
    #猎聘网
    companyNode = soup.find(string="公司名称：")
    if(companyNode!=None):
        companyName = companyNode.find_next("td").string
        
    return companyName
    
def FindKeyWord(soup):
    #使用全文搜索，只要找到关键字返回
    #因此无需判断不同的招聘网站
    for target in targetJobs:
        found = soup.find_all(text=re.compile(target, re.IGNORECASE))
        if(found):
            return target
    return "其他"
    
    # for targetJob in targetJobs:
    #     if(soup.find(string=Find(targetJob,string)) != None):
    #         return targetJob
    # return "None"

for folderName, subfolders, filenames in os.walk(rawFolder):
    for filename in filenames:
        fullPath = folderName+'\\'+filename
        # if(filename.startswith("CV")):
        if(True):
            soup = BeautifulSoup(open(fullPath, encoding='utf-8'), "html.parser", from_encoding="utf-8")
            #名字
            name = GetName(soup)
                
            #职业
            jobName = GetJob(soup)
            
            #公司
            companyName = GetCompany(soup)
            
            #改名
            newFileName = name.string+"_"+jobName+"_"+companyName+".html"
            newFileName = newFileName.strip().replace("/",".")
            newFileName = newFileName.strip().replace("*",".")
            shutil.move(fullPath, folderName+'\\'+newFileName)
            
            #转移文件夹
            keyWord = FindKeyWord(soup)
            shutil.move(fullPath, publishFolder+keyWord+'\\'+newFileName)


