from Model import *

class Product(Model):
    def __init__(self, stockID):
        self.stockID = stockID
        self.images = []
        self.color = ""
        self.sizes = []

    def setStockID(self, stockID):
        self.stockID = stockID

    def getStockID(self):
        return self.stockID

    def addImageObject(self, Image):
        self.images.append(Image)

    def setImageName(self, index, imageName):
        self.images[index].setName(imageName)

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setSizes(self, sizes):
        self.sizes = sizes

    def getSizes(self):
        return self.sizes