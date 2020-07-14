import os
import earthpy as et
import re
from PIL import Image


#OS agnostic creation of a folder for project 2, along with subdirectories for each file type
if not os.path.exists(os.path.join(et.io.HOME, "LED Zeppelin", "Project 2")):
  path = os.path.join(et.io.HOME, "LED Zeppelin", "Project 2")
  os.makedirs(path)
  for subfolder in ['png', 'jpg', 'pdf', 'gif', 'docx', 'jpg2', 'fragments_incomplete']:
    os.makedirs(os.path.join(path, subfolder))
  print("/LED Zeppelin/Project 2 and subfolders have been created")
else:
  path = os.path.join(et.io.HOME, "LED Zeppelin", "Project 2")
  print(path + ' already exists')
os.chdir(path)
print("Please enter your binary file into the new directory: " + path)

file_obj=open('carveit','rb')
data=file_obj.read()
file_obj.close()

SOF = b"\xFF\xD8\xFF"
EOF = b"\xFF\xD9"
cwd = os.chdir(os.path.join(path, 'jpg'))

SOFList = [match.start() for match in re.finditer(re.escape(SOF), data)]
EOFList = [match.start() for match in re.finditer(re.escape(EOF), data)]

print(SOFList)
print(EOFList)
i = 0
b = 0

while True:




        while EOFList[i] < EOFList[- 1]:
            subdata = data[SOFList[b]:EOFList[i] + 2]
            if SOFList[b] < EOFList[i]:
                carve_filename = "LEDZ_" + str(SOFList[b]) + "-" + str(EOFList[i] + 2) + ".jpg"
                with open(carve_filename, 'wb+') as carve_obj:
                    carve_obj.write(subdata)
                    try:
                        im = Image.open(carve_obj)
                        print("Found an image and carving it to " + carve_filename)
                        b += 1
                        i = 0
                        break
                    except:
                        source=os.getcwd()
                        destination=os.path.join(source,"fragments_incomplete")
                        im.close()
                        if i < len(EOFList):
                            i += 1
                        pass
            while SOFList[b] > EOFList[i] and EOFList[i] < EOFList[- 1]:
                i += 1


        else:
            subdata = data[SOFList[b]:EOFList[i] + 2]
            while SOFList[b] > EOFList[i]:
                i += 1
            if EOFList[i] == EOFList[-1]:
                carve_filename = "LEDZ" + str(SOFList[b]) + "_" + str(EOFList[i] + 2) + ".jpg"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "JPG")
                    fileBasics("JPG", carve_filename, SOFList[b], EOFList[i]+2)

                    if SOFList[b] == SOFList[-1]:
                        sys.exit()

                    else:
                        i = 0
                        b += 1
            elif len(EOFList) == 1:
                break
