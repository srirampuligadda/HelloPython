import os
import glob

listFiles = glob.glob("./*.*")
listFiles.sort()

for each in listFiles:
	print(each)