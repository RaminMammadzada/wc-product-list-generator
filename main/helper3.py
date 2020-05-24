from helper1 import retrieveImageFilenameList
import json

# this is an extra function to write filename
# s into the "resultsx.txt" file
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


# create json for Swatches Attributes
def createSwatchAttributesJson(sizes):
    answerJson = {}
    answerJson["Numara"] = {}
    answerJson["Numara"]["name"] = "Numara"
    answerJson["Numara"]["type"] = "label"
    answerJson["Numara"]["terms"] = {}

    for size in sizes:
        answerJson["Numara"]["terms"][str(size)] = {}
        answerJson["Numara"]["terms"][str(size)]["name"] = str(size)
        answerJson["Numara"]["terms"][str(size)]["color"] = ""
        answerJson["Numara"]["terms"][str(size)]["image"] = ""
        answerJson["Numara"]["terms"][str(size)]["show_tooltip"] = ""
        answerJson["Numara"]["terms"][str(size)]["tooltip_text"] = ""
        answerJson["Numara"]["terms"][str(size)]["tooltip_image"] = ""
        answerJson["Numara"]["terms"][str(size)]["image_size"] = ""

    json_data = json.dumps(answerJson)
    return json_data
