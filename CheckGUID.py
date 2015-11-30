import os

examplePath = 'Example'
listAllFile = []
listMeta = []
listGUID = []
listTimes = []

#find all meta files for files, which means except folder's meta
for folderName, subFolders, fileNames in os.walk(examplePath):
	for fileName in fileNames:
		wholePath = os.path.join(folderName, fileName)
		listAllFile.append(wholePath)
		if os.path.isfile(wholePath) and not fileName.endswith('.meta')
			listMeta.append(wholePath+'.meta')

#get all GUIDs in meta files
for filePath in listMeta:
	readLines = open(filePath).readlines()
	for line in readLines:
		if line.startswith('guid: '):
			listGUID.append(line.lstrip('guid: ').rstrip('\n'))

print(listGUID)

#record GUID times in all prefabs
for filePath in listAllFile:
	if filePath.endswith('prefab'):
		print(filePath)
		readAll = open(filePath).read()
		for i, guid in enumerate(listGUID):
			if guid in readAll:
				print('find :' + guid)
				if len(listTimes)>i:
					listTimes[i] += 1
				else:
					listTimes.insert(i, 1)


#show all file's referenced times
for i, file in enumerate(listMeta):
	print(file + ": " + str(listTimes[i]))