
# coding=utf-8

import os
import shutil
import codecs
import re
import random
from bs4 import BeautifulSoup

folderStart = input("起始")
folderEnd = input("结束")
rawFolder = "D:\\my\\python\\PythonTools\\DownloadFiles\\files\\"
publishFolder = "D:\\my\\python\\PythonTools\\DownloadFiles\\publish\\"

targetJobs = ["iOS", "Java", "UI", "产品经理", "PHP"]

def GetName(soup):    
    #猎聘
    if "猎聘" in soup.title.string:
        name = soup.find("td", width="140", style="font-size:12px")
        if(name!=None):
            return name.string
        
    #智联
    if "智联" in soup.title.string:
        name = soup.find("div", class_="name")
        if(name!=None):
            return name.string
    
    return "未知"
    
def GetJob(soup):
    #猎聘
    if "猎聘" in soup.title.string:
        currentJobNode = soup.find(string="所任职位：") #从指定的表格项查找下一个即为所任职位
        if(currentJobNode!=None):
            return currentJobNode.find_next("td").string
    
    #智联
    if "智联" in soup.title.string:
        currentJobNode = soup.find(string="工作经历") #从指定的表格项查找下两项的第3段即为所任职位
        if(currentJobNode!=None):
            work = currentJobNode.find_next("td").find_next_sibling("td").contents[0]
            return work.split('|')[-1]
        else:
            #找不到工作经历项，说明没有工作经历
            return "无"
    
    return "未知"
    
def GetCompany(soup):
    #猎聘
    if "猎聘" in soup.title.string:
        companyNode = soup.find(string="公司名称：")
        if(companyNode!=None):
            return companyNode.find_next("td").string
        
    #智联
    if "智联" in soup.title.string:
        currentJobNode = soup.find(string="工作经历") #从指定的表格项查找下两项的第1段即为所任职位
        if(currentJobNode!=None):
            work = currentJobNode.find_next("td").find_next_sibling("td").contents[0]
            return work.split('|')[0]
        else:
            #找不到工作经历项，说明没有工作经历
            return "无"
        
    return "未知"

def FindKeyWord(soup):
    #使用全文搜索，只要找到关键字返回
    #因此无需判断不同的招聘网站
    for target in targetJobs:
        found = False
        if target == "UI":
            #对UI要匹配大小写且前后不能有英文，出现超过1次
            result = soup.find_all(text=re.compile("([^a-zA-Z]|^)UI([^a-zA-Z]|$)"))
            found = len(result)>1
        elif target == "iOS":
            #对iOS要前后不能有英文，出现超过1次
            result = soup.find_all(text=re.compile("([^a-zA-Z]|^)iOS([^a-zA-Z]|$)", re.IGNORECASE))
            found = len(result)>1
        elif target == "PHP" or target == "Java":
            #出现超过1次
            result = soup.find_all(text=re.compile(target, re.IGNORECASE))
            found = len(result)>1
        else:
            found = soup.find_all(text=re.compile(target, re.IGNORECASE))
        if(found):
            return target
    return "其他"

for folder in range(int(folderStart), int(folderEnd)+1):
    print("start "+str(folder))
    for folderName, subfolders, filenames in os.walk(rawFolder+str(folder)):
        for filename in filenames:
            fullPath = folderName+'\\'+filename
            # if(filename.startswith("CV")):
            if(True):
                try:
                    soup = BeautifulSoup(open(fullPath, encoding='utf-8'), "html.parser", from_encoding="utf-8")
                    #名字
                    name = GetName(soup).strip()
                        
                    #职业
                    jobName = GetJob(soup).strip()
                    
                    #公司
                    companyName = GetCompany(soup).strip()
                    
                    #改名
                    newFileName = name+"_"+jobName+"_"+companyName
                    newFileName = newFileName.strip().replace("/",".")
                    newFileName = newFileName.strip().replace("\\",".")
                    newFileName = newFileName.strip().replace("*",".")
                    
                    #转移文件夹
                    if not ("未知" in newFileName):
                        keyWord = FindKeyWord(soup)
                        targetPath = publishFolder+keyWord+'\\'+newFileName+".html"
                        if(os.path.exists(targetPath)):
                            newFileName+=re.search("[0-9]{6}", filename).group(0)
                            targetPath = publishFolder+keyWord+'\\'+newFileName+".html"
                        print("move: "+newFileName)
                        shutil.move(fullPath, targetPath)
                    
                except Exception as e:
                    print(e)


