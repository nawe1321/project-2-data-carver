import argparse
import datetime
import hashlib
import os
import re
import sys

# ---
# Variables
#
timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d-Time-%H-%M.%S"))
current_dir = str(os.getcwd())
project_dir = str("LED-Zeppelin_Project-2_" + timestamp)

# ---
# Pre-Checks for Argparse - Coded by Preston
#
if len(sys.argv) < 2:
    print(
        "Invalid or missing filename.  Insert a binary filename to be carved.  Enter the -h flag for more information.")
    sys.exit()

if len(sys.argv) > 4:
    print("Too many arguments.  Enter the -h flag for more information.")
    sys.exit()

# ---
# Parser to accept command-line arguments - Coded by Preston/Nathan
#
parser = argparse.ArgumentParser(description='Carving Evidence from a Binary File')
grouptype = parser.add_mutually_exclusive_group(required=True)
####### group carve coming soon: standard will create less false postives, but will also be less successful finding embedded files.
####### brute force is the default and what is currently being implemented.  It will find more files, but will take up more disk space as well.
#groupcarve = parser.add_mutually_exclusive_group(required=False)

# ---
# Create list of arguments - Coded by Preston/Nathan
#
parser.add_argument(dest='filename',
                    type=argparse.FileType('rb'),
                    help='The binary filename to be carved located in the current working directory.')
grouptype.add_argument('-m', '--media', dest='media', action='store_true',
                       help='Search the binary file for media only')
grouptype.add_argument('-d', '--docs', '--documents', dest='docs', action='store_true',
                       help='Search the binary file for documents only')
grouptype.add_argument('-a', '--all', dest='all', action='store_true', help='Search the binary file for all file types')
"""
groupcarve.add_argument('-s', '--standard', dest='standard', action='store_true', default=False,
                        help='Search the binary file for images only')
groupcarve.add_argument('-b', '--brute force', dest='brute_force', action='store_true', default=True,
                        help='Search the binary file for images only')
"""
args = parser.parse_args()

# ---
# Open/Read/Close Binary File as Read-Only - Coded by Preston
#
with open(args.filename.name, 'rb') as file_obj:
    data = file_obj.read()


# ---
# Menu Function - Coded by Preston
# 
def menu():
    # Carves Media File Types (JPG, GIF, PNG, and MP4)
    if args.media == True:
        createdirectories("jpg gif png mp4")
        jpgcarve()
        os.chdir(path)
        gifcarve()
        os.chdir(path)
        pngcarve()
        os.chdir(path)
        mp4carve()

    # Carves Document File Types (PDF and DOCX)
    elif args.docs == True:
        createdirectories("pdf docx")
        pdfcarve()
        os.chdir(path)
        docxcarve()



    # Carves All File Types (JPG, PDF, GIF, DOCX, PNG, and MP4)
    elif args.all == True:
        createdirectories("jpg pdf gif docx png mp4")
        jpgcarve()
        os.chdir(path)
        pdfcarve()
        os.chdir(path)
        gifcarve()
        os.chdir(path)
        docxcarve()
        os.chdir(path)
        pngcarve()
        os.chdir(path)
        mp4carve()

    # Carves All File Types (JPG, PDF, GIF, DOCX, PNG, and MP4)
    else:
        createdirectories("jpg pdf gif docx png mp4")
        jpgcarve()
        os.chdir(path)
        pdfcarve()
        os.chdir(path)
        gifcarve()
        os.chdir(path)
        docxcarve()
        os.chdir(path)
        pngcarve()
        os.chdir(path)
        mp4carve()


# ---
# Directory Creation Function - Coded by Nathan/Preston
# OS agnostic creation of a folder for project 2, along with subdirectories for each file type
#
def createdirectories(carved_types):
    global path
    subfolders = carved_types.split()

    if not os.path.exists(os.path.join(current_dir, project_dir)):
        path = os.path.join(current_dir, project_dir)
        os.makedirs(path)
        for subfolder in subfolders:
            os.makedirs(os.path.join(path, subfolder))
        print(project_dir + " and subfolders have been created!")
    else:
        path = os.path.join(current_dir, project_dir)
        print(path + ' already exists')
        os.chdir(path)
        print("Please enter your binary file into the new directory: " + path)


