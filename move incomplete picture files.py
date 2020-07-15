import os
from PIL import Image
from os import listdir

current_dir = str(os.getcwd())
project_dir = str("LED-Zeppelin_Project-2_")
if not os.path.exists(os.path.join(current_dir, project_dir)):
    path = os.path.join(current_dir, project_dir)
    os.makedirs(path)
    for subfolder in ['png', 'jpg', 'pdf', 'gif', 'docx']:
        os.makedirs(os.path.join(path, subfolder))
cwd=os.chdir('/Users/nathan/Library/Application Support/JetBrains/PyCharmCE2020.1/scratches/LED-Zeppelin_Project-2_/images/')

cwd=os.getcwd()
src = cwd
dst = os.path.join(cwd, 'fragments_incomplete')

print(dst)
badfiles=[]
extensions=('.gif', '.jpg', '.png')

for filename in listdir(cwd):
  if filename.endswith(extensions):
    try:
      img = Image.open(filename) # open the image file
      img.load() # verify that it is, in fact an image
    except (IOError, SyntaxError) as e:
      badfiles.append(filename)
      # print out the names of corrupt files
print('List of bad images:')
for filename in badfiles:
    print(os.getcwd()+filename) # Print each corrupted file's name with full path
#print('There are,' + len(badfiles) + 'bad images that need to be deleted and replaced.')
print(badfiles)
for filename in badfiles:
    os.replace(os.path.join(src,filename), os.path.join(dst, filename))
