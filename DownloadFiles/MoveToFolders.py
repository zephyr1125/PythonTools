import os
import re
import shutil

rootFolder = "D:\\my\\python\\PythonTools\\DownloadFiles\\files\\"
for folderName, subfolders, filenames in os.walk(rootFolder):
    for filename in filenames:
        fullPath = folderName+'\\'+filename
        #转移文件夹
        i = int(re.search('[0-9]+', filename).group(0))
        folderPath = "D:\\my\\python\\PythonTools\\DownloadFiles\\"+str(int(i/1000))
        targetPath = folderPath+"\\"+filename
        if not os.path.exists(folderPath):
            os.makedirs(folderPath)
        shutil.move(fullPath, targetPath)