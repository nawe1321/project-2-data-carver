import hashlib
import os
import earthpy as et
import re
from PIL import Image
import argparse
import datetime

# Variables
timestamp = str(datetime.datetime.now().strftime("%Y%m%dT%H%M%S"))
current_dir = str(os.getcwd())
project_dir = str("LED-Zeppelin_Project-2_" + timestamp)


# Parser to accept command-line arguments
parser = argparse.ArgumentParser(description='Carving Evidence from a Binary File')


# Create list of agruments
parser.add_argument(    dest='filename',
                        type = argparse.FileType('rb'),
                        help ='The binary filename to be carved located in the current working directory.')


# Parse Arguments
args = parser.parse_args()


# Open/Read/Close Binary File as Read-Only
with open(args.filename.name, 'rb') as file_obj:
    data = file_obj.read()


# OS agnostic creation of a folder for project 2, along with subdirectories for each file type
if not os.path.exists(os.path.join(current_dir, project_dir)):
    path = os.path.join(current_dir, project_dir)
    os.makedirs(path)
    for subfolder in ['png', 'jpg', 'pdf', 'gif', 'docx']:
        os.makedirs(os.path.join(path, subfolder))
    print(project_dir + " and subfolders have been created!")
else:
    path = os.path.join(current_dir, project_dir)
    print(path + ' already exists')
    os.chdir(path)
    print("Please enter your binary file into the new directory: " + path)


def pngcarve():
    SOF = b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a"
    EOF = b"\x49\x45\x4e\x44\xae\x42\x60\x82"
    cwd = os.chdir(os.path.join(path, 'png'))

    SOFList = [match.start() for match in re.finditer(re.escape(SOF), data)]
    EOFList = [match.start() for match in re.finditer(re.escape(EOF), data)]

    #print(SOFList)
    #print(EOFList)

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

    #print(SOFList)
    #print(EOFList)

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

    #print(SOFList)
    #print(EOFList)

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

    #print(SOFList)
    #print(EOFList)

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

    #print(SOFList)
    #print(EOFList)

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


# MD5 hash of carved file coded by Bobbie
#Used Python API for hashing large file types
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

# Output basic file coded by Bobbie
def fileBasics(fileType, fileName, startOfFile, endOfFile):
    fType = fileType
    fName = fileName
    bof = startOfFile
    eof = endOfFile
    size = int(eof - bof)
    offSet = hex(bof) #Converts the offset to Hex

    #Writes the file data to the screen
    print("File Information")
    print("------------------------------------------------------------------")
    print("Found a file of type " + fType + " and carving it to " + fName)
    print("The file has an offset of " + str(offSet)+ " and a size of " + str(size))
    print(" ")

    #Writes the file data to a file in case it needs to be looked at later on
    file = open('File Information.txt', 'a+')
    file.write(fileName + " Information \n")
    file.write("--------------------------------------------------------\n")
    file.write("This file is type: " + fType +"\n")
    file.write("The offset of this file is: " + str(offSet) +"\n")
    file.write("The size of the file is: " + str(size) + "\n\n")
    file.close()

#Run the program
jpgcarve()
os.chdir(path)
pdfcarve()
os.chdir(path)
gifcarve()
os.chdir(path)
docxcarve()
os.chdir(path)
pngcarve()
