import requests
import json
import sys
import time
import serial
import socket
from threading import Thread
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon, QFont, QColor, QPalette
from PyQt5.QtWidgets import QApplication, QTextEdit, QFrame, QGraphicsView, QMainWindow, QWidget, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QLabel, QHBoxLayout




class StackedWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("StackedWidget Example")
        self.setGeometry(0, 0, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.stacked_widget = QStackedWidget()

        self.page1 = QWidget()
        self.page2 = QWidget()
        self.page3 = QWidget()
        self.page4 = QWidget()
        self.page5 = QWidget()
        self.page6 = QWidget()
        self.page7 = QWidget()
        self.page8 = QWidget()
        self.page9 = QWidget()


        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)
        self.stacked_widget.addWidget(self.page4)
        self.stacked_widget.addWidget(self.page5)
        self.stacked_widget.addWidget(self.page6)
        self.stacked_widget.addWidget(self.page7)
        self.stacked_widget.addWidget(self.page8)
        self.stacked_widget.addWidget(self.page9)

        layout.addWidget(self.stacked_widget)

        # Populate pages
        self.populate_page1()
        self.populate_page2()
        self.populate_page3()
        self.populate_page4()
        self.populate_page5()
        self.populate_page6()
        self.populate_page7()
        self.populate_page8()
        self.populate_page9()

        # Show the initial page
        self.show_page1()

        self.previous_page = None


    #Main Window
    def populate_page1(self):
        background_label = QLabel(self.page1)
        background_label.setPixmap(QPixmap("images/Background.png"))
        background_label.setGeometry(0, 0, 800, 600)
        background_label.setScaledContents(True)

        self.plate_number = QPushButton(self.page1)
        self.plate_number.setGeometry(70, 180, 300, 300)
        self.plate_number.setStyleSheet(u"border-radius:18px;")
        self.plate_number.setIcon(QIcon("images/Plate Button.png"))
        self.plate_number.setIconSize(QSize(300, 300))
        self.plate_number.clicked.connect(self.show_page2)

        self.qr_code = QPushButton(self.page1)
        self.qr_code.setGeometry(440, 180, 301, 301)
        self.qr_code.setStyleSheet(u"border-radius:18px;")
        self.qr_code.setIcon(QIcon("images/QR Button.png"))
        self.qr_code.setIconSize(QSize(300, 300))
        self.qr_code.clicked.connect(self.show_page3)


    #Enter Plate Number
    def populate_page2(self):
        background_label2 = QLabel(self.page2)
        background_label2.setPixmap(QPixmap("images/Background.png"))
        background_label2.setGeometry(0, 0, 800, 600)
        background_label2.setScaledContents(True)

        self.plate_label= QLabel(self.page2)
        self.plate_label.setGeometry(159, 110, 481, 71)
        font = QFont()
        font.setFamilies(["Gotham"])
        font.setPointSize(24)
        font.setBold(True)
        self.plate_label.setFont(font)
        self.plate_label.setStyleSheet("color: white;")
        self.plate_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.plate_label.setText("Enter your car plate number")

        self.plate_lineEdit = QLineEdit(self.page2)
        self.plate_lineEdit.setFont(font)
        self.plate_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.plate_lineEdit.setGeometry(160, 180, 481, 61)
        self.plate_lineEdit.setStyleSheet("border-radius: 10px;")

        #Keyboard
        button_positions = [
            (68, 260, "1"), (124, 260, "2"), (180, 260, "3"), (236, 260, "4"),
            (292, 260, "5"), (348, 260, "6"), (404, 260, "7"), (460, 260, "8"),
            (516, 260, "9"), (572, 260, "0"), (123, 316, "Q"), (179, 316, "W"),
            (235, 316, "E"), (291, 316, "R"), (347, 316, "T"), (403, 316, "Y"),
            (459, 316, "U"), (515, 316, "I"), (571, 316, "O"), (627, 316, "P"),
            (151, 372, "A"), (207, 372, "S"), (263, 372, "D"), (319, 372, "F"),
            (375, 372, "G"), (431, 372, "H"), (487, 372, "J"), (543, 372, "K"),
            (599, 372, "L"), (178, 430, "Z"), (234, 430, "X"), (290, 430, "C"),
            (346, 430, "V"), (402, 430, "B"), (458, 430, "N"), (514, 430, "M"),
            (570, 430, "-")
        ]

        font2 = QFont()
        font2.setFamilies(["Gotham"])
        font2.setPointSize(16)
        font2.setBold(True)

        for x, y, text in button_positions:
            button = QPushButton(self.page2)
            button.setGeometry(x, y, 50, 50)
            button.setFont(font2)
            button.setStyleSheet("background-color: white;" "border-width:2px;" "border-radius:10px;")
            button.setText(text)
            button.clicked.connect(lambda _, button=button: self.on_button_click(button.text()))
           

        self.delete = QPushButton(self.page2)
        self.delete.setGeometry(630, 260, 91, 50)
        self.delete.setFont(font2)
        self.delete.setStyleSheet("background-color: white;" "border-width:2px;" "border-radius:10px;")
        self.delete.setText("DELETE")
        self.delete.clicked.connect(self.delete_input)


        self.next_button  = QPushButton(self.page2)
        self.next_button.setGeometry(558, 485, 190, 90)
        font3 = QFont()
        font3.setFamilies(["Gotham"])
        font3.setPointSize(22)
        font3.setBold(True)
        self.next_button.setFont(font3)
        self.next_button.setStyleSheet("background-color: rgb(25, 65, 108);\n" "color:white;\n" "border-width:2px;\n" "border-radius:10px;\n")
        self.next_button.setText("NEXT")
        self.next_button.clicked.connect(self.populate_page4)
        self.next_button.clicked.connect(self.show_page4)

        self.back_button = QPushButton(self.page2)
        self.back_button.setGeometry(41, 485, 190, 90)
        self.back_button.setFont(font3)
        self.back_button.setStyleSheet("background-color: rgb(25, 65, 108);\n" "color:white;\n" "border-width:2px;\n" "border-radius:10px;\n")
        self.back_button.setText("BACK")
        self.back_button.clicked.connect(self.show_page1)

        self.next_button.clicked.connect(self.set_previous_page_to_2)
        self.next_button.clicked.connect(self.populate_page4)
        self.next_button.clicked.connect(self.show_page4)

    def set_previous_page_to_2(self):
        self.previous_page = self.page2


    def on_button_click(self, text):
        current_text = self.plate_lineEdit.text()
        new_text = current_text + text
        self.plate_lineEdit.setText(new_text)


    def delete_input(self):
        self.plate_lineEdit.clear()
        self.total_label.clear()


    #Scan QR Ticket
    def populate_page3(self):
        self.label_3 = QLabel(self.page3)
        self.label_3.setGeometry(0, 0, 800, 600)
        self.label_3.setPixmap(QPixmap("images/Background.png"))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.qr_label = QLabel(self.page3)
        self.qr_label.setGeometry(150, 170, 511, 61)
        font4 = QFont()
        font4.setFamilies(["Gotham"])
        font4.setPointSize(36)
        font4.setBold(True)
        self.qr_label.setFont(font4)
        self.qr_label.setStyleSheet("color: white;")
        self.qr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.qr_label.setText("Scan your QR Ticket")

        self.qr_lineEdit = QLineEdit(self.page3)
        self.qr_lineEdit.setGeometry(150, 240, 511, 81)
        self.qr_lineEdit.setStyleSheet("border-radius: 10px;")
        self.qr_lineEdit.setFont(font4)
        self.qr_lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.next_button2 = QPushButton(self.page3)
        self.next_button2.setGeometry(540, 460, 191, 91)
        font5 = QFont()
        font5.setFamilies(["Gotham"])
        font5.setPointSize(22)
        font5.setBold(True)
        self.next_button2.setFont(font5)
        self.next_button2.setStyleSheet("background-color: rgb(25, 65, 108);\n" "color:white;\n" "border-width:2px;\n" "border-radius:10px;\n")
        self.next_button2.setText("NEXT")
        self.next_button2.clicked.connect(self.populate_page4)
        self.next_button2.clicked.connect(self.show_page4)

        self.back_button2 = QPushButton(self.page3)
        self.back_button2.setGeometry(50, 460, 191, 91)
        self.back_button2.setFont(font5)
        self.back_button2.setStyleSheet("background-color: rgb(25, 65, 108);\n" "color:white;\n" "border-width:2px;\n" "border-radius:10px;\n")
        self.back_button2.setText("BACK")
        self.back_button2.clicked.connect(self.show_page1)

        self.next_button2.clicked.connect(self.set_previous_page_to_3)
        self.next_button2.clicked.connect(self.populate_page4)
        self.next_button2.clicked.connect(self.show_page4)

    def set_previous_page_to_3(self):
        self.previous_page = self.page3

    #Customer Info
    def populate_page4(self):
        self.background_label4 = QLabel(self.page4)
        self.background_label4.setGeometry(0, 0, 800, 600)
        self.background_label4.setPixmap(QPixmap("images/Background.png"))
        self.background_label4.setScaledContents(True)

        self.plate_number = QLabel(self.page4)
        self.plate_number.setGeometry(15, 140, 201, 31)
        font6 = QFont()
        font6.setFamily(u"Gotham")
        font6.setPointSize(16)
        font6.setBold(True)
        self.plate_number.setFont(font6)
        self.plate_number.setStyleSheet(u"color: white;")
        self.plate_number.setText("PLATE NUMBER")

        self.plate_textEdit = QTextEdit(self.page4)
        self.plate_textEdit.setGeometry(270, 140, 281, 41)
        self.plate_textEdit.setStyleSheet(u"border-radius: 10px;\n" "background-color: white;\n" "color: rgb(2, 32, 52);\n""")
        self.plate_textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.plate_textEdit.setFont(font6)
        self.plate_textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.plate_textEdit.setUndoRedoEnabled(True)
        self.plate_textEdit.setReadOnly(True)


        self.entry_time = QLabel(self.page4)
        self.entry_time.setGeometry(15, 200, 171, 31)
        self.entry_time.setFont(font6)
        self.entry_time.setStyleSheet(u"color: white;")
        self.entry_time.setText("ENTRY TIME")

        self.time_textEdit = QTextEdit(self.page4)
        self.time_textEdit.setGeometry(270, 200, 281, 41)
        self.time_textEdit.setFont(font6)
        self.time_textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_textEdit.setStyleSheet(u"background-color: white;\n" "border-radius: 10px;\n" "color:rgb(2, 32, 52);\n")
        self.time_textEdit.setReadOnly(True)


        self.entry_gate = QLabel(self.page4)
        self.entry_gate.setGeometry(15, 260, 171, 31)
        self.entry_gate.setFont(font6)
        self.entry_gate.setStyleSheet(u"color: white;")
        self.entry_gate.setText("ENTRY GATE")

        self.gate_textEdit = QTextEdit(self.page4)
        self.gate_textEdit.setGeometry(270, 260, 281, 41)
        self.gate_textEdit.setStyleSheet(u"background-color: white;\n" "border-radius: 10px;\n" "color:rgb(2, 32, 52);\n")
        self.gate_textEdit.setFont(font6)
        self.gate_textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gate_textEdit.setReadOnly(True)


        self.vehicle_class = QLabel(self.page4)
        self.vehicle_class.setGeometry(15, 320, 201, 31)
        self.vehicle_class.setFont(font6)
        self.vehicle_class.setStyleSheet(u"color: white;")
        self.vehicle_class.setText("VEHICLE CLASS")

        self.vehicle_textEdit = QTextEdit(self.page4)
        self.vehicle_textEdit.setGeometry(270, 320, 281, 41)
        self.vehicle_textEdit.setStyleSheet(u"background-color: white;\n" "border-radius: 10px;\n" "color:rgb(2, 32, 52);")
        self.vehicle_textEdit.setFont(font6)
        self.vehicle_textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vehicle_textEdit.setReadOnly(True)


        self.parking_time = QLabel(self.page4)
        self.parking_time.setGeometry(15, 380, 251, 31)
        self.parking_time.setFont(font6)
        self.parking_time.setStyleSheet(u"color: white;")
        self.parking_time.setText("TOTAL PARKING TIME")

        self.parking_textEdit = QTextEdit(self.page4)
        self.parking_textEdit.setGeometry(270, 380, 281, 41)
        self.parking_textEdit.setStyleSheet(u"background-color: white;\n" "border-radius: 10px;\n" "color:rgb(2, 32, 52);")
        self.parking_textEdit.setFont(font6)
        self.parking_textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.parking_textEdit.setReadOnly(True)

        self.bill_amount = QLabel(self.page4)
        self.bill_amount.setGeometry(15, 505, 260, 40)
        font7 = QFont()
        font7.setFamilies([u"Gotham"])
        font7.setPointSize(24)
        font7.setBold(True)
        self.bill_amount.setFont(font7)
        self.bill_amount.setStyleSheet(u"color: white;")
        self.bill_amount.setText("BILL AMOUNT")

        self.textEdit_6 = QTextEdit(self.page4)
        self.textEdit_6.setGeometry(270, 505, 285, 45)
        self.textEdit_6.setStyleSheet(u"background-color: white;\n" "border-radius: 10px;\n" "color:rgb(2, 32, 52);")
        self.textEdit_6.setFont(font7)
        self.textEdit_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textEdit_6.setReadOnly(True)

        self.graphicsView = QGraphicsView(self.page4)
        self.graphicsView.setGeometry(570, 140, 201, 141)
        self.graphicsView.setStyleSheet(u"border-radius: 10px;\n" "background-color: white;")

        self.next_button3 = QPushButton(self.page4)
        self.next_button3.setGeometry(575, 480, 191, 91)
        font8 = QFont()
        font8.setFamilies(["Gotham"])
        font8.setPointSize(22)
        font8.setBold(True)
        self.next_button3.setFont(font8)
        self.next_button3.setStyleSheet("background-color: rgb(25, 65, 108);\n" "color:white;\n" "border-width:2px;\n" "border-radius:10px;\n")
        self.next_button3.setText("NEXT")
        self.next_button3.clicked.connect(self.show_page5)

        self.next_button3 = QPushButton(self.page4)
        self.next_button3.setGeometry(575, 379, 191, 91)
        self.next_button3.setFont(font8)
        self.next_button3.setStyleSheet("background-color: rgb(25, 65, 108);\n" "color:white;\n" "border-width:2px;\n" "border-radius:10px;\n")
        self.next_button3.setText("BACK")
        self.next_button3.clicked.connect(self.show_page3)

        self.next_button3.clicked.connect(self.back_to_previous_page)


        # Get user input from both fields
        qr_input = self.qr_lineEdit.text()
        plate_input = self.plate_lineEdit.text()

        # Determine which input to use based on user input
        if qr_input:
            user_input = qr_input
        elif plate_input:
            user_input = plate_input
        else:
            # Handle the case when neither field has input
            self.plate_textEdit.setPlainText("Please enter a value in either QR or Plate field.")
            return

        # Construct the URL with the selected user input
        url = f"http://13.209.8.192/parkingci/Cashier/billrequest?AccessType=QR&&parkingcode={user_input}"

        response = requests.get(url)

        if response.status_code == 200:
            # Parse the JSON response
            data = json.loads(response.text)

            # Populate QTextEdit widgets with data
            self.plate_textEdit.setPlainText(data.get("plate"))
            self.time_textEdit.setPlainText(str(data.get("entry_time")))
            self.gate_textEdit.setPlainText(data.get("gate"))
            self.vehicle_textEdit.setPlainText(data.get("vclass"))
            self.parking_textEdit.setPlainText(str(data.get("Ptime")))
            self.textEdit_6.setPlainText(str(data.get("bill")))
        else:
            # Handle the case when the request fails
            self.plate_textEdit.setPlainText("Error fetching data from the URL")
            self.time_textEdit.setPlainText("")
            self.time_textEdit.setPlainText("")
            self.gate_textEdit.setPlainText("")
            self.vehicle_textEdit.setPlainText("")
            self.parking_textEdit.setPlainText("")
            self.textEdit_6.setPlainText("")

    def back_to_previous_page(self):
        if self.previous_page:
            self.stacked_widget.setCurrentWidget(self.previous_page)



    #Mode of Payment
    def populate_page5(self):
        self.background_label5 = QLabel(self.page5)
        self.background_label5.setGeometry(0, 0, 800, 600)
        self.background_label5.setPixmap(QPixmap("images/Background.png"))
        self.background_label5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.payment_solution = QLabel(self.page5)
        self.payment_solution.setGeometry(90, 100, 611, 131)
        font9 = QFont()
        font9.setFamilies([u"Gotham"])
        font9.setPointSize(36)
        font9.setBold(True)
        self.payment_solution.setFont(font9)
        self.payment_solution.setStyleSheet(u"color: white;")
        self.payment_solution.setText("Select Payment Solution")
        self.payment_solution.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gcash_button = QPushButton(self.page5)
        self.gcash_button.setGeometry(40, 250, 221, 221)
        self.gcash_button.setStyleSheet(u"border-radius: 18px;")
        self.gcash_button.setIcon(QIcon("images/Gcash button.png"))
        self.gcash_button.setIconSize(QSize(225, 225))
        self.gcash_button.clicked.connect(self.show_page6)

        self.cash_button = QPushButton(self.page5)
        self.cash_button.setGeometry(290, 250, 221, 221)
        self.cash_button.setStyleSheet(u"border-radius: 18px;\n""")
        self.cash_button.setIcon(QIcon("images/Cash button.png"))
        self.cash_button.setIconSize(QSize(225, 225))
        self.cash_button.clicked.connect(self.show_page7)

        self.maya_button = QPushButton(self.page5)
        self.maya_button.setGeometry(540, 250, 221, 221)
        self.maya_button.setStyleSheet(u"border-radius: 18px;")
        self.maya_button.setIcon(QIcon("images/PayMaya button.png"))
        self.maya_button.setIconSize(QSize(225, 225))
        self.maya_button.clicked.connect(self.show_page8)     


    #Gcash QR Code Window
    def populate_page6(self):
        self.background_label6 = QLabel(self.page6)
        self.background_label6.setGeometry(0, 0, 800, 600)
        self.background_label6.setPixmap(QPixmap("images/Background.png"))
        self.background_label6.setScaledContents(True)

        self.gcash_label = QLabel(self.page6)
        self.gcash_label.setGeometry(200, 110, 400, 400)
        self.gcash_label.setPixmap(QPixmap("images/Gcash.png"))
        self.gcash_label.setScaledContents(True)

        
        self.next_button4 = QPushButton(self.page6)
        self.next_button4.setGeometry(575, 480, 191, 91)
        font12 = QFont()
        font12.setFamilies(["Gotham"])
        font12.setPointSize(22)
        font12.setBold(True)
        self.next_button4.setFont(font12)
        self.next_button4.setStyleSheet("background-color: rgb(25, 65, 108);\n" "color:white;\n" "border-width:2px;\n" "border-radius:10px;\n")
        self.next_button4.setText("NEXT")
        self.next_button4.clicked.connect(self.show_page9)


        self.back_button4 = QPushButton(self.page6)
        self.back_button4.setGeometry(20, 480, 190, 90)
        self.back_button4.setFont(font12)
        self.back_button4.setStyleSheet("background-color: rgb(25, 65, 108);\n" "color:white;\n" "border-width:2px;\n" "border-radius:10px;\n")
        self.back_button4.setText("BACK")
        self.back_button4.clicked.connect(self.show_page5)


    #Cash Window
    def populate_page7(self):
        self.background_label7 = QLabel(self.page7)
        self.background_label7.setGeometry(0, 0, 800, 600)
        self.background_label7.setPixmap(QPixmap("images/Background.png"))
        self.background_label7.setScaledContents(True)

        self.arduino_label = QLabel(self.page7) 
        self.arduino_label.setGeometry(250, 100, 300, 300)
        self.arduino_label.setPixmap(QPixmap("images/insert.png"))
        self.arduino_label.setScaledContents(True)

        self.total_label = QLabel(self.page7)
        self.total_label.setGeometry(90, 390, 610, 100)  
        self.total_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.total_label.setStyleSheet(u"color:white;")
        font13 = QFont()
        font13.setFamilies(["gotham"])
        font13.setBold(True)
        font13.setPointSize(34)
        self.total_label.setFont(font13) 
        self.total_label.setText("Total Amount: 0 pesos")

        self.next_button5 = QPushButton(self.page7)
        self.next_button5.setGeometry(575, 480, 191, 91)
        font14 = QFont()
        font14.setFamilies(["Gotham"])
        font14.setPointSize(22)
        font14.setBold(True)
        self.next_button5.setFont(font14)
        self.next_button5.setStyleSheet("background-color: rgb(25, 65, 108);\n" "color:white;\n" "border-width:2px;\n" "border-radius:10px;\n")
        self.next_button5.setText("NEXT")
        self.next_button5.clicked.connect(self.show_page9)

        self.back_button5 = QPushButton(self.page7)
        self.back_button5.setGeometry(20, 480, 190, 90)
        self.back_button5.setFont(font14)
        self.back_button5.setStyleSheet("background-color: rgb(25, 65, 108);\n" "color:white;\n" "border-width:2px;\n" "border-radius:10px;\n")
        self.back_button5.setText("BACK")
        self.back_button5.clicked.connect(self.show_page5)
        self.back_button5.clicked.connect(self.delete_input)

        self.serial_port = "COM4"
        self.serial_connected = False
        self.ser = None
        self.total_amount = 0

        self.connect_arduino()
        self.serial_thread = Thread(target=self.read_serial)
        self.serial_thread.start()

    def connect_arduino(self):
        try:
            self.ser = serial.Serial(self.serial_port, 9600, timeout=1)
            self.serial_connected = True
        except serial.SerialException:
            print("Error connecting to Arduino")

    def disconnect_arduino(self):
        if self.serial_connected:
            self.serial_connected = False
            self.ser.close()
        
    def read_serial(self):
        last_pulse_time = time.time()
        while self.serial_connected:
            line = self.ser.readline().decode("utf-8").strip()
            if line.startswith("Total:"):
                total_str = line.split()[1]
                total_peso = int(total_str)
                self.total_amount = total_peso
                last_pulse_time = time.time()

            if time.time() - last_pulse_time > 10.0:
                self.total_amount = 0

            if time.time() - last_pulse_time > 1.0:
                self.total_label.setText(f"Total Amount: {self.total_amount} pesos")


    #Pay Maya QR Window
    def populate_page8(self):
        self.background_label8 = QLabel(self.page8)
        self.background_label8.setGeometry(0, 0, 800, 600)
        self.background_label8.setPixmap(QPixmap("images/Background.png"))
        self.background_label8.setScaledContents(True)

        self.maya_label = QLabel(self.page8)
        self.maya_label.setGeometry(200, 110, 400, 400)
        self.maya_label.setPixmap(QPixmap("images/Pay Maya.png"))
        self.maya_label.setScaledContents(True)

        self.next_button6 = QPushButton(self.page8)
        self.next_button6.setGeometry(575, 480, 191, 91)
        font15 = QFont()
        font15.setFamilies(["Gotham"])
        font15.setPointSize(22)
        font15.setBold(True)
        self.next_button6.setFont(font15)
        self.next_button6.setStyleSheet("background-color: rgb(25, 65, 108);\n" "color:white;\n" "border-width:2px;\n" "border-radius:10px;\n")
        self.next_button6.setText("NEXT")
        self.next_button6.clicked.connect(self.show_page9)

        self.back_button6 = QPushButton(self.page8)
        self.back_button6.setGeometry(20, 480, 190, 90)
        self.back_button6.setFont(font15)
        self.back_button6.setStyleSheet("background-color: rgb(25, 65, 108);\n" "color:white;\n" "border-width:2px;\n" "border-radius:10px;\n")
        self.back_button6.setText("BACK")
        self.back_button6.clicked.connect(self.show_page5)


    #Receipt Window
    def populate_page9(self):
        self.background_label9 = QLabel(self.page9)
        self.background_label9.setGeometry(0, 0, 800, 600)
        self.background_label9.setPixmap(QPixmap("images/Background.png"))
        self.background_label9.setScaledContents(True)

        self.thanks_label = QLabel(self.page9)
        self.thanks_label.setGeometry(110, 260, 281, 61)
        self.thanks_label.setStyleSheet("color: white;")
        self.thanks_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font15 = QFont()
        font15.setFamilies(["Gotham"])
        font15.setPointSize(36)
        font15.setBold(True)
        self.thanks_label.setFont(font15)
        self.thanks_label.setText("Thank You!")

        self.receipt_label = QLabel(self.page9)
        self.receipt_label.setGeometry(70, 280, 361, 131)
        self.receipt_label.setStyleSheet("color: white;")
        self.receipt_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font16 = QFont()
        font16.setFamilies(["Gotham"])
        font16.setPointSize(24)
        font16.setBold(True)
        self.receipt_label.setFont(font16)
        self.receipt_label.setText("Please take receipt")
        self.receipt_label.setScaledContents(True)

        self.receipt_img = QLabel(self.page9)
        self.receipt_img.setGeometry(340, 80, 541, 521)
        self.receipt_img.setPixmap(QPixmap("images/Receipt.png"))
        self.receipt_img.setScaledContents(True)

    def show_page1(self):
        self.stacked_widget.setCurrentWidget(self.page1)

    def show_page2(self):
        self.stacked_widget.setCurrentWidget(self.page2)

    def show_page3(self):
        self.stacked_widget.setCurrentWidget(self.page3)

    def show_page4(self):
        self.stacked_widget.setCurrentWidget(self.page4)

    def show_page5(self):
        self.stacked_widget.setCurrentWidget(self.page5)

    def show_page6(self):
        self.stacked_widget.setCurrentWidget(self.page6)

    def show_page7(self):
        self.stacked_widget.setCurrentWidget(self.page7)

    def show_page8(self):
        self.stacked_widget.setCurrentWidget(self.page8)

    def show_page9(self):
        self.stacked_widget.setCurrentWidget(self.page9)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StackedWidget()
    window.show()
    sys.exit(app.exec())

    