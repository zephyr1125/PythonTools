import os

# 命令行版工具需求
# 1.等待输入搜索范围文件夹路径
# 2.等待输入搜索文件路径
# 3.列出所有结果
# 4.回到2

def CheckFileSuffix(path):
    targetSuffixs = [r'.prefab', r'.unity', r'.controller']
    for suffix in targetSuffixs:
        if path.endswith(suffix):
            return True
    return False

guidTag = r'guid: '
targetFolderPath = input('搜索范围')

while True:
    targetFile = input('搜索文件')
    if targetFile == 'exit':
        SystemExit()

    #get GUID and Class name
    guid = ''
    metaPath = targetFile+'.meta'
    lines = open(metaPath).readlines()
    for line in lines:
        if line.startswith(guidTag):
            guid = line.lstrip(guidTag).rstrip('\n')
            print(guid)

    # search guid in prefab
    for folderName, subfolders, filenames in os.walk(targetFolderPath):
        for filename in filenames:
            fullPath = folderName+'\\'+filename
            if os.path.isfile(fullPath) and CheckFileSuffix(fullPath) and fullPath!=targetFile:
                try:
                    lines = open(fullPath).readlines()
                    for line in lines:
                        if guid in line:
                            print('找到： ' + fullPath)
                            break
                except:
                    print(fullPath + ": ERROR")

    print('搜索结束')
