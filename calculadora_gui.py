"""
Calculadora de escritorio con interfaz grafica.

Ejecutar:
    python calculadora_gui.py

La aplicacion usa tkinter, una libreria incluida en la instalacion
estandar de Python, por lo que no requiere paquetes externos.
"""

import tkinter as tk
from tkinter import ttk


class CalculadoraApp:
    """Controla la interfaz y la logica de una calculadora basica."""

    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Python")
        self.root.geometry("360x520")
        self.root.minsize(320, 480)
        self.root.configure(bg="#f4f7fb")

        self.expression = ""
        self.display_value = tk.StringVar(value="0")

        self._configure_styles()
        self._build_layout()
        self._bind_keyboard()

    def _configure_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Display.TEntry",
            fieldbackground="#ffffff",
            foreground="#172033",
            bordercolor="#d6dee9",
            lightcolor="#d6dee9",
            darkcolor="#d6dee9",
            padding=16,
            font=("Segoe UI", 24, "bold"),
        )

        style.configure(
            "Number.TButton",
            background="#ffffff",
            foreground="#172033",
            bordercolor="#d6dee9",
            focusthickness=0,
            padding=14,
            font=("Segoe UI", 14, "bold"),
        )
        style.map("Number.TButton", background=[("active", "#eaf1fb")])

        style.configure(
            "Operator.TButton",
            background="#dbeafe",
            foreground="#1d4ed8",
            bordercolor="#bfdbfe",
            padding=14,
            font=("Segoe UI", 14, "bold"),
        )
        style.map("Operator.TButton", background=[("active", "#bfdbfe")])

        style.configure(
            "Action.TButton",
            background="#fee2e2",
            foreground="#b91c1c",
            bordercolor="#fecaca",
            padding=14,
            font=("Segoe UI", 14, "bold"),
        )
        style.map("Action.TButton", background=[("active", "#fecaca")])

        style.configure(
            "Equal.TButton",
            background="#2563eb",
            foreground="#ffffff",
            bordercolor="#1d4ed8",
            padding=14,
            font=("Segoe UI", 14, "bold"),
        )
        style.map("Equal.TButton", background=[("active", "#1d4ed8")])

    def _build_layout(self):
        container = tk.Frame(self.root, bg="#f4f7fb", padx=18, pady=18)
        container.pack(fill="both", expand=True)

        title = tk.Label(
            container,
            text="Calculadora",
            bg="#f4f7fb",
            fg="#172033",
            font=("Segoe UI", 18, "bold"),
            anchor="w",
        )
        title.pack(fill="x", pady=(0, 12))

        display = ttk.Entry(
            container,
            textvariable=self.display_value,
            style="Display.TEntry",
            justify="right",
            state="readonly",
        )
        display.pack(fill="x", pady=(0, 16), ipady=8)

        keypad = tk.Frame(container, bg="#f4f7fb")
        keypad.pack(fill="both", expand=True)

        buttons = [
            ("C", self.clear, "Action.TButton"),
            ("⌫", self.backspace, "Action.TButton"),
            ("%", self.percent, "Operator.TButton"),
            ("÷", lambda: self.add_operator("/"), "Operator.TButton"),
            ("7", lambda: self.add_value("7"), "Number.TButton"),
            ("8", lambda: self.add_value("8"), "Number.TButton"),
            ("9", lambda: self.add_value("9"), "Number.TButton"),
            ("×", lambda: self.add_operator("*"), "Operator.TButton"),
            ("4", lambda: self.add_value("4"), "Number.TButton"),
            ("5", lambda: self.add_value("5"), "Number.TButton"),
            ("6", lambda: self.add_value("6"), "Number.TButton"),
            ("−", lambda: self.add_operator("-"), "Operator.TButton"),
            ("1", lambda: self.add_value("1"), "Number.TButton"),
            ("2", lambda: self.add_value("2"), "Number.TButton"),
            ("3", lambda: self.add_value("3"), "Number.TButton"),
            ("+", lambda: self.add_operator("+"), "Operator.TButton"),
            ("±", self.toggle_sign, "Operator.TButton"),
            ("0", lambda: self.add_value("0"), "Number.TButton"),
            (".", lambda: self.add_value("."), "Number.TButton"),
            ("=", self.calculate, "Equal.TButton"),
        ]

        for index, (text, command, style) in enumerate(buttons):
            row = index // 4
            column = index % 4
            button = ttk.Button(keypad, text=text, command=command, style=style)
            button.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)

        for i in range(5):
            keypad.rowconfigure(i, weight=1)
        for i in range(4):
            keypad.columnconfigure(i, weight=1)

    def _bind_keyboard(self):
        self.root.bind("<Key>", self.handle_keypress)
        self.root.bind("<Return>", lambda _event: self.calculate())
        self.root.bind("<BackSpace>", lambda _event: self.backspace())
        self.root.bind("<Escape>", lambda _event: self.clear())

    def handle_keypress(self, event):
        key = event.char
        if key in "0123456789.":
            self.add_value(key)
        elif key in "+-*/":
            self.add_operator(key)
        elif key in ("=", "\r"):
            self.calculate()

    def add_value(self, value):
        if self.display_value.get() == "Error":
            self.clear()

        if value == ".":
            current_number = self._current_number()
            if "." in current_number:
                return
            if current_number == "":
                value = "0."

        self.expression += value
        self._refresh_display()

    def add_operator(self, operator):
        if not self.expression or self.display_value.get() == "Error":
            return

        if self.expression[-1] in "+-*/":
            self.expression = self.expression[:-1] + operator
        else:
            self.expression += operator

        self._refresh_display()

    def calculate(self):
        if not self.expression:
            return

        try:
            result = eval(self.expression, {"__builtins__": {}}, {})
            self.expression = self._format_number(result)
            self.display_value.set(self.expression)
        except ZeroDivisionError:
            self.expression = ""
            self.display_value.set("Error")
        except Exception:
            self.expression = ""
            self.display_value.set("Error")

    def clear(self):
        self.expression = ""
        self.display_value.set("0")

    def backspace(self):
        if self.display_value.get() == "Error":
            self.clear()
            return

        self.expression = self.expression[:-1]
        self._refresh_display()

    def percent(self):
        if not self.expression or self.expression[-1] in "+-*/":
            return

        try:
            value = eval(self.expression, {"__builtins__": {}}, {}) / 100
            self.expression = self._format_number(value)
            self.display_value.set(self.expression)
        except Exception:
            self.expression = ""
            self.display_value.set("Error")

    def toggle_sign(self):
        if not self.expression or self.display_value.get() == "Error":
            return

        operators = ["+", "-", "*", "/"]
        last_operator_index = -1
        for operator in operators:
            last_operator_index = max(last_operator_index, self.expression.rfind(operator))

        number_start = last_operator_index + 1
        current_number = self.expression[number_start:]

        if not current_number:
            return

        if current_number.startswith("-"):
            current_number = current_number[1:]
        else:
            current_number = "-" + current_number

        self.expression = self.expression[:number_start] + current_number
        self._refresh_display()

    def _refresh_display(self):
        if self.expression:
            pretty_expression = (
                self.expression.replace("*", "×")
                .replace("/", "÷")
                .replace("-", "−")
            )
            self.display_value.set(pretty_expression)
        else:
            self.display_value.set("0")

    def _current_number(self):
        last_operator = max(
            self.expression.rfind("+"),
            self.expression.rfind("-"),
            self.expression.rfind("*"),
            self.expression.rfind("/"),
        )
        return self.expression[last_operator + 1 :]

    @staticmethod
    def _format_number(number):
        if isinstance(number, float) and number.is_integer():
            return str(int(number))
        return str(round(number, 10)).rstrip("0").rstrip(".")


def main():
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
