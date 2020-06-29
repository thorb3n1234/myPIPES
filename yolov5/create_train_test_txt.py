import os
import sys


a = open("data/train.txt", "w")
for file in os.listdir("../pipes/images/train/"):
	if file.endswith('.jpg'):
		a.write("../pipes/images/train/"+ str(file) + os.linesep)
		#a.write("../GIT_DATA/ML_DATA/data/data/train/"+ str(file) + os.linesep)

a.close()

b = open("data/test.txt", "w")
for file in os.listdir("../pipes/images/valid"):
	if file.endswith('.jpg'):
		b.write("../pipes/images/valid/"+ str(file) + os.linesep)
		#b.write("../GIT_DATA/ML_DATA/data/data/test/"+ str(file) + os.linesep)
b.close()

