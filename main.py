import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QFormLayout, QMessageBox, QComboBox, QTableWidget,QTableWidgetItem, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QSize, Qt    
from collections import namedtuple


class HBox(QWidget):
    def __init__(self, parent, align=None):
        super().__init__(parent)
        self._layout = QHBoxLayout(self)
        self.setLayout(self._layout)

        if align:
            self._layout.setAlignment(align)

    def addWidget(self, child):
        self._layout.addWidget(child)

    def setContentsMargins(self, *args):
        self._layout.setContentsMargins(*args)


class VBox(QWidget):
    def __init__(self, parent, align=None):
        super().__init__(parent)
        self._layout = QVBoxLayout(self)
        self.setLayout(self._layout)

        if align:
            self._layout.setAlignment(align)

    def addWidget(self, child):
        self._layout.addWidget(child)

    def setContentsMargins(self, *args):
        self._layout.setContentsMargins(*args)

class mainMenu(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setStyleSheet(qss_file)
        self.setMinimumSize(QSize(885, 720))    #set size
        self.setWindowTitle("FLIGHT PLANNING") #set title
        central_widget = QWidget()

        self.setCentralWidget(central_widget)
        
        self.error_dialog = QtWidgets.QErrorMessage()

        mainCol = VBox(central_widget)
        
        acComboRow = HBox(mainCol)
        txt1 = QLabel("FLIGHT PLANNING",self)
        acComboRow.addWidget(txt1)
        mainCol.addWidget(acComboRow)

        # Create a button in the window
        self.toAirport = QPushButton('Airport Details')
        self.toAirport.clicked.connect(self.hide)
        acConfirmRow = HBox(mainCol)
        acConfirmRow.addWidget(self.toAirport)
        mainCol.addWidget(acConfirmRow)

        self.toFlight = QPushButton('Flight Details')   
        self.toFlight.clicked.connect(self.hide)
        acBackRow = HBox(mainCol)
        acBackRow.addWidget(self.toFlight)
        mainCol.addWidget(acBackRow)

        self.toPrice = QPushButton('Calculate Profit Option')   
        self.toPrice.clicked.connect(self.hide)
        acBackRow = HBox(mainCol)
        acBackRow.addWidget(self.toPrice)
        mainCol.addWidget(acBackRow)

class airportWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setStyleSheet(qss_file)
        self.setMinimumSize(QSize(300, 720))    #set size
        self.setWindowTitle("AIRPORT LOL") #set title
        central_widget = QWidget()

        self.setCentralWidget(central_widget)

        # Create textbox
        self.textbox = QLineEdit()
        self.textbox2 = QLineEdit()   

        txt1 = QLabel("UK Airport Code",self)
        txt1.setAlignment(Qt.AlignCenter)    
        txt2 = QLabel("Overseas Airport Code",self)
        txt2.setAlignment(Qt.AlignCenter)

        txt3 = QLabel("Airport Name: ",self)
        txt3.setAlignment(Qt.AlignCenter)
        self.txt4 = QLabel("",self)
        self.txt4.setAlignment(Qt.AlignLeft)
        
        self.error_dialog = QtWidgets.QErrorMessage()

        mytext = QFormLayout(central_widget)
        mytext.addRow(txt1, self.textbox) #add label:input row
        mytext.addRow(txt2, self.textbox2)
        mytext.addRow(txt3, self.txt4) #add labal:label row

        # Create a button in the window
        self.button = QPushButton('Confirm')
        mytext.addRow(self.button)
        self.button.clicked.connect(self.airportClick)

        self.pushButton = QPushButton('Back')
        mytext.addRow(self.pushButton)
        self.pushButton.clicked.connect(self.hide) #button onclick event

    def airportClick(self):
        textboxValue = self.textbox.text()
        textboxValue2 = self.textbox2.text().upper()

        if airport := results.get(textboxValue2, None): #if textboxValue2 matches key in results dictionary, assign array of values to airport variable
            self.txt4.setText(airport[0]) #display full airport name
        else:
            if textboxValue.upper() != "LPL" and textboxValue.upper() != "BOH":
                self.error_dialog.showMessage("ERROR: INCORRECT UK AIRPORT CODE AND INCORRECT OVERSEAS AIRPORT CODE")
            else:
                self.error_dialog.showMessage("ERROR: INCORRECT OVERSEAS AIRPORT CODE")

class flightWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setStyleSheet(qss_file)
        self.setMinimumSize(QSize(885, 720))    #set size
        self.setWindowTitle("FLIGHT LOL") #set title
        central_widget = QWidget()

        self.setCentralWidget(central_widget)

        # Create textbox and dropdown menu
        self.textbox = QLineEdit()
        self.combobox = QComboBox(self)
        self.combobox.addItems([craft.type for craft in Aircraft]) 

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(5)

        item1 = QtWidgets.QTableWidgetItem('Type')
        self.tableWidget.setHorizontalHeaderItem(0,item1)
        item2 = QtWidgets.QTableWidgetItem('Running cost per seat per 100 km')
        self.tableWidget.setHorizontalHeaderItem(1,item2)
        item3 = QtWidgets.QTableWidgetItem('Maximum flight range (km)')
        self.tableWidget.setHorizontalHeaderItem(2,item3)
        item4 = QtWidgets.QTableWidgetItem('Capacity if all seats are standard-class')
        self.tableWidget.setHorizontalHeaderItem(3,item4)
        item5 = QtWidgets.QTableWidgetItem('Minimum number of first-class seats')
        self.tableWidget.setHorizontalHeaderItem(4,item5)

        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.resizeColumnsToContents() #make table resize nicely

        txt1 = QLabel("Aircraft Type",self)
        txt2 = QLabel("Number of first-class seats",self)

        txt3 = QLabel("Number of standard-class seats: ",self)
        self.txt4 = QLabel("NA",self)
        self.txt4.setAlignment(Qt.AlignLeft)
        
        self.error_dialog = QtWidgets.QErrorMessage()
        mainCol = VBox(central_widget)
        acComboRow = HBox(mainCol)
        acComboRow.addWidget(txt1)
        acComboRow.addWidget(self.combobox)
        mainCol.addWidget(acComboRow)

        acTypeRow = HBox(mainCol)
        acTypeRow.addWidget(txt2)
        acTypeRow.addWidget(self.textbox)
        mainCol.addWidget(acTypeRow)

        acLabelRow = HBox(mainCol)
        acLabelRow.addWidget(txt3)
        acLabelRow.addWidget(self.txt4)
        mainCol.addWidget(acLabelRow)

        acTableRow = HBox(mainCol)
        acTableRow.addWidget(self.tableWidget)
        mainCol.addWidget(acTableRow)

        # Create a button in the window
        self.button = QPushButton('Confirm')
        self.button.clicked.connect(self.flightClick)
        acConfirmRow = HBox(mainCol)
        acConfirmRow.addWidget(self.button)
        mainCol.addWidget(acConfirmRow)

        self.pushButton = QPushButton('Back')
        self.pushButton.clicked.connect(self.hide) #button onclick event
        
        acBackRow = HBox(mainCol)
        acBackRow.addWidget(self.pushButton)
        mainCol.addWidget(acBackRow)

    def flightClick(self):
        textboxValue = self.textbox.text() #NEED TO IMPLEMENT MATHS
        textboxValue2 = self.combobox.currentText() #IMPLEMENT TABLE NAMES

        if items := [i for i in Aircraft if i.type==textboxValue2][0]: #find tuple that type is in
            for i in range(5):
                item = QTableWidgetItem(items[i])
                item.setFlags(QtCore.Qt.ItemIsEnabled) #make table uneditable
                self.tableWidget.setItem(0, i, QTableWidgetItem(item))
                self.tableWidget.resizeColumnsToContents() #make table resize nicely

class Manager:
    def __init__(self):
        self.menu = mainMenu()
        self.airport = airportWindow()
        self.flight = flightWindow()

        self.menu.toAirport.clicked.connect(self.airport.show)
        self.menu.toFlight.clicked.connect(self.flight.show)
        self.menu.toPrice.clicked.connect(self.airport.show) # replace with price class

        self.airport.pushButton.clicked.connect(self.menu.show) 
        self.flight.pushButton.clicked.connect(self.menu.show)

        self.menu.show()

if __name__ == "__main__":
    global qss_file
    qss_file = open('style.qss').read() #make it look nice lol

    global results
    global Aircraft
    with open('Airports.txt', 'r') as f: #open airport csv
        results = {}
        for line in f:
                words = line.split(',') #splits csv format
                results[words[0]] =  words[1:] #adds to global dictionary

    with open('Aircraft.csv', 'r') as f: #open aircraft csv
        f = f.read()
        ImportedObject = namedtuple("ImportedObject", f.split("\n")[0].replace(",", ""))
        Aircraft = [ImportedObject(*i.split(", ")) for i in f.split("\n")[1:-1]] 

    app = QtWidgets.QApplication(sys.argv) #GUI
    mainWin = Manager()
    sys.exit( app.exec_() )