import os

# 命令行版工具需求
# 1.等待输入搜索范围文件夹路径
# 2.等待输入搜索tag
# 3.列出所有结果
# 4.回到2

guidTag = r'guid: '
targetFolderPath = input('搜索范围')

while True:
    targetTag = input('搜索tag')
    if targetTag == 'exit':
        SystemExit()

    # search tag in prefab
    searchLine = r'spritePackingTag: '+targetTag
    for folderName, subfolders, filenames in os.walk(targetFolderPath):
        for filename in filenames:
            fullPath = folderName+'\\'+filename
            if os.path.isfile(fullPath) and (fullPath.endswith(r'.png') or fullPath.endswith(r'.jpg')):
                try:
                    lines = open(fullPath+r'.meta').readlines()
                    for line in lines:
                        if searchLine in line:
                            print('找到： ' + fullPath)
                            break
                except:
                    print(fullPath + ": ERROR")

    print('搜索结束')
