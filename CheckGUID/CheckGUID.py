import os

# 命令行版工具需求
# 1.等待输入搜索范围文件夹路径
# 2.等待输入搜索文件路径
# 3.列出所有结果
# 4.回到2

guidTag = r'guid: '
targetFolderPath = input('搜索范围')

while True:
    targetFile = input('搜索文件')
    if targetFile == 'exit':
        SystemExit()

    #get GUID
    guid = ''
    metaPath = targetFile+'.meta'
    lines = open(metaPath).readlines()
    for line in lines:
        if line.startswith(guidTag):
            guid = line.lstrip(guidTag)
            print(guid)
            break

    # search
    for folderName, subfolders, filenames in os.walk(targetFolderPath):
        for filename in filenames:
            fullPath = folderName+'\\'+filename
            if os.path.isfile(fullPath) and (fullPath.endswith('.prefab') or fullPath.endswith('.unity')) and fullPath!=targetFile:
                try:
                    lines = open(fullPath).readlines()
                    for line in lines:
                        if guid in line:
                            print(fullPath)
                except:
                    print(fullPath + ": ERROR")
