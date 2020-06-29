import glob,os,shutil
counter =1
files = sorted(glob.iglob(os.path.join("../pipes/labels/valid/","*.txt")))

for file in files:
	if os.path.isfile(file):
		if os.stat(file).st_size != 0:
			f = open(file,"r")
			content = f.readline()
			print(content)
			f.close()
