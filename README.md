# Calculadora Científica y Básica de Escritorio

Aplicación de escritorio desarrollada en **Python** con **Tkinter**, que ofrece tanto una **Calculadora Científica Avanzada** con funciones trigonométricas, hiperbólicas y logarítmicas, como una versión **Básica** para operaciones cotidianas.

![Calculadora Científica](img/screenshot.png)

---

## Características

- **Calculadora Científica (`calculadora_cientifica.py`):**
  - Operaciones aritméticas y precedencia de operadores con paréntesis.
  - Funciones trigonométricas e hiperbólicas (`sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `sinh`, `cosh`, `tanh`).
  - Modos de ángulo: conmutador entre **DEG** (grados sexagesimales) y **RAD** (radianes).
  - Funciones matemáticas avanzadas: raíces (`sqrt`), logaritmo base 10 (`log`), logaritmo natural (`ln`), potencias (`x²`, `xʸ`), factorial (`n!`), inverso (`1/x`) y porcentaje (`%`).
  - Constantes matemáticas: $\pi$ y $e$.
  - Soporte completo para entrada mediante teclado físico y atajos (`Enter`, `BackSpace`, `Esc`).
  - Contexto de evaluación matemática seguro en memoria.

- **Calculadora Básica (`calculadora_gui.py`):**
  - Interfaz gráfica compacta y minimalista para cálculos rápidos.
  - Suma, resta, multiplicación, división, porcentajes y punto decimal.

---

## Requisitos y Ejecución

Al estar construida con la biblioteca estándar `tkinter`, **no requiere la instalación de dependencias externas**.

### 1. Clonar el repositorio
```bash
git clone https://github.com/urhiel-tao/calculadora-cientifica.git
cd calculadora-cientifica
```

### 2. Ejecutar la Calculadora Científica
```bash
python calculadora_cientifica.py
```

### 3. Ejecutar la Calculadora Básica
```bash
python calculadora_gui.py
```

---

## Pruebas Unitarias

El proyecto incluye tests unitarios para validar la precisión de las operaciones matemáticas:

```bash
python -m unittest discover tests
```

---

## Autor

- **Hector Uriel Taño Fernandez** - [urhiel-tao](https://github.com/urhiel-tao)
- Contacto: [urhieltatao@gmail.com](mailto:urhieltatao@gmail.com)
