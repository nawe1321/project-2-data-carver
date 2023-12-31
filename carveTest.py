import hashlib
import os
import earthpy as et
import re

#OS agnostic creation of a folder for project 2, along with subdirectories for each file type
if not os.path.exists(os.path.join(et.io.HOME, "LED Zeppelin", "Project 2")):
  path = os.path.join(et.io.HOME, "LED Zeppelin", "Project 2")
  os.makedirs(path)
  for subfolder in ['png', 'jpg', 'pdf', 'gif']:
    os.makedirs(os.path.join(path, subfolder))
  print("/LED Zeppelin/Project 2 and subfolders have been created")
else:
  path = os.path.join(et.io.HOME, "LED Zeppelin", "Project 2")
  print(path + ' already exists')
os.chdir(path)
print("Please enter your binary file into the new directory: " + path)

#Accept binary file
fname = input("Enter a file name: ")
file_obj = open(fname, 'rb')
data = file_obj.read()
file_obj.close()

def pngcarve():
  SOF = b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a"
  EOF = b"\x49\x45\x4e\x44\xae\x42\x60\x82"
  cwd = os.chdir(os.path.join(path, 'png'))

  SOFList = [match.start() for match in re.finditer(re.escape(SOF), data)]
  EOFList = [match.start() for match in re.finditer(re.escape(EOF), data)]

  print(SOFList)
  print(EOFList)

  i = 0
  for SOF in SOFList:
    subdata = data[SOF:EOFList[i] + 8]
    if int(EOFList[i]) > int(SOF):
      carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 7) + ".png"
      carve_obj = open(carve_filename, 'wb')
      carve_obj.write(subdata)
      carve_obj.close()
      i = i + 1
      print("Found an image and carving it to " + carve_filename)
    else:
      while int(EOFList[i]) < int(SOF):
        EOFList[i] = EOFList[i + 1]
        i = i + 1
      carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 7) + ".png"
      carve_obj = open(carve_filename, 'wb')
      carve_obj.write(subdata)
      carve_obj.close()
      i = i + 1
      print("Found an image and carving it to " + carve_filename)


def jpgcarve():
  SOF = b"\xFF\xD8\xFF"
  EOF = b"\xFF\xD9"
  cwd = os.chdir(os.path.join(path, 'jpg'))

  SOFList = [match.start() for match in re.finditer(re.escape(SOF), data)]
  EOFList = [match.start() for match in re.finditer(re.escape(EOF), data)]

  print(SOFList)
  print(EOFList)

  i = 0
  for SOF in SOFList:
    subdata = data[SOF:EOFList[i] + 2]
    if int(EOFList[i]) > int(SOF):
      carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 1) + ".jpg"
      carve_obj = open(carve_filename, 'wb')
      carve_obj.write(subdata)
      carve_obj.close()
      i = i + 1
      print("Found an image and carving it to " + carve_filename)
    else:
      while int(EOFList[i]) < int(SOF):
        EOFList[i] = EOFList[i + 1]
        i = i + 1
      carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 1) + ".jpg"
      carve_obj = open(carve_filename, 'wb')
      carve_obj.write(subdata)
      carve_obj.close()
      i = i + 1
      print("Found an image and carving it to " + carve_filename)

def pdfcarve():
  SOF = b"\x25\x50\x44\x46"
  EOF = b"\x0A\x25\x25\x45\x4F\x46"
  cwd = os.chdir(os.path.join(path, 'pdf'))

  SOFList = [match.start() for match in re.finditer(re.escape(SOF), data)]
  EOFList = [match.start() for match in re.finditer(re.escape(EOF), data)]

  print(SOFList)
  print(EOFList)

  i = 0
  for SOF in SOFList:
    subdata = data[SOF:EOFList[i] + 6]
    if int(EOFList[i]) > int(SOF):
      carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 5) + ".pdf"
      carve_obj = open(carve_filename, 'wb')
      carve_obj.write(subdata)
      carve_obj.close()
      i = i + 1
      print("Found a file and carving it to " + carve_filename)
    else:
      while int(EOFList[i]) < int(SOF):
        EOFList[i] = EOFList[i + 1]
        i = i + 1
      carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 5) + ".pdf"
      carve_obj = open(carve_filename, 'wb')
      carve_obj.write(subdata)
      carve_obj.close()
      i = i + 1
      print("Found a file and carving it to " + carve_filename)

def gifcarve():
  SOF = b"\x47\x49\x46\x38"
  EOF = b"\x00\x3B"
  cwd = os.chdir(os.path.join(path, 'gif'))

  SOFList = [match.start() for match in re.finditer(re.escape(SOF), data)]
  EOFList = [match.start() for match in re.finditer(re.escape(EOF), data)]

  print(SOFList)
  print(EOFList)

  i = 0
  for SOF in SOFList:
    subdata = data[SOF:EOFList[i] + 2]
    if int(EOFList[i]) > int(SOF):
      carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 1) + ".gif"
      carve_obj = open(carve_filename, 'wb')
      carve_obj.write(subdata)
      carve_obj.close()
      i = i + 1
      print("Found an image and carving it to " + carve_filename)
    else:
      while int(EOFList[i]) < int(SOF):
        EOFList[i] = EOFList[i + 1]
        i = i + 1
      carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 1) + ".gif"
      carve_obj = open(carve_filename, 'wb')
      carve_obj.write(subdata)
      carve_obj.close()
      i = i + 1
      print("Found an image and carving it to " + carve_filename)

#Write MD5 hash of carved file
def fileHash():
    BLOCKSIZE = 65536
    #file type menu
    print(
        "Select the folder location of the file you would like to hash: \n" \
        + " Press 1 for gif \n" \
        + " Press 2 for jpg \n" \
        + " Press 3 for pdf \n" \
        + " Press 4 for png \n")
    
    while True:
        try:
            menu = int(input("How would you like to proceed:  "))
            if menu == 1:
                filePath = os.chdir(os.path.join(path, 'gif'))
            elif menu ==2:
                filePath = os.chdir(os.path.join(path, 'jpg'))
            elif menu == 3:
                filePath = os.chdir(os.path.join(path, 'pdf'))
            elif menu == 4:
                filePath = os.chdir(os.path.join(path, 'png'))
            else:
                print("Please enter a number 1 - 4.")
                menu = int(input("How would you like to proceed:  "))
            break
        except ValueError:
            print("Please enter a number 1 - 4.")
    



    file = input("Enter the name of the file you want to hash:\n")
    md5_hash = hashlib.md5()
    with open(file, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            md5_hash.update(buf)
            buf = afile.read(BLOCKSIZE)
    hashVal = md5_hash.hexdigest()
    print("The hash value of your file is: " + hashVal)

#Output basic file info



pngcarve()
os.chdir(path)
jpgcarve()
os.chdir(path)
pdfcarve()
os.chdir(path)
gifcarve()
fileHash()
