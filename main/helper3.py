# this is an extra function to write filename
# s into the "resultsx.txt" file
from helper1 import retrieveImageFilenameList

def writeFilenamesToTxt(pathInPC, filenameTxtFile):
    imageFilenameList = retrieveImageFilenameList(pathInPC)
    f = open(filenameTxtFile, "w", encoding="utf-8")
    for ele in imageFilenameList:
        f.write(ele + '\n')
    f.close()


# this is extra function to get image filenames from extra txt file
def getImageFilenameListFromTxt(filenameTxtFile):
    data = []
    file1 = open(filenameTxtFile, 'r')
    Lines = file1.readlines()

    # Strips the newline character
    for line in Lines:
        data.append(line.strip())
    return data