# ---
# PNG Carving Function - Coded by Nathan
#
def pngcarve():
    global path
    SOF = b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a"
    EOF = b"\x49\x45\x4e\x44\xae\x42\x60\x82"
    cwd = os.chdir(os.path.join(path, 'png'))

    SOFList = [match.start() for match in re.finditer(re.escape(SOF), data)]
    EOFList = [match.start() for match in re.finditer(re.escape(EOF), data)]
    
    #Error check for list, if nothing in list exits to the next function - Coded by Bobbie
    if len(SOFList) == 0 or len(EOFList) == 0:
        return

    # print(SOFList)
    # print(EOFList)

    i = 0
    b = 0

    while True:

        while SOFList[b] > EOFList[i]:
            i += 1

        while EOFList[i] < EOFList[- 1]:
            subdata = data[SOFList[b]:EOFList[i] + 8]
            if SOFList[b] < EOFList[i]:
                carve_filename = "LEDZ: " + str(SOFList[b]) + "-" + str(EOFList[i] + 8) + ".png"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "PNG")
                    fileBasics("PNG", carve_filename, SOFList[b], EOFList[i] + 8)
                    # print("Found an image and carving it to " + carve_filename)
                    i += 1

        else:
            subdata = data[SOFList[b]:EOFList[i] + 8]
            if EOFList[i] == EOFList[-1]:
                carve_filename = "LEDZ: " + str(SOFList[b]) + "-" + str(EOFList[i] + 8) + ".png"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "PNG")
                    fileBasics("PNG", carve_filename, SOFList[b], EOFList[i] + 8)
                    # print("Found an image and carving it to " + carve_filename)
                    if SOFList[b] == SOFList[-1]:
                        break
                    else:
                        i = 0
                        b += 1
            elif len(EOFList) == 1:
                break


# ---
# JPG Carving Function - Coded by Nathan
#
def jpgcarve():
    global path
    SOF = b"\xFF\xD8\xFF"
    EOF = b"\xFF\xD9"
    cwd = os.chdir(os.path.join(path, 'jpg'))

    SOFList = [match.start() for match in re.finditer(re.escape(SOF), data)]
    EOFList = [match.start() for match in re.finditer(re.escape(EOF), data)]
    
    #Error check for list, if nothing in list exits to the next function - Coded by Bobbie
    if len(SOFList) == 0 or len(EOFList) == 0:
        return

    # print(SOFList)
    # print(EOFList)

    i = 0
    b = 0

    while True:

        while SOFList[b] > EOFList[i]:
            i += 1

        while EOFList[i] < EOFList[- 1]:
            subdata = data[SOFList[b]:EOFList[i] + 2]
            if SOFList[b] < EOFList[i]:
                carve_filename = "LEDZ: " + str(SOFList[b]) + "-" + str(EOFList[i] + 2) + ".jpg"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "JPG")
                    fileBasics("JPG", carve_filename, SOFList[b], EOFList[i] + 2)
                    # print("Found an image and carving it to " + carve_filename)
                    i += 1

        else:
            subdata = data[SOFList[b]:EOFList[i] + 2]
            if EOFList[i] == EOFList[-1]:
                carve_filename = "LEDZ: " + str(SOFList[b]) + "-" + str(EOFList[i] + 2) + ".jpg"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "JPG")
                    fileBasics("JPG", carve_filename, SOFList[b], EOFList[i] + 2)
                    # print("Found an image and carving it to " + carve_filename)
                    if SOFList[b] == SOFList[-1]:
                        break
                    else:
                        i = 0
                        b += 1
            elif len(EOFList) == 1:
                break


# ---
# PDF Carving Function - Coded by Nathan
def pdfcarve():
    global path
    SOF = b"\x25\x50\x44\x46"
    EOF = b"\x0A\x25\x25\x45\x4F\x46"
    cwd = os.chdir(os.path.join(path, 'pdf'))

    SOFList = [match.start() for match in re.finditer(re.escape(SOF), data)]
    EOFList = [match.start() for match in re.finditer(re.escape(EOF), data)]
    
    #Error check for list, if nothing in list exits to the next function - Coded by Bobbie
    if len(SOFList) == 0 or len(EOFList) == 0:
        exit()

    # print(SOFList)
    # print(EOFList)

    i = 0
    b = 0

    while True:

        while SOFList[b] > EOFList[i]:
            i += 1

        while EOFList[i] < EOFList[- 1]:
            subdata = data[SOFList[b]:EOFList[i] + 6]
            if SOFList[b] < EOFList[i]:
                carve_filename = "LEDZ: " + str(SOFList[b]) + "-" + str(EOFList[i] + 6) + ".pdf"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "PDF")
                    fileBasics("PDF", carve_filename, SOFList[b], EOFList[i] + 6)
                    # print("Found a document and carving it to " + carve_filename)
                    i += 1

        else:
            subdata = data[SOFList[b]:EOFList[i] + 6]
            if EOFList[i] == EOFList[-1]:
                carve_filename = "LEDZ: " + str(SOFList[b]) + "-" + str(EOFList[i] + 6) + ".pdf"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "PDF")
                    fileBasics("PDF", carve_filename, SOFList[b], EOFList[i] + 6)
                    # print("Found a document and carving it to " + carve_filename)
                    if SOFList[b] == SOFList[-1]:
                        break
                    else:
                        i = 0
                        b += 1
            elif len(EOFList) == 1:
                break


