from imp import reload
from xlsxwriter import Workbook
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

excellSheetName = "pittimen2020"

class Excell(Workbook):
    def __init__(self, name = str(excellSheetName) ):
        self.name = name + ".xlsx"
        self.workbook = Workbook(self.name)
        self.worksheet = []

    def createWorkbook(self):
        self.workbook = Workbook(self.name)

    def createWorksheet(self):
        self.worksheet = self.workbook.add_worksheet()

    def closeWorksheet(self):
        self.workbook.close()

    def setWorksheetHeaders(self):
        # Widen the first column to make the text clearer.
        self.worksheet.set_column('AA:AA', 200)
        self.worksheet.set_default_row(13)

        # write headers
        self.worksheet.write('A1', 'Type')
        self.worksheet.write('B1', 'SKU')
        self.worksheet.write('C1', 'Name')
        self.worksheet.write('D1', 'Published')
        self.worksheet.write('E1', 'Is featured?')
        self.worksheet.write('F1', 'Visibility in catalog')
        self.worksheet.write('G1', 'Short description')
        self.worksheet.write('H1', 'Description')
        self.worksheet.write('I1', 'Date sale price starts')
        self.worksheet.write('J1', 'Date sale price ends')
        self.worksheet.write('K1', 'Tax class')
        self.worksheet.write('L1', 'In stock?')
        self.worksheet.write('M1', 'Stock')
        self.worksheet.write('N1', 'Backorders allowed?')
        self.worksheet.write('O1', 'Sold individually?')
        self.worksheet.write('P1', 'Weight (kg)')
        self.worksheet.write('Q1', 'Length (cm)')
        self.worksheet.write('R1', 'Width (cm)')
        self.worksheet.write('S1', 'Height (cm)')
        self.worksheet.write('T1', 'Allow customer reviews?')
        self.worksheet.write('U1', 'Purchase note')
        self.worksheet.write('V1', 'Sale price')
        self.worksheet.write('W1', 'Regular price')
        self.worksheet.write('X1', 'Categories')
        self.worksheet.write('Y1', 'Tags')
        self.worksheet.write('Z1', 'Shipping class')
        self.worksheet.write('AA1', 'Images')
        self.worksheet.write('AB1', 'Download limit')
        self.worksheet.write('AC1', 'Download expiry days')
        self.worksheet.write('AD1', 'Parent')
        self.worksheet.write('AE1', 'Grouped products')
        self.worksheet.write('AF1', 'Upsells')
        self.worksheet.write('AG1', 'Cross-sells')
        self.worksheet.write('AH1', 'External URL')
        self.worksheet.write('AI1', 'Button text')
        self.worksheet.write('AJ1', 'Download 1 name')
        self.worksheet.write('AK1', 'Download 1 URL')
        self.worksheet.write('AL1', 'Attribute 1 name')
        self.worksheet.write('AM1', 'Attribute 1 value(s)')
        self.worksheet.write('AN1', 'Attribute 1 visible')
        self.worksheet.write('AO1', 'Attribute 1 global')
        self.worksheet.write('AP1', 'Attribute 2 name')
        self.worksheet.write('AQ1', 'Attribute 2 value(s)')
        self.worksheet.write('AR1', 'Attribute 2 visible')
        self.worksheet.write('AS1', 'Attribute 2 global')
        self.worksheet.write('AT1', 'Attribute 1 default')
        self.worksheet.write('AU1', 'Attribute 2 default')

    def setType(self, rowNumber, value):
        self.worksheet.write('A' + str(rowNumber), value)

    def setSKU(self, rowNumber, value):
        self.worksheet.write('B' + str(rowNumber), value)

    def setName(self, rowNumber, value):
        self.worksheet.write('C' + str(rowNumber), value)

    def setPublished(self, rowNumber, value):
        self.worksheet.write('D' + str(rowNumber), value)

    def setIsFeatured(self, rowNumber, value):
        self.worksheet.write('E' + str(rowNumber), value)

    def setVisibilityInCatalog(self, rowNumber, value):
        self.worksheet.write('F' + str(rowNumber), value)

    def setShortSescription(self, rowNumber, value):
        self.worksheet.write('G' + str(rowNumber), value)

    def setDescription(self, rowNumber, value):
        self.worksheet.write('H' + str(rowNumber), value)

    def setDateSalePriceStarts(self, rowNumber, value):
        self.worksheet.write('I' + str(rowNumber), value)

    def setDateSalePriceEnds(self, rowNumber, value):
        self.worksheet.write('J' + str(rowNumber), value)

    def setTaxClass(self, rowNumber, value):
        self.worksheet.write('K' + str(rowNumber), value)

    def setInStock(self, rowNumber, value):
        self.worksheet.write('L' + str(rowNumber), value)

    def setStock(self, rowNumber, value):
        self.worksheet.write('M' + str(rowNumber), value)

    def setBackordersAllowed(self, rowNumber, value):
        self.worksheet.write('N' + str(rowNumber), value)

    def setSoldIndividually(self, rowNumber, value):
        self.worksheet.write('O' + str(rowNumber), value)

    def setWeightInKg(self, rowNumber, value):
        self.worksheet.write('P' + str(rowNumber), value)

    def setLengthIncm(self, rowNumber, value):
        self.worksheet.write('Q' + str(rowNumber), value)

    def setWidthIncm(self, rowNumber, value):
        self.worksheet.write('R' + str(rowNumber), value)

    def setHeightIncm(self, rowNumber, value):
        self.worksheet.write('S' + str(rowNumber), value)

    def setAllowCustomerReviews(self, rowNumber, value):
        self.worksheet.write('T' + str(rowNumber), value)

    def setPurchaseNote(self, rowNumber, value):
        self.worksheet.write('U' + str(rowNumber), value)

    def setSalePrice(self, rowNumber, value):
        self.worksheet.write('V' + str(rowNumber), value)

    def setRegularPrice(self, rowNumber, value):
        self.worksheet.write('W' + str(rowNumber), value)

    def setCategories(self, rowNumber, value):
        self.worksheet.write('X' + str(rowNumber), value)

    def setTags(self, rowNumber, value):
        self.worksheet.write('Y' + str(rowNumber), value)

    def setShippingClass(self, rowNumber, value):
        self.worksheet.write('Z' + str(rowNumber), value)

    def setImages(self, rowNumber, value):
        self.worksheet.write('AA' + str(rowNumber), value)

    def setDownloadLimit(self, rowNumber, value):
        self.worksheet.write('AB' + str(rowNumber), value)

    def setDownloadExpiryDays(self, rowNumber, value):
        self.worksheet.write('AC' + str(rowNumber), value)

    def setParent(self, rowNumber, value):
        self.worksheet.write('AD' + str(rowNumber), value)

    def setGroupedProducts(self, rowNumber, value):
        self.worksheet.write('AE' + str(rowNumber), value)

    def setUpsells(self, rowNumber, value):
        self.worksheet.write('AF' + str(rowNumber), value)

    def setCrossSells(self, rowNumber, value):
        self.worksheet.write('AG' + str(rowNumber), value)

    def setExternalURL(self, rowNumber, value):
        self.worksheet.write('AH' + str(rowNumber), value)

    def setButtonText(self, rowNumber, value):
        self.worksheet.write('AI' + str(rowNumber), value)

    def setDownload1Name(self, rowNumber, value):
        self.worksheet.write('AJ' + str(rowNumber), value)

    def setDownload1URL(self, rowNumber, value):
        self.worksheet.write('AK' + str(rowNumber), value)

    def setAttribute1Name(self, rowNumber, value):
        self.worksheet.write('AL' + str(rowNumber), value)

    def setAttribute1Values(self, rowNumber, value):
        self.worksheet.write('AM' + str(rowNumber), value)

    def setAttribute1Visible(self, rowNumber, value):
        self.worksheet.write('AN' + str(rowNumber), value)

    def setAttribute1Global(self, rowNumber, value):
        self.worksheet.write('AO' + str(rowNumber), value)

    def setAttribute2Name(self, rowNumber, value):
        self.worksheet.write('AP' + str(rowNumber), value)

    def setAttribute2Values(self, rowNumber, value):
        self.worksheet.write('AQ' + str(rowNumber), value)

    def setAttribute2Visible(self, rowNumber, value):
        self.worksheet.write('AR' + str(rowNumber), value)

    def setAttribute2Global(self, rowNumber, value):
        self.worksheet.write('AS' + str(rowNumber), value)

    def setAttribute1Default(self, rowNumber, value):
        self.worksheet.write('AT' + str(rowNumber), value)

    def setAttribute2Default(self, rowNumber, value):
        self.worksheet.write('AU' + str(rowNumber), value)