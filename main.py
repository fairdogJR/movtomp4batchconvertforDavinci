
# tim fairfield Eula License free to use for your non commercial projects
# code to batch convert mov to mp4 for Davinci when using iphone 13 footage
# Aug 3 2022

import os


def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()

def read_list(filename):
    # Using readlines()
    file1 = open(filename, 'r')
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        print("file {}: {}".format(count, line.strip()))

def process_list(filename):
    # Using readlines()
    file1 = open(filename, 'r')
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        count += 1
        infile=line.strip();
        outfile=os.path.splitext(infile)[0]+'.mp4'
        convertthem = 'HandBrakeCLI -e x264 -q 20.0 --input '+infile +' --output ' +outfile +''
        print (convertthem)


        os.system(convertthem)


# Driver's code
# Printing CWD before
current_path()

path=r'D:\documents m2\video projects\davinci projects\tdr-walkthrough\calibration raw content'

# Changing the CWD
os.chdir(path)
current_path()

filelistname='filelist.txt'
create_filelist='dir /b *.mov>'+filelistname
runprocess1='HandBrakeCLI -e x264 -q 20.0 --input IMG_3331.MOV --output IMG_3331.mp4'

os.system(create_filelist)
read_list(filelistname)

process_list(filelistname)



