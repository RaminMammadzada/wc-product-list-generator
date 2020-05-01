# creating empty object and filling them with informations
from Image import Image
from Product import Product


def createObjectsAndFillThem(imageFilenameList):
    # create Products iteratively
    products = [Product(0) for n in range( int(len(imageFilenameList)/7) ) ]
    images = [Image("sampleImageName") for m in range( len(imageFilenameList) ) ]

    # assigning empty image objects (images) to products
    imageIndex = 0
    for product in products:
        for index in range(7):
            product.addImageObject(images[imageIndex + index])
            # isim = product.images[index]
            # print(isim.name)
        imageIndex += 7

    # seperating image file names to images in each product, 7 images to each product
    imageIndex = 0
    for product in products:
        for index in range(7):

            product.setImageName(index, imageFilenameList[imageIndex + index])
            #print(product.images[index])
        imageIndex += 7

        # print("basla")
        # for image in product.images:
        #     print(image.getName())
        # print("bit")


    # # fill product objects with the variables objects
    # variables = [Variable("sampleVariableName") for k in range(2)]
    # for product in products:
    #     product.addVariablebject(variables[0])
    #     product.variables[0].setName("color")
    #     product.addVariablebject(variables[1])
    #     product.variables[1].setName("size")


    # fill product object with the informations taken from image filenames
    for product in products:

        try:
            factory, index = extraxtFactoryCode(product.images[0].getName())
            index += 1

            nameWithoutFactorycode = product.images[0].getName()[index:]
            lisOfElementsInName = nameWithoutFactorycode.split('-')
            designedYear = lisOfElementsInName[0][:2]
            season = lisOfElementsInName[0][2:4]
            style = lisOfElementsInName[0][4]
            rubberType = lisOfElementsInName[0][5]
            modelID = lisOfElementsInName[0][6:]
            color = lisOfElementsInName[1]
            # print("Factory: ", factory)
            # print("Year: ", designedYear)
            # print("Season: ", season)
            # print("Style: ", style)
            # print("Rubber Type", rubberType)
            # print("Model ID: ", modelID)
            # print("Color: ", color)

            nameOflastImageOfTheProduct = product.images[6].getName()[index:]
            lisOfElementsInName = nameOflastImageOfTheProduct.split('-')
            price = lisOfElementsInName[3]
            stockID = lisOfElementsInName[4]
            sizes = lisOfElementsInName[5:]
            # print("Price: ", price)
            # print("Stock ID: ", stockID)
            # print("Sizes: ", sizes)
            # print("- - - - -")
            product.setFactory(factory)
            product.setDesignedYear(designedYear)
            product.setSeason(season)
            product.setStyle(style)
            product.setRubberType(rubberType)
            product.setModelID(modelID)
            product.setPrice(price)
            product.setStockID(stockID)
            product.setColor(color)
            product.setSizes(sizes)
        except:
            print("<<<<<< ASAGIDAKI ISIMLENDIRME HATALI >>>>>>")
            print("_________________________________________")
            print(product.images[0].getName()[:])
            print("_________________________________________")
            print("<<<<<< YUKARIDAKI ISIMLENDIRME HATALI >>>>>>")

    if( validateStockIDs(products) ): print("::: All SKU codes are validated. :::")
    print("- - - - - - - -")
    if( validatSizes(products) ): print("::: ALL PRODUCT SIZES ARE VERIFIED. :::")
    print("- - - - - - - -")

    return products

# def totalNumberOfNonzeroElements( list ):
#     counter = 0
#     for element in list:
#         if(int(element) != 0):
#             counter += 1
#     return counter


def unique(list1):
    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)

    return unique_list

def extraxtFactoryCode(string):
    index = 0
    totalNumberOfDash = 0
    for character in string:
        if(character == "-"):
            totalNumberOfDash += 1
        if(totalNumberOfDash == 2):
            return string[:index], index

        index += 1

# returns true: if it is all validated
# throw exception when there is duplicated Stock IDs inside products
def validateStockIDs(products):
    print("::: SKU VALIDATION STARTED ::: ")
    seenStockIDSet = set()
    index = 1 # this is for debugging purpose
    numberOfDuplicates = 0
    for product in products:
        currentStockID = product.getStockID()
        if(currentStockID in seenStockIDSet):
            print(" " + str(index) + ") " + product.images[6].getName()[:] + "  >>> Change SKU Number !!!")
            numberOfDuplicates += 1
        else:
            seenStockIDSet.add(currentStockID)
            print(" " + str(index) + ") " + product.images[6].getName()[:])
        index += 1 # this is for debugging purpose

    if(numberOfDuplicates > 0):
        raise Exception('CHECK THE PRINTED LINES ABOVE, AND CHANGE THE SKU NUMBERS WHICH ARE DUPLICATED. THERE NUMBER OF DUPLICATED: {}'.format(numberOfDuplicates))
    return True

def validatSizes(products):
    print("::: ALL SIZES VALIDATION STARTED ::: ")
    index = 1
    numberOfWrongSizes = 0
    isThisProductChecked = False
    for product in products:
        isThisProductChecked = False
        for amountOfSize in product.getSizes():
            try:
                stock = int(amountOfSize)
            except ValueError:
                if(not isThisProductChecked):
                    numberOfWrongSizes += 1
                    isThisProductChecked = True
                    print("CORRECTION IS NEEDED IN THE PRODUCT IN THE LINE " + str(index) + ") ")
        index += 1

    if (numberOfWrongSizes > 0):
        raise Exception(
            'CHECK THE PRINTED LINES ABOVE, AND CHANGE THE SIZES WHICH ARE NOT WRITTEN COREECTLY. TOTALLY {} PRODUCT SIZES NEEDED TO CHANGE! '.format(
                numberOfWrongSizes))

    return True