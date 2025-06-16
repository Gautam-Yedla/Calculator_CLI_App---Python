![Python CI](https://github.com/Gautam-Yedla/Calculator_CLI_App---Python/actions/workflows/python-ci.yml/badge.svg)

# 🧮 Python Calculator (CLI + GUI)


A beginner-friendly calculator app built in **Python**, available in both **command-line** and **GUI (PyQt5)** versions. Supports all essential operations, lets you perform chained calculations, and logs history to a file.

---

## 🚀 Features

### ✅ CLI Version:
- ➕ Addition (`+`)
- ➖ Subtraction (`-`)
- ✖️ Multiplication (`*`)
- ➗ Division (`/`) with zero-division protection
- 🔺 Exponentiation (`^`)
- 🧮 Modulus (`%`) with zero-division protection
- 🔁 Continue with previous result
- 🔄 Menu loop for repeated calculations
- 🛡️ Full input validation and edge-case handling

### ✅ GUI Version (PyQt5):
- 🖱️ Button-based calculator interface
- 🧾 Result history (last 10 calculations)
- 💾 Logs calculations to `calc_history.txt`
- 💡 Expression evaluation with support for `^`, `%`, and `()`

---

## 🛠️ Technologies Used

- Python 3.x
- PyQt5 (`pip install PyQt5`)

---

## 🧠 Concepts Covered

- Variables & data types
- Functions and return values
- Conditional statements
- Loops and logic control
- Error handling (`try/except`)
- User interaction: `input()`, `print()`, and GUI widgets
- Basic file I/O
- Modular coding
- GUI design principles with `PyQt5`

---

## 🖥️ How to Run

### 1. 📟 CLI Calculator

```bash
git clone https://github.com/yourusername/cli-calculator.git
cd cli-calculator
python calculator.py
```

### 2. 🪟 GUI Calculator (PyQt5)

Install PyQt5 (if not already):

```bash
pip install PyQt5
```

Then run:

```bash
python gui_calculator.py
```

> ✅ All calculations are saved in `calc_history.txt`.

---

## 🧪 Testing

You can write tests for the core logic using `unittest`:

```bash
python -m unittest test_calculator.py
```

---

## 🧾 Sample CLI Usage

```bash
Choose operation:
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Exponent (^)
6. Modulus (%)
7. Exit

Enter choice (1–7): 5
Enter first number: 3
Enter second number: 4

✅ Result: 81.0
```

---

## 🧱 Project Structure

```
calculator/
│
├── calculator.py          # CLI version
├── gui_calculator.py      # PyQt5 GUI version
├── test_calculator.py     # Unit tests (optional)
├── calc_history.txt       # History log (auto-generated)
└── README.md
```

---

## 💡 Future Improvements

- [ ] Add keyboard shortcuts to GUI
- [ ] Add dark mode toggle
- [ ] Export history as CSV
- [ ] Add scientific functions (sin, cos, sqrt, log)
- [ ] Package as an executable using PyInstaller

---

## 👨‍💻 Author

Made with ❤️ by [Gautam Yedla](https://github.com/Gautam-Yedla/Calculator_CLI_App---Python.git)

---