# ---
# GIF Carving Function - Coded by Nathan
#
def gifcarve():
    global path
    SOF = b"\x47\x49\x46\x38"
    EOF = b"\x00\x3B"
    cwd = os.chdir(os.path.join(path, 'gif'))

    SOFList = [match.start() for match in re.finditer(re.escape(SOF), data)]
    EOFList = [match.start() for match in re.finditer(re.escape(EOF), data)]
    
    #Error check for list, if nothing in list exits to the next function - Coded by Bobbie
    if len(SOFList) == 0 or len(EOFList) == 0:
        return

    # print(SOFList)
    # print(EOFList)

    i = 0
    b = 0

    while True:

        while SOFList[b] > EOFList[i]:
            i += 1

        while EOFList[i] < EOFList[- 1]:
            subdata = data[SOFList[b]:EOFList[i] + 2]
            if SOFList[b] < EOFList[i]:
                carve_filename = "LEDZ: " + str(SOFList[b]) + "-" + str(EOFList[i] + 2) + ".gif"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "GIF")
                    fileBasics("GIF", carve_filename, SOFList[b], EOFList[i] + 2)
                    # print("Found an image and carving it to " + carve_filename)
                    i += 1

        else:
            subdata = data[SOFList[b]:EOFList[i] + 2]
            if EOFList[i] == EOFList[-1]:
                carve_filename = "LEDZ: " + str(SOFList[b]) + "-" + str(EOFList[i] + 2) + ".gif"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "GIF")
                    fileBasics("GIF", carve_filename, SOFList[b], EOFList[i] + 2)
                    # print("Found an image and carving it to " + carve_filename)
                    if SOFList[b] == SOFList[-1]:
                        break
                    else:
                        i = 0
                        b += 1
            elif len(EOFList) == 1:
                break


# ---
# DOCX Carving Function - Coded by Nathan
#
def docxcarve():
    global path
    SOF = b"\x50\x4B\x03\x04\x14\x00\x06\x00"
    EOF = b"\x50\x4B\x05\x06"
    cwd = os.chdir(os.path.join(path, 'docx'))

    SOFList = [match.start() for match in re.finditer(re.escape(SOF), data)]
    EOFList = [match.start() for match in re.finditer(re.escape(EOF), data)]
    
    #Error check for list, if nothing in list exits to the next function - Coded by Bobbie
    if len(SOFList) == 0 or len(EOFList) == 0:
        return

    # print(SOFList)
    # print(EOFList)

    i = 0
    b = 0

    while True:

        while SOFList[b] > EOFList[i]:
            i += 1

        while EOFList[i] < EOFList[- 1]:
            subdata = data[SOFList[b]:EOFList[i] + 22]
            if SOFList[b] < EOFList[i]:
                carve_filename = "LEDZ: " + str(SOFList[b]) + "-" + str(EOFList[i] + 22) + ".docx"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "DOCX")
                    fileBasics("DOCX", carve_filename, SOFList[b], EOFList[i] + 22)
                    # print("Found a document and carving it to " + carve_filename)
                    i += 1

        else:
            subdata = data[SOFList[b]:EOFList[i] + 22]
            if EOFList[i] == EOFList[-1]:
                carve_filename = "LEDZ: " + str(SOFList[b]) + "-" + str(EOFList[i] + 22) + ".docx"
                with open(carve_filename, 'wb') as carve_obj:
                    carve_obj.write(subdata)
                    carve_obj.close()
                    fileHash(carve_filename, "DOCX")
                    fileBasics("DOCX", carve_filename, SOFList[b], EOFList[i] + 22)
                    # print("Found a document and carving it to " + carve_filename)
                    if SOFList[b] == SOFList[-1]:
                        break
                    else:
                        i = 0
                        b += 1
            elif len(EOFList) == 1:
                break


