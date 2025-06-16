import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLineEdit, QListWidget, QMessageBox
)

history = []

def log_to_file(expression, result):
    with open("calc_history.txt", "a") as f:
        f.write(f"{expression} = {result}\n")

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Calculator")
        self.setFixedSize(400, 400)

        self.expression = ""

        self.create_ui()

    def create_ui(self):
        main_layout = QVBoxLayout()

        # Entry field
        self.entry = QLineEdit()
        self.entry.setPlaceholderText("Enter expression")
        self.entry.setStyleSheet("font-size: 18px; padding: 5px;")
        main_layout.addWidget(self.entry)

        # Button grid layout
        button_layout = QVBoxLayout()
        rows = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '^', '+'],
            ['C', '%', '=', '']
        ]
        for row in rows:
            row_layout = QHBoxLayout()
            for label in row:
                if label:
                    btn = QPushButton(label)
                    btn.setFixedSize(60, 40)
                    btn.setStyleSheet("font-size: 16px;")
                    btn.clicked.connect(self.on_button_clicked)
                    row_layout.addWidget(btn)
            button_layout.addLayout(row_layout)

        main_layout.addLayout(button_layout)

        # History box
        self.history_box = QListWidget()
        self.history_box.setFixedHeight(100)
        main_layout.addWidget(self.history_box)

        self.setLayout(main_layout)

    def on_button_clicked(self):
        sender = self.sender()
        text = sender.text()

        if text == '=':
            self.evaluate()
        elif text == 'C':
            self.entry.clear()
        else:
            self.entry.setText(self.entry.text() + text)

    def evaluate(self):
        try:
            expr = self.entry.text().replace("^", "**")
            result = eval(expr)
            full_expr = f"{expr} = {result}"
            self.history_box.addItem(full_expr)
            history.append(full_expr)
            log_to_file(expr, result)
            self.entry.setText(str(result))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Invalid Input:\n{e}")

# Run the app
app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec_())
