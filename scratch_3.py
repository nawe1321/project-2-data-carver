import os
import earthpy as et
import re

#OS agnostic creation of a folder for project 2, along with subdirectories for each file type
if not os.path.exists(os.path.join(et.io.HOME, "LED Zeppelin", "Project 2")):
  path = os.path.join(et.io.HOME, "LED Zeppelin", "Project 2")
  os.makedirs(path)
  for subfolder in ['png', 'jpg', 'pdf', 'gif', 'docx', 'jpg2']:
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
cwd = os.chdir(os.path.join(path, 'jpg2'))

SOFList = [match.start() for match in re.finditer(re.escape(SOF), data)]
EOFList = [match.start() for match in re.finditer(re.escape(EOF), data)]

print(SOFList)
print(EOFList)
i = 0
b = 0


for SOF in SOFList:
    subdata = data[SOF:EOFList[i] + 2]


    while EOFList[i] == EOFList[- 1]:
      carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 2) + ".jpg"
      carve_obj = open(carve_filename, 'wb')
      carve_obj.write(subdata)
      carve_obj.close()
      print("Found an image and carving it to " + carve_filename)
      #print(i)
      b = b + 1
      i = 0

    while EOFList[i] < EOFList[- 1]:
      #print(EOFList[i])
      print("S" + str(SOFList[b]))
      EOFList[i] = EOFList[i + 1]
      i += 1
      if SOFList[b] < EOFList[i]:


          print(EOFList[i])
          carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 2) + ".jpg"
          carve_obj = open(carve_filename, 'wb')
          carve_obj.write(subdata)
          carve_obj.close()
          print("Found an image and carving it to " + carve_filename)









