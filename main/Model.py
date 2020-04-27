class Model(object):
    def __init__(self, modelID, designedYear="2020"):
        self.factory = ""
        self.designedYear = designedYear
        self.modelID = modelID
        self.price = ""
        self.season = ""
        self.style = ""
        self.rubberType = ""


    def setModelID(self, modelID):
        self.modelID = modelID

    def getModelID(self ):
        return self.modelID

    def setDesignedYear(self, year):
        self.year = year

    def getDesignedYear(self):
        return self.year

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def setFactory(self, factory):
        self.factory = factory

    def getFactory(self):
        return self.factory

    def setSeason(self, season):
        self.season = season

    def getSeason(self):
        return self.season

    def setStyle(self, style):
        self.style = style

    def getStyle(self):
        return self.style

    def setRubberType(self, rubberType):
        self.rubberType = rubberType

    def getRubberType(self):
        return self.rubberType