# Morse Trainer GUI

Este es un programa en Python con interfaz gráfica que permite practicar código Morse usando el teclado. Puedes configurar qué teclas usar para el punto (`.`) y la raya (`-`), y el sistema mostrará automáticamente la letra o número correspondiente en función del código ingresado.

## 🧰 Requisitos

- Python 3.7 o superior
- Paquete adicional:
  - `keyboard`

## 📦 Instalación

1. Guarda el proyecto en una carpeta.
2. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
venv\Scripts\activate  # En Windows
# o
source venv/bin/activate  # En Linux/Mac
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## 🚀 Uso

1. Ejecuta el programa:

```bash
python morse_gui.py
```

2. En la interfaz:
   - Configura qué teclas usarás para el punto y la raya.
   - Pulsa esas teclas para enviar señales.
   - El sistema detectará pausas para traducir el código Morse a una letra o número.
   - También puedes ver el alfabeto y los números en código Morse como referencia dentro de la aplicación.

---

## 📋 Código Morse

```
Letra : Código Morse
-------------------------
A : .-
B : -...
C : -.-.
D : -..
E : .
F : ..-.
G : --.
H : ....
I : ..
J : .---
K : -.-
L : .-..
M : --
N : -.
O : ---
P : .--.
Q : --.-
R : .-.
S : ...
T : -
U : ..-
V : ...-
W : .--
X : -..-
Y : -.--
Z : --..

0 : -----
1 : .----
2 : ..---
3 : ...--
4 : ....-
5 : .....
6 : -....
7 : --...
8 : ---..
9 : ----.
```

---

## 🧠 Créditos

Desarrollado por ErikLPA

