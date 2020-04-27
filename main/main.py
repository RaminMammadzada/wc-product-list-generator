from Excell import Excell
from Image import Image
from Model import Model
from Product import Product
from constants import Categories, Tags
from helper1 import *

#pathInPC = "../../../modeller/erkek-2020-yazlik/" + "sultan/*"
#pathInPC = "../../../../../Volumes/G-DRIVE mobile SSD R-Series/Shoes/modeller/erkek-2020-yazlik/depedro/*"
from helper2 import createObjectsAndFillThem, unique

pathInPC = "/Volumes/G-DRIVE mobile SSD R-Series/Shoes/modeller/first-170-pairs-22-march-2020/dorduncu-merhele/*"




#### PRODUCT
modelID = "5234"
stockID = "2222"
# 4-1-20YZCP3425-siyah
# 4-1-20YZCP3425-kahve
# 4-1-20YZCP3425-laci
# 4-1-20YZCP3425-laci-80-222200001
# take images as a bundle of 6 images and check
product1 = Product(stockID)
product1.setModelID(modelID)
print(product1.getStockID())
print(product1.getModelID())
print(" - - - - ")
model1 = Model(modelID)
# resim isimleri tarama, 6 li olarak yigma
# her modelin 6 resmi olacaq sekilde


imageFilenameList = retrieveImageFilenameList(pathInPC)
products = createObjectsAndFillThem(imageFilenameList)

def createAndFillRow(rowNumber, myFile, product, type, isFeatured, description, stock="", categories="", images="", parent="", crossSellProducts="", color="", size=""):
    value = ""

    myFile.setType(rowNumber, type)

    #print("Size:  > " + size)
    #print("Color: >" + color)
    if(size != "" and color != ""):
        #print("burada")
        stockCode = product.getStockID() + size + str(ord(color[0]))
    else:
        stockCode = product.getStockID()

    myFile.setSKU(rowNumber, stockCode)
    myFile.setName(rowNumber, Tags["factory"][product.getFactory()] + " " + Categories["style"][product.getStyle()] )
    myFile.setPublished(rowNumber, "1")

    myFile.setIsFeatured(rowNumber, isFeatured)
    myFile.setVisibilityInCatalog(rowNumber, "visible")
    myFile.setShortSescription(rowNumber, "Model no: " + product.factory + " " + product.getModelID() )
    myFile.setDescription(rowNumber, description)
    myFile.setDateSalePriceStarts(rowNumber, "")
    myFile.setDateSalePriceEnds(rowNumber, "")
    myFile.setTaxClass(rowNumber, "taxable")
    myFile.setInStock(rowNumber, "1")
    myFile.setStock(rowNumber, stock )
    myFile.setBackordersAllowed(rowNumber, "0")
    myFile.setSoldIndividually(rowNumber, "0")
    myFile.setWeightInKg(rowNumber, "")
    myFile.setLengthIncm(rowNumber, "")
    myFile.setWidthIncm(rowNumber, "")
    myFile.setHeightIncm(rowNumber, "")
    myFile.setAllowCustomerReviews(rowNumber, "1")
    myFile.setPurchaseNote(rowNumber, "")

    salePrice = product.getPrice() if type == "variation" else ""
    regularPrice = int(salePrice) + 200 if type == "variation" else ""
    myFile.setSalePrice(rowNumber, salePrice)
    myFile.setRegularPrice(rowNumber, regularPrice)
    myFile.setCategories(rowNumber, categories)
    myFile.setTags( rowNumber, "deri, " + Tags["factory"][product.getFactory()] + ", " + Categories["style"][product.getStyle()] + ", " + Categories["rubber"][product.getRubberType()] + ", " + Categories["season"][product.getSeason()] )
    myFile.setShippingClass(rowNumber, "")

    myFile.setImages(rowNumber, images)
    myFile.setDownloadLimit(rowNumber, "")
    myFile.setDownloadExpiryDays(rowNumber, "")
    myFile.setParent(rowNumber, parent)
    myFile.setGroupedProducts(rowNumber, "")
    myFile.setUpsells(rowNumber, "")
    myFile.setCrossSells(rowNumber, crossSellProducts)
    myFile.setExternalURL(rowNumber, "")
    myFile.setButtonText(rowNumber, "")
    myFile.setDownload1Name(rowNumber, "")
    myFile.setDownload1URL(rowNumber, "")

    myFile.setAttribute1Name(rowNumber, "Reng")
    myFile.setAttribute1Values(rowNumber, color)
    myFile.setAttribute1Visible(rowNumber, "1")
    myFile.setAttribute1Global(rowNumber, "1")
    myFile.setAttribute2Name(rowNumber, "Numara")
    myFile.setAttribute2Values(rowNumber, size)
    myFile.setAttribute2Visible(rowNumber, "1")
    myFile.setAttribute2Global(rowNumber, "1")
    myFile.setAttribute1Default(rowNumber, color)
    myFile.setAttribute2Default(rowNumber, size)


# for product in products:
#     print(product)
#     print(product.factory)
#     print(product.price)
#     print(product.modelID)
#     print(product.rubberType)





### EXCEL FILE
# Create Excell Workbook and ExcellSheet
myfile = Excell("ProductsMarch2020")
myfile.createWorkbook()
myfile.createWorksheet()
myfile.setWorksheetHeaders()


