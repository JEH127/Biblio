from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class BookView(QWidget):
    def __init__(self):
        super().__init__()
        label = QLabel("Exemple Book")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)