# ---
# MP4 Carving Function - Coded by Nathan
#
def mp4carve():
    global path
    SOF = b"\x66\x74\x79\x70\x6D\x70\x34\x32"
    EOFList = len(data)
    cwd = os.chdir(os.path.join(path, 'mp4'))

    SOFList = [match.start() for match in re.finditer(re.escape(SOF), data)]
    #EOFList = [match.start() for match in re.finditer(re.escape(EOF), data)]

    # print(SOFList)
    # print(EOFList)

    i = 0
    b = 0
    print(SOFList)
    print(EOFList)


    for SOF in SOFList:
        subdata = data[SOFList[b] - 4:EOFList]
        carve_filename = "LEDZ: " + str(SOFList[b] - 4) + "-" + str(EOFList) + ".mp4"
        with open(carve_filename, 'wb') as carve_obj:
            carve_obj.write(subdata)
            carve_obj.close()
            fileHash(carve_filename, "MP4")
            fileBasics("MP4", carve_filename, SOFList[b] - 4, EOFList)
            # print("Found a video and carving it to " + carve_filename)




# ---
# MD5 hash of carved file - Coded by Bobbie
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


# ---
# Output basic file - Coded by Bobbie
#
def fileBasics(fileType, fileName, startOfFile, endOfFile):
    fType = fileType
    fName = fileName
    bof = startOfFile
    eof = endOfFile
    size = int(eof - bof)
    offSet = hex(bof)  # Converts the offset to Hex

    # Writes the file data to the screen
    print("File Information")
    print("------------------------------------------------------------------")
    print("Found a file of type " + fType + " and carving it to " + fName)
    print("The file has an offset of " + str(offSet) + " and a size of " + str(size))
    print(" ")

    # Writes the file data to a file in case it needs to be looked at later on
    file = open('File Information.txt', 'a+')
    file.write(fileName + " Information \n")
    file.write("--------------------------------------------------------\n")
    file.write("This file is type: " + fType + "\n")
    file.write("The offset of this file is: " + str(offSet) + "\n")
    file.write("The size of the file is: " + str(size) + "\n\n")
    file.close()


# ---
# Print Summary - Coded by Preston
# 
def summary():
    # Variables
    jpgs = pdfs = gifs = docxs = pngs = mp4s = media = documents = total = 0

    # Count Number of Carved Files by Category Type
    for category_dir in os.listdir(path):
        for file_name in os.listdir(os.path.join(path, category_dir)):
            if file_name.endswith(".jpg"):
                jpgs += 1
            elif file_name.endswith(".pdf"):
                pdfs += 1
            elif file_name.endswith(".gif"):
                gifs += 1
            elif file_name.endswith(".docx"):
                docxs += 1
            elif file_name.endswith(".png"):
                pngs += 1
            elif file_name.endswith(".mp4"):
                mp4s += 1

    # Print Summary
    print("==================================================================")
    print("Data Carving Results")
    print("==================================================================\n")

    # Total Media
    if jpgs > 0 or gifs > 0 or pngs > 0 or mp4s > 0:
        images = int(jpgs) + int(gifs) + int(pngs)
        videos = int(mp4s)
        media = images + videos

        print("---------------------------------")
        print('JPG\'s: '+ str(jpgs))
        print('GIF\'s: '+ str(gifs))
        print('PNG\'s: '+ str(pngs))
        print('MP4\'s: '+ str(mp4s))
        print("---------------------------------")
        print('Total Images: '+ str(images) + '\n')
        print('Total Videos: '+ str(videos) + '\n')
        print('Total Media: '+ str(media) + '\n')

    # Total Documents
    if pdfs > 0 or docxs > 0:
        documents = int(pdfs) + int(docxs)

        print("---------------------------------")
        print('PDF\'s: ' + str(pdfs))
        print('DOCX\'s: ' + str(docxs))
        print("---------------------------------")
        print('Total Documents: '+ str(documents) + '\n')

    # Total Files Carved
    total = int(media) + int(documents)

    print("==================================================================")
    print('Total Files Carved: '+ str(total))
    print("==================================================================")


# ---
# Run the program
#
menu()
summary()
