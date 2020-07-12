import hashlib
import os
import earthpy as et
import re
from PIL import Image

# OS agnostic creation of a folder for project 2, along with subdirectories for each file type
if not os.path.exists(os.path.join(et.io.HOME, "LED Zeppelin", "Project 2")):
    path = os.path.join(et.io.HOME, "LED Zeppelin", "Project 2")
    os.makedirs(path)
    for subfolder in ['png', 'jpg', 'pdf', 'gif', 'docx']:
        os.makedirs(os.path.join(path, subfolder))
    print("/LED Zeppelin/Project 2 and subfolders have been created")
else:
    path = os.path.join(et.io.HOME, "LED Zeppelin", "Project 2")
    print(path + ' already exists')
os.chdir(path)
print("Please enter your binary file into the new directory: " + path)

# Accept binary file
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
    b = 0

    while True:

        while SOFList[b] > EOFList[i]:
            i += 1

        while EOFList[i] < EOFList[- 1]:
            subdata = data[SOFList[b]:EOFList[i] + 8]
            if SOFList[b] < EOFList[i]:
                carve_filename = "LEDZ" + str(SOFList[b]) + "_" + str(EOFList[i] + 8) + ".png"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "PNG")
                    fileBasics("PNG", carve_filename, SOFList[b], EOFList[i]+8)
                    #print("Found an image and carving it to " + carve_filename)
                    i += 1

        else:
            subdata = data[SOFList[b]:EOFList[i] + 8]
            if EOFList[i] == EOFList[-1]:
                carve_filename = "LEDZ" + str(SOFList[b]) + "_" + str(EOFList[i] + 2) + ".png"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "PNG")
                    fileBasics("PNG", carve_filename, SOFList[b], EOFList[i]+8)
                    #print("Found an image and carving it to " + carve_filename)
                    if SOFList[b] == SOFList[-1]:
                        break
                    else:
                        i = 0
                        b += 1
            elif len(EOFList) == 1:
                break


def jpgcarve():
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

        while SOFList[b] > EOFList[i]:
            i += 1

        while EOFList[i] < EOFList[- 1]:
            subdata = data[SOFList[b]:EOFList[i] + 2]
            if SOFList[b] < EOFList[i]:
                carve_filename = "LEDZ" + str(SOFList[b]) + "_" + str(EOFList[i] + 2) + ".jpg"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "JPG")
                    fileBasics("JPG", carve_filename, SOFList[b], EOFList[i]+2)
                    #print("Found an image and carving it to " + carve_filename)
                    i += 1

        else:
            subdata = data[SOFList[b]:EOFList[i] + 2]
            if EOFList[i] == EOFList[-1]:
                carve_filename = "LEDZ" + str(SOFList[b]) + "_" + str(EOFList[i] + 2) + ".jpg"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "JPG")
                    fileBasics("JPG", carve_filename, SOFList[b], EOFList[i]+2)
                    #print("Found an image and carving it to " + carve_filename)
                    if SOFList[b] == SOFList[-1]:
                        break
                    else:
                        i = 0
                        b += 1
            elif len(EOFList) == 1:
                break


def pdfcarve():
    SOF = b"\x25\x50\x44\x46"
    EOF = b"\x0A\x25\x25\x45\x4F\x46"
    cwd = os.chdir(os.path.join(path, 'pdf'))

    SOFList = [match.start() for match in re.finditer(re.escape(SOF), data)]
    EOFList = [match.start() for match in re.finditer(re.escape(EOF), data)]

    print(SOFList)
    print(EOFList)

    i = 0
    b = 0

    while True:

        while SOFList[b] > EOFList[i]:
            i += 1

        while EOFList[i] < EOFList[- 1]:
            subdata = data[SOFList[b]:EOFList[i] + 6]
            if SOFList[b] < EOFList[i]:
                carve_filename = "LEDZ" + str(SOFList[b]) + "_" + str(EOFList[i] + 6) + ".pdf"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "PDF")
                    fileBasics("PDF", carve_filename, SOFList[b], EOFList[i]+6)
                    #print("Found an image and carving it to " + carve_filename)
                    i += 1

        else:
            subdata = data[SOFList[b]:EOFList[i] + 6]
            if EOFList[i] == EOFList[-1]:
                carve_filename = "LEDZ" + str(SOFList[b]) + "_" + str(EOFList[i] + 6) + ".pdf"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "PDF")
                    fileBasics("PDF", carve_filename, SOFList[b], EOFList[i]+6)
                    #print("Found an image and carving it to " + carve_filename)
                    if SOFList[b] == SOFList[-1]:
                        break
                    else:
                        i = 0
                        b += 1
            elif len(EOFList) == 1:
                break


