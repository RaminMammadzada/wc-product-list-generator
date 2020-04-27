# this is helper for extracting image filenames as a list and sort them
import glob

def bubblesort(list):
# Swap the elements to arrange in order
	for iter_num in range(len(list)-1,0,-1):
		for idx in range(iter_num):
			last4Numberv1 = list[idx]
			v1 = last4Numberv1[10:17]
			last4Numberv2 = list[idx+1]
			v2 = last4Numberv2[10:17]
			if v1>v2:
				temp = list[idx]
				list[idx] = list[idx+1]
				list[idx+1] = temp
	return list


def filebrowser(filename):
	return [f for f in glob.glob(filename)]


# this function stays for the purpose of debug
def printImageNamesInList(imageNameList):
	for imageName in imageNameList:
		print(imageName)


def readImageNamesInPath(path):
	print("Reading image names from the file ...")
	imageNameList = filebrowser(path)
	#printImageNamesInList(imageNameList)
	return imageNameList


def extractImageNames(rawImageNameList, pathInPC):
	imageNameStartingPoint = len(pathInPC) - 1
	print("Extracting pure image names from the raw image names list...")
	pureImageNameList = []
	for imageName in rawImageNameList:
		pureImageNameList.append(imageName[imageNameStartingPoint:-4])
	return pureImageNameList

def sortImageListByTheSKUNumber(unsortedImageNameList):
	sortedList = bubblesort(unsortedImageNameList)
	return sortedList


def retrieveImageFilenameList(pathInPC):
    imageFilenameList = readImageNamesInPath(pathInPC)
    imageFilenameList = extractImageNames(imageFilenameList, pathInPC)
    return sortImageListByTheSKUNumber(imageFilenameList)
