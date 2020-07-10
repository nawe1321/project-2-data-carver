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

    print(SOFList)
    print(EOFList)

    i = 0
    b = 0
    for SOF in SOFList:
        subdata = data[SOF:EOFList[i] + 8]

        while EOFList[i] < EOFList[- 1]:

            if SOFList[b] < EOFList[i]:
                # print(EOFList[i])
                carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 8) + ".png"
                carve_obj = open(carve_filename, 'wb')
                carve_obj.write(subdata)
                carve_obj.close()
                print("Found an image and carving it to " + carve_filename)

            # print(EOFList[i])
            # print("S" + str(SOFList[b]))
            EOFList[i] = EOFList[i + 1]
            i += 1

        while EOFList[i] == EOFList[- 1]:
            carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 8) + ".png"
            carve_obj = open(carve_filename, 'wb')
            carve_obj.write(subdata)
            carve_obj.close()
            print("Found an image and carving it to " + carve_filename)
            # print(i)
            b = b + 1
            i = 0
            if len(EOFList) == 1:
                break
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
    for SOF in SOFList:
        subdata = data[SOF:EOFList[i] + 2]

        while EOFList[i] == EOFList[- 1]:
            carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 2) + ".jpg"
            carve_obj = open(carve_filename, 'wb')
            carve_obj.write(subdata)
            carve_obj.close()
            print("Found an image and carving it to " + carve_filename)
            # print(i)
            b = b + 1
            i = 0
            if len(EOFList) == 1:
                break

        while EOFList[i] < EOFList[- 1]:
            # print(EOFList[i])
            # print("S" + str(SOFList[b]))
            EOFList[i] = EOFList[i + 1]
            i += 1
            if SOFList[b] < EOFList[i]:
                # print(EOFList[i])
                carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 2) + ".jpg"
                carve_obj = open(carve_filename, 'wb')
                carve_obj.write(subdata)
                carve_obj.close()
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
    b = 0
    for SOF in SOFList:
        subdata = data[SOF:EOFList[i] + 6]

        while EOFList[i] == EOFList[- 1]:
            carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 6) + ".pdf"
            carve_obj = open(carve_filename, 'wb')
            carve_obj.write(subdata)
            carve_obj.close()
            print("Found an image and carving it to " + carve_filename)
            # print(i)
            b = b + 1
            i = 0
            if len(EOFList) == 1:
                break

        while EOFList[i] < EOFList[- 1]:
            # print(EOFList[i])
            # print("S" + str(SOFList[b]))
            EOFList[i] = EOFList[i + 1]
            i += 1
            if SOFList[b] < EOFList[i]:
                # print(EOFList[i])
                carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 6) + ".pdf"
                carve_obj = open(carve_filename, 'wb')
                carve_obj.write(subdata)
                carve_obj.close()
                print("Found an image and carving it to " + carve_filename)


def gifcarve():
    SOF = b"\x47\x49\x46\x38"
    EOF = b"\x00\x3B\x2E"
    cwd = os.chdir(os.path.join(path, 'gif'))

    SOFList = [match.start() for match in re.finditer(re.escape(SOF), data)]
    EOFList = [match.start() for match in re.finditer(re.escape(EOF), data)]

    print(SOFList)
    print(EOFList)

    i = 0
    b = 0
    for SOF in SOFList:
        subdata = data[SOF:EOFList[i] + 2]

        while EOFList[i] == EOFList[- 1]:
            carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 2) + ".gif"
            carve_obj = open(carve_filename, 'wb')
            carve_obj.write(subdata)
            carve_obj.close()
            print("Found an image and carving it to " + carve_filename)
            # print(i)
            b = b + 1
            i = 0
            if len(EOFList) == 1:
                break

        while EOFList[i] < EOFList[- 1]:
            # print(EOFList[i])
            # print("S" + str(SOFList[b]))
            EOFList[i] = EOFList[i + 1]
            i += 1
            if SOFList[b] < EOFList[i]:
                # print(EOFList[i])
                carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 2) + ".gif"
                carve_obj = open(carve_filename, 'wb')
                carve_obj.write(subdata)
                carve_obj.close()
                print("Found an image and carving it to " + carve_filename)



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
    for SOF in SOFList:
        subdata = data[SOF:EOFList[i] + 22]

        while EOFList[i] == EOFList[- 1]:
            carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 22) + ".docx"
            carve_obj = open(carve_filename, 'wb')
            carve_obj.write(subdata)
            carve_obj.close()
            print("Found an image and carving it to " + carve_filename)
            # print(i)
            b = b + 1
            i = 0
            if len(EOFList) == 1:
                break

        while EOFList[i] < EOFList[- 1]:
            # print(EOFList[i])
            # print("S" + str(SOFList[b]))
            EOFList[i] = EOFList[i + 1]
            i += 1
            if SOFList[b] < EOFList[i]:
                # print(EOFList[i])
                carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 22) + ".docx"
                carve_obj = open(carve_filename, 'wb')
                carve_obj.write(subdata)
                carve_obj.close()
                print("Found an image and carving it to " + carve_filename)

        while EOFList[i] == EOFList[- 1]:
            carve_filename = "Carve1_" + str(SOF) + "_" + str(EOFList[i] + 22) + ".docx"
            carve_obj = open(carve_filename, 'wb')
            carve_obj.write(subdata)
            carve_obj.close()
            print("Found an image and carving it to " + carve_filename)
            # print(i)
            b = b + 1
            i = 0
            if len(EOFList) == 1:
                break


# Write MD5 hash of carved file


# Output basic file info

#jpgcarve()
#only returns some jpegs, but will return all if the while EOFList[i] == EOFList[-1] is first, but then all files are massive
os.chdir(path)
pdfcarve()
os.chdir(path)
#gifcarve()
#still won't carve the gif and gives a 0 byte file return
os.chdir(path)
docxcarve()
os.chdir(path)
pngcarve()
