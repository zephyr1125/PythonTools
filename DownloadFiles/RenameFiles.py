
# coding=utf-8

import os
import shutil
import codecs
import re
from bs4 import BeautifulSoup

rawFolder = "D:\\my\\python\\PythonTools\\DownloadFiles\\raw\\"

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


