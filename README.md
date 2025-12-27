<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/3426/3426653.png" alt="Logo Sixteen" width="80px" style="margin-bottom: 20px;">

  <h1>🧩 Sixteen</h1>

  <p>
    <strong>Fundamentos de Programación</strong><br>
    Un desafío de lógica matemática y ordenamiento matricial en terminal.
  </p>

  <img src="https://img.shields.io/badge/Language-Python_3-blue?style=flat-square&logo=python" alt="Python 3">
  <img src="https://img.shields.io/badge/Interface-CLI-black?style=flat-square&logo=gnu-bash" alt="CLI">
  <img src="https://img.shields.io/badge/Logic-Matrix_Rotation-green?style=flat-square" alt="Matrix">

  <br><br>
  <img src="sixteen_gameplay.png" alt="Gameplay Screenshot" width="80%" style="border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.2);">
</div>

---

## 📋 Descripción

**Sixteen** es un juego de ingenio desarrollado en Python que opera sobre una matriz de números enteros (tablero). El objetivo es ordenar los números de menor a mayor (comenzando desde el 1) manipulando el tablero exclusivamente mediante **rotaciones de filas y columnas**.

El proyecto demuestra el manejo sólido de:
* Listas de listas (Matrices).
* Validación robusta de entradas de usuario.
* Modularización de código (lógica vs. interfaz).

---

## ⚙️ Requerimientos

El proyecto no utiliza librerías externas, por lo que solo necesitas:
* **Python 3.x** instalado.

---

## 🚀 Instalación y Ejecución

Sigue estos pasos para correr el juego en tu terminal:

### Ejecutar el juego

```bash
python3 main.py
```

## 🎮 Cómo Jugar

Al iniciar, el programa te pedirá definir las dimensiones del tablero (filas y columnas). Luego, el tablero se mezclará automáticamente.

### Comandos de Movimiento

El formato de entrada es: **índice,movimiento**

| Tecla | Acción |
| :---: | :--- |
| <kbd>W</kbd> (Arriba) | Rota la columna hacia arriba |
| <kbd>S</kbd> (Abajo) | Rota la columna hacia abajo |
| <kbd>A</kbd> (Izquierda) | Rota la fila hacia la izquierda |
| <kbd>D</kbd> (Derecha) | Rota la fila hacia la derecha |

### Ejemplos:

- 0,s -> Mueve la columna 0 hacia abajo.
- 2,a -> Mueve la fila 2 hacia la izquierda.

### Otros Comandos:

- m: Mezclar el tablero nuevamente.
- q: Salir del juego.

---

## 📂 Estructura del Proyecto

- sixteen.py: Motor del juego. Contiene la lógica pura (crear tablero, rotaciones, verificar si está ordenado). No interactúa con el usuario.

- main.py: Interfaz y Flujo. Se encarga de los input/print, validaciones de entrada y el bucle principal del juego.

---

## 👥 Autor

| Integrante | Padrón | Contacto |
| :--- | :---: | :---: |
| **Calderón Vasil, Máximo Augusto** | 111810 | [![GitHub](https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github)](https://github.com/maxivasil) [![Email](https://img.shields.io/badge/Email-red?style=flat-square&logo=gmail&logoColor=white)](mailto:mcalderonv@fi.uba.ar) |