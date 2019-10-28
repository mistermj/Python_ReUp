import os

for root, dirs, files in os.walk(os.getcwd()):
	print(root)
	for file in files:
		if file.endswith('.xml'):
			print(file)
			os.remove(os.path.join(root, file))
		else:
			pass
    # os.remove(file)
    # print(file)
    # if file.endswith('.xml'):
    #     print(str(file))
    #     print('---------')
    #     os.remove(file)


