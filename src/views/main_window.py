from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from src.views.book_view import BookView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Book Manager")
        self.setGeometry(100, 100, 800, 600)
        self.layout = QVBoxLayout()
       
        # Création du widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        # Layout principal ( Disposition)
        self.central_widget.setLayout(self.layout) # central_widget <-> main_layout 

        bookview = BookView()
        self.layout.addWidget(bookview)
        self.show()
