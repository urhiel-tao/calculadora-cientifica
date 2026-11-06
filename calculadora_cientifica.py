"""
Calculadora cientifica de escritorio con interfaz grafica.

Ejecutar:
    python calculadora_cientifica.py

No requiere instalar librerias externas. Usa tkinter, que viene incluido
con la instalacion estandar de Python.
"""

import math
import tkinter as tk
from tkinter import ttk


class CalculadoraCientifica:
    """Interfaz y logica de una calculadora cientifica."""

    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Cientifica")
        self.root.geometry("520x680")
        self.root.minsize(420, 620)
        self.root.configure(bg="#f4f7fb")

        self.expression = ""
        self.display_value = tk.StringVar(value="0")
        self.angle_mode = tk.StringVar(value="DEG")

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
            font=("Segoe UI", 22, "bold"),
        )
        style.configure(
            "Number.TButton",
            background="#ffffff",
            foreground="#172033",
            bordercolor="#d6dee9",
            padding=12,
            font=("Segoe UI", 12, "bold"),
        )
        style.map("Number.TButton", background=[("active", "#eaf1fb")])

        style.configure(
            "Function.TButton",
            background="#e0f2fe",
            foreground="#075985",
            bordercolor="#bae6fd",
            padding=12,
            font=("Segoe UI", 11, "bold"),
        )
        style.map("Function.TButton", background=[("active", "#bae6fd")])

        style.configure(
            "Operator.TButton",
            background="#dbeafe",
            foreground="#1d4ed8",
            bordercolor="#bfdbfe",
            padding=12,
            font=("Segoe UI", 12, "bold"),
        )
        style.map("Operator.TButton", background=[("active", "#bfdbfe")])

        style.configure(
            "Action.TButton",
            background="#fee2e2",
            foreground="#b91c1c",
            bordercolor="#fecaca",
            padding=12,
            font=("Segoe UI", 12, "bold"),
        )
        style.map("Action.TButton", background=[("active", "#fecaca")])

        style.configure(
            "Equal.TButton",
            background="#2563eb",
            foreground="#ffffff",
            bordercolor="#1d4ed8",
            padding=12,
            font=("Segoe UI", 12, "bold"),
        )
        style.map("Equal.TButton", background=[("active", "#1d4ed8")])

    def _build_layout(self):
        container = tk.Frame(self.root, bg="#f4f7fb", padx=18, pady=18)
        container.pack(fill="both", expand=True)

        header = tk.Frame(container, bg="#f4f7fb")
        header.pack(fill="x", pady=(0, 12))

        title = tk.Label(
            header,
            text="Calculadora Cientifica",
            bg="#f4f7fb",
            fg="#172033",
            font=("Segoe UI", 18, "bold"),
            anchor="w",
        )
        title.pack(side="left", fill="x", expand=True)

        mode_button = ttk.Button(
            header,
            textvariable=self.angle_mode,
            command=self.toggle_angle_mode,
            style="Operator.TButton",
            width=7,
        )
        mode_button.pack(side="right")

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
            ("sin", lambda: self.add_function("sin("), "Function.TButton"),
            ("cos", lambda: self.add_function("cos("), "Function.TButton"),
            ("tan", lambda: self.add_function("tan("), "Function.TButton"),
            ("log", lambda: self.add_function("log10("), "Function.TButton"),
            ("ln", lambda: self.add_function("log("), "Function.TButton"),
            ("C", self.clear, "Action.TButton"),
            ("asin", lambda: self.add_function("asin("), "Function.TButton"),
            ("acos", lambda: self.add_function("acos("), "Function.TButton"),
            ("atan", lambda: self.add_function("atan("), "Function.TButton"),
            ("sqrt", lambda: self.add_function("sqrt("), "Function.TButton"),
            ("x!", self.factorial, "Function.TButton"),
            ("⌫", self.backspace, "Action.TButton"),
            ("(", lambda: self.add_value("("), "Operator.TButton"),
            (")", lambda: self.add_value(")"), "Operator.TButton"),
            ("x²", lambda: self.add_operator("**2"), "Function.TButton"),
            ("xʸ", lambda: self.add_operator("**"), "Function.TButton"),
            ("π", lambda: self.add_constant("pi"), "Function.TButton"),
            ("÷", lambda: self.add_operator("/"), "Operator.TButton"),
            ("7", lambda: self.add_value("7"), "Number.TButton"),
            ("8", lambda: self.add_value("8"), "Number.TButton"),
            ("9", lambda: self.add_value("9"), "Number.TButton"),
            ("e", lambda: self.add_constant("e"), "Function.TButton"),
            ("%", self.percent, "Function.TButton"),
            ("×", lambda: self.add_operator("*"), "Operator.TButton"),
            ("4", lambda: self.add_value("4"), "Number.TButton"),
            ("5", lambda: self.add_value("5"), "Number.TButton"),
            ("6", lambda: self.add_value("6"), "Number.TButton"),
            ("1/x", self.inverse, "Function.TButton"),
            ("±", self.toggle_sign, "Function.TButton"),
            ("−", lambda: self.add_operator("-"), "Operator.TButton"),
            ("1", lambda: self.add_value("1"), "Number.TButton"),
            ("2", lambda: self.add_value("2"), "Number.TButton"),
            ("3", lambda: self.add_value("3"), "Number.TButton"),
            (".", lambda: self.add_value("."), "Number.TButton"),
            ("=", self.calculate, "Equal.TButton"),
            ("+", lambda: self.add_operator("+"), "Operator.TButton"),
            ("0", lambda: self.add_value("0"), "Number.TButton"),
            ("00", lambda: self.add_value("00"), "Number.TButton"),
            ("Ans", lambda: self.add_value(self.display_value.get()), "Function.TButton"),
            ("mod", lambda: self.add_operator("%"), "Function.TButton"),
            ("EXP", lambda: self.add_operator("*10**"), "Function.TButton"),
            ("AC", self.clear, "Action.TButton"),
        ]

        for index, (text, command, style) in enumerate(buttons):
            row = index // 6
            column = index % 6
            button = ttk.Button(keypad, text=text, command=command, style=style)
            button.grid(row=row, column=column, sticky="nsew", padx=4, pady=4)

        for i in range(7):
            keypad.rowconfigure(i, weight=1)
        for i in range(6):
            keypad.columnconfigure(i, weight=1)

    def _bind_keyboard(self):
        self.root.bind("<Key>", self.handle_keypress)
        self.root.bind("<Return>", lambda _event: self.calculate())
        self.root.bind("<BackSpace>", lambda _event: self.backspace())
        self.root.bind("<Escape>", lambda _event: self.clear())

    def handle_keypress(self, event):
        key = event.char
        if key in "0123456789.()":
            self.add_value(key)
        elif key in "+-*/%":
            self.add_operator(key)
        elif key == "^":
            self.add_operator("**")
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
        if self.display_value.get() == "Error":
            self.clear()

        if not self.expression and operator not in ("-", "+"):
            return

        if self.expression and self.expression[-1] in "+-*/%" and operator not in ("**", "**2"):
            self.expression = self.expression[:-1] + operator
        else:
            self.expression += operator

        self._refresh_display()

    def add_function(self, function_text):
        if self.display_value.get() == "Error":
            self.clear()
        self.expression += function_text
        self._refresh_display()

    def add_constant(self, constant):
        if self.display_value.get() == "Error":
            self.clear()
        self.expression += constant
        self._refresh_display()

    def calculate(self):
        if not self.expression:
            return

        try:
            result = eval(self.expression, {"__builtins__": {}}, self._safe_math_context())
            self.expression = self._format_number(result)
            self.display_value.set(self.expression)
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
        if not self.expression:
            return
        try:
            result = eval(self.expression, {"__builtins__": {}}, self._safe_math_context()) / 100
            self.expression = self._format_number(result)
            self.display_value.set(self.expression)
        except Exception:
            self.expression = ""
            self.display_value.set("Error")

    def factorial(self):
        if not self.expression:
            return
        try:
            value = eval(self.expression, {"__builtins__": {}}, self._safe_math_context())
            if value < 0 or int(value) != value:
                raise ValueError
            result = math.factorial(int(value))
            self.expression = str(result)
            self.display_value.set(self.expression)
        except Exception:
            self.expression = ""
            self.display_value.set("Error")

    def inverse(self):
        if not self.expression:
            return
        try:
            value = eval(self.expression, {"__builtins__": {}}, self._safe_math_context())
            result = 1 / value
            self.expression = self._format_number(result)
            self.display_value.set(self.expression)
        except Exception:
            self.expression = ""
            self.display_value.set("Error")

    def toggle_sign(self):
        if not self.expression or self.display_value.get() == "Error":
            return

        if self.expression.startswith("-(") and self.expression.endswith(")"):
            self.expression = self.expression[2:-1]
        else:
            self.expression = f"-({self.expression})"
        self._refresh_display()

    def toggle_angle_mode(self):
        self.angle_mode.set("RAD" if self.angle_mode.get() == "DEG" else "DEG")

    def _safe_math_context(self):
        return {
            "pi": math.pi,
            "e": math.e,
            "sqrt": math.sqrt,
            "log": math.log,
            "log10": math.log10,
            "sin": self._sin,
            "cos": self._cos,
            "tan": self._tan,
            "asin": self._asin,
            "acos": self._acos,
            "atan": self._atan,
            "abs": abs,
            "round": round,
        }

    def _to_radians(self, value):
        if self.angle_mode.get() == "DEG":
            return math.radians(value)
        return value

    def _from_radians(self, value):
        if self.angle_mode.get() == "DEG":
            return math.degrees(value)
        return value

    def _sin(self, value):
        return math.sin(self._to_radians(value))

    def _cos(self, value):
        return math.cos(self._to_radians(value))

    def _tan(self, value):
        return math.tan(self._to_radians(value))

    def _asin(self, value):
        return self._from_radians(math.asin(value))

    def _acos(self, value):
        return self._from_radians(math.acos(value))

    def _atan(self, value):
        return self._from_radians(math.atan(value))

    def _refresh_display(self):
        if not self.expression:
            self.display_value.set("0")
            return

        pretty_expression = (
            self.expression.replace("**2", "^2")
            .replace("**", "^")
            .replace("*", "×")
            .replace("/", "÷")
            .replace("-", "−")
            .replace("pi", "π")
        )
        self.display_value.set(pretty_expression)

    def _current_number(self):
        separators = ["+", "-", "*", "/", "%", "(", ")"]
        last_separator = -1
        for separator in separators:
            last_separator = max(last_separator, self.expression.rfind(separator))
        return self.expression[last_separator + 1 :]

    @staticmethod
    def _format_number(number):
        if isinstance(number, float):
            if abs(number) < 1e-12:
                number = 0
            if number.is_integer():
                return str(int(number))
            return f"{number:.12g}"
        return str(number)


def main():
    root = tk.Tk()
    CalculadoraCientifica(root)
    root.mainloop()


if __name__ == "__main__":
    main()