def gifcarve():
    SOF = b"\x47\x49\x46\x38"
    EOF = b"\x00\x3B"
    cwd = os.chdir(os.path.join(path, 'gif'))

    SOFList = [match.start() for match in re.finditer(re.escape(SOF), data)]
    EOFList = [match.start() for match in re.finditer(re.escape(EOF), data)]

    print(SOFList)
    print(EOFList)

    i = 0
    b = 0

    while True:

        while SOFList[b] > EOFList[i]:
            i += 1

        while EOFList[i] < EOFList[- 1]:
            subdata = data[SOFList[b]:EOFList[i] + 2]
            if SOFList[b] < EOFList[i]:
                carve_filename = "LEDZ" + str(SOFList[b]) + "_" + str(EOFList[i] + 2) + ".gif"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "GIF")
                    fileBasics("GIF", carve_filename, SOFList[b], EOFList[i]+2)
                    #print("Found an image and carving it to " + carve_filename)
                    i += 1

        else:
            subdata = data[SOFList[b]:EOFList[i] + 2]
            if EOFList[i] == EOFList[-1]:
                carve_filename = "LEDZ" + str(SOFList[b]) + "_" + str(EOFList[i] + 2) + ".gif"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "GIF")
                    fileBasics("GIF", carve_filename, SOFList[b], EOFList[i]+2)
                    #print("Found an image and carving it to " + carve_filename)
                    if SOFList[b] == SOFList[-1]:
                        break
                    else:
                        i = 0
                        b += 1
            elif len(EOFList) == 1:
                break



def docxcarve():
    SOF = b"\x50\x4B\x03\x04\x14\x00\x06\x00"
    EOF = b"\x50\x4B\x05\x06"
    cwd = os.chdir(os.path.join(path, 'docx'))

    SOFList = [match.start() for match in re.finditer(re.escape(SOF), data)]
    EOFList = [match.start() for match in re.finditer(re.escape(EOF), data)]

    print(SOFList)
    print(EOFList)

    i = 0
    b = 0

    while True:

        while SOFList[b] > EOFList[i]:
            i += 1

        while EOFList[i] < EOFList[- 1]:
            subdata = data[SOFList[b]:EOFList[i] + 22]
            if SOFList[b] < EOFList[i]:
                carve_filename = "LEDZ" + str(SOFList[b]) + "_" + str(EOFList[i] + 22) + ".docx"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "DOCX")
                    fileBasics("DOCX", carve_filename, SOFList[b], EOFList[i]+22)
                    #print("Found an image and carving it to " + carve_filename)
                    i += 1

        else:
            subdata = data[SOFList[b]:EOFList[i] + 22]
            if EOFList[i] == EOFList[-1]:
                carve_filename = "LEDZ" + str(SOFList[b]) + "_" + str(EOFList[i] + 22) + ".docx"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "DOCX")
                    fileBasics("DOCX", carve_filename, SOFList[b], EOFList[i]+22)
                    #print("Found an image and carving it to " + carve_filename)
                    if SOFList[b] == SOFList[-1]:
                        break
                    else:
                        i = 0
                        b += 1
            elif len(EOFList) == 1:
                break


# Write MD5 hash of carved file
def fileHash(fileName, fileType):
    BLOCKSIZE = 65536
    file = fileName
    md5_hash = hashlib.md5()
    with open(file, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            md5_hash.update(buf)
            buf = afile.read(BLOCKSIZE)
    hashVal = md5_hash.hexdigest()
    fName = fileType + " hashes.txt"
    file = open(fName, 'a+')
    file.write(fileName + " has a hash value of " + hashVal + "\n")
    file.close()

# Output basic file info
def fileBasics(fileType, fileName, startOfFile, endOfFile):
    fType = fileType
    fName = fileName
    bof = startOfFile
    eof = endOfFile
    size = int(eof - bof)
    print("File Information")
    print("------------------------------------------------------------------")
    print("Found a file of type " + fType + " and carving it to " + fName)
    print("The file has an offset of " + str(bof)+ " and a size of " + str(size))
    print(" ")

jpgcarve()
os.chdir(path)
pdfcarve()
os.chdir(path)
gifcarve()
os.chdir(path)
docxcarve()
os.chdir(path)
pngcarve()
