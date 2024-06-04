from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QListWidget
from PySide6.QtGui import QPixmap
from data.data_manager import DataManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QtpyDixitAll")
        self.data_manager = DataManager("src/data/data.xml")

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.term_label = QLabel("Término:")
        layout.addWidget(self.term_label)
        self.term_entry = QLineEdit()
        layout.addWidget(self.term_entry)

        self.definition_label = QLabel("Definición:")
        layout.addWidget(self.definition_label)
        self.definition_entry = QTextEdit()
        layout.addWidget(self.definition_entry)

        self.save_button = QPushButton("Guardar")
        self.save_button.clicked.connect(self.save_term)
        layout.addWidget(self.save_button)

        self.modify_button = QPushButton("Modificar")
        self.modify_button.clicked.connect(self.modify_term)
        layout.addWidget(self.modify_button)

        self.delete_button = QPushButton("Eliminar")
        self.delete_button.clicked.connect(self.delete_term)
        layout.addWidget(self.delete_button)

        self.search_label = QLabel("Término a consultar:")
        layout.addWidget(self.search_label)
        self.search_entry = QLineEdit()
        layout.addWidget(self.search_entry)

        self.search_button = QPushButton("Consultar")
        self.search_button.clicked.connect(self.search_term)
        layout.addWidget(self.search_button)

        self.output_label = QLabel("Definición:")
        layout.addWidget(self.output_label)
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        self.term_list_label = QLabel("Términos almacenados:")
        layout.addWidget(self.term_list_label)
        self.term_list = QListWidget()
        layout.addWidget(self.term_list)

        self.update_term_list()

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def save_term(self):
        term = self.term_entry.text()
        definition = self.definition_entry.toPlainText()
        if term and definition:
            self.data_manager.add_term(term, definition)
            self.update_term_list()

    def modify_term(self):
        term = self.term_entry.text()
        definition = self.definition_entry.toPlainText()
        if term and definition:
            self.data_manager.modify_term(term, definition)
            self.update_term_list()

    def delete_term(self):
        term = self.term_entry.text()
        if term:
            self.data_manager.delete_term(term)
            self.update_term_list()

    def search_term(self):
        term = self.search_entry.text()
        definition = self.data_manager.get_definition(term)
        if definition:
            self.output.setText(definition)
        else:
            self.output.setText("El término no existe")

    def update_term_list(self):
        self.term_list.clear()
        terms = self.data_manager.get_all_terms()
        self.term_list.addItems(terms)