# dictionary for controlling the number of the existince of the same product, first we set them all 0, we will change it later
isControlledDict = {}
for product in products:
    isControlledDict[product.getFactory() + "-" + product.getDesignedYear() + product.getModelID()] = 0


rowNumber = 2
isFeatured = 1
description = " Kaliteli Deri Urunleri "
stock = 0
for product in products:

    if (isFeatured == 0):
        isFeatured = 1
    else:
        isFeatured = 0


    categories = Categories["season"][product.getSeason()] + "," + Categories["season"][product.getSeason()] + " > " + Categories["style"][product.getStyle()] + "," + Categories["style"][product.getStyle()] + " > " + Categories["rubber"][product.getRubberType()]

    # loop for collection all images of the product as a string
    images = ""
    for image in product.images:
        if(image != product.images[-1]):
            images += ( image.getName() + ".jpg")

        if(image != product.images[-1] and image != product.images[-2] ):
            images += ", "

    # loop for collection stockIDs for crossSellingProducts
    crossSellProducts = ""
    for pro in products:
        if (pro.getFactory() == product.getFactory()):
            crossSellProducts += pro.getStockID()
            if (pro != products[-1]):
                crossSellProducts += ", "


    # lists to collect all colors of the model
    colors = []
    colors.append(product.getColor())
    #print(colors)

    sizes = []
    index = -1
    for size in product.getSizes():
        if(index == -1): # this is for 39 size check
            if(size != "0"):
                sizes.append("39")
        else:
            if(size != "0"):
                sizes.append("4" + str(index) )
        index += 1
    #print(sizes)


    #print("Color: ", product.getColor())
    #print("Sizes: ", product.getSizes())
    if(isControlledDict[product.getFactory() + "-" + product.getDesignedYear() + product.getModelID()] == 0):

        parent = product.getStockID()
        createAndFillRow(rowNumber, myfile, product, "variable", isFeatured, description,"", categories, images, "", crossSellProducts, "", "")
        tempRowNumberForColorsAndSizes = rowNumber
        rowNumber += 1
        index = -1
        for amountOfSize in product.getSizes():
            stock = int(amountOfSize)
            if (index == -1):
                if (stock != 0):
                    size = "39"
                    createAndFillRow(rowNumber, myfile, product, "variation", isFeatured, description, str(stock), "",
                                     images, parent, crossSellProducts, product.getColor(), size)
                    rowNumber += 1
            else:
                if (stock != 0):
                    size = "4" + str(index)
                    createAndFillRow(rowNumber, myfile, product, "variation", isFeatured, description, str(stock), "", images, parent, crossSellProducts, product.getColor(), size)
                    rowNumber += 1
            index += 1


        for prod in products:
            parent = prod.getStockID()

            if( (product.getFactory() == prod.getFactory() )
                    and ( product.getModelID() == prod.getModelID() )
                    and ( product.getColor() != prod.getColor() ) ):

                # adding other colored product's color and size to the colors and sizes lists
                colors.append(prod.getColor())
                index = -1
                for size in prod.getSizes():
                    if (index == -1):  # this is for 39 size check
                        if (size != "0"):
                            sizes.append("39")
                    else:
                        if (size != "0"):
                            sizes.append("4" + str(index))
                    index += 1


                index = -1
                for amountOfSize in prod.getSizes():
                    stock = int(amountOfSize)
                    if (index == -1):
                        if(stock != 0):
                            size = "39"
                            createAndFillRow(rowNumber, myfile, prod, "variation", isFeatured, description, str(stock),
                                             "", images, parent, crossSellProducts, prod.getColor(), size)
                            rowNumber += 1
                    else:
                        if( stock != 0 ):
                            size = "4" + str(index)
                            createAndFillRow(rowNumber, myfile, prod, "variation", isFeatured, description, str(stock), "", images, parent, crossSellProducts, prod.getColor(), size)
                            rowNumber += 1
                    index += 1

                isControlledDict[product.getFactory() + "-" + product.getDesignedYear() + product.getModelID()] += 1


        colors = unique(colors)
        #print(colors)
        colorsString = ""
        for color in colors:
            colorsString += str(color)
            if(color != colors[-1]):
                colorsString += ", "
        #print(colorsString)


        sizes = unique(sizes)
        #print(sizes)
        sizesString = ""
        for size in sizes:
            sizesString += str(size)
            if (size != sizes[-1]):
                sizesString += ", "
        #print(sizesString)


        myfile.setAttribute1Values(tempRowNumberForColorsAndSizes, colorsString)
        myfile.setAttribute2Values(tempRowNumberForColorsAndSizes, sizesString)

print(isControlledDict)







#gui()
#newGUI()
#gui1()
#gui2()
#gui3()


#    other_object.add(product)

# images[imageIndex].setStockID()
# images[imageIndex].setName(imageFilenameList[imageIndex])
# images[imageIndex].setModelID()
# images[imageIndex].setVariables()
# images[imageIndex].setPrice()

#objs[0].do_sth()


# for model in range(len(imageFilenameList)/4):
#     print("")







# Each product have 6 images
# system will take the names of images as a lot as an string


myfile.closeWorksheet()
