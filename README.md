# Sistema de Gestión de Biblioteca

## Integrantes

- Joaquin Selinger
- Tomas Nahuel Fanchin
- Matias Ivan Silva

## Comisión

Comisión: D

---

# Descripción general del sistema

Este proyecto consiste en el desarrollo de un Sistema de Gestión de Biblioteca realizado en Python.

El sistema permite administrar los recursos de una biblioteca mediante una interfaz de consola, gestionando usuarios, libros y préstamos.

La información se almacena en archivos de texto, permitiendo conservar los datos entre ejecuciones del programa.

---

# Funcionalidades principales

El sistema permite:

- Registrar usuarios.
- Registrar libros.
- Consultar libros disponibles.
- Emitir préstamos de libros.
- Verificar existencia de usuarios y disponibilidad de libros.
- Actualizar automáticamente el stock al realizar préstamos y devoluciones.
- Procesar devoluciones.
- Calcular multas por demora en la devolución.
- Consultar historial de préstamos.
- Visualizar préstamos activos.
- Generar reportes estadísticos del funcionamiento de la biblioteca.

---

# Archivos utilizados

El sistema utiliza archivos de texto para almacenar la información:

- `usuarios.txt` → contiene los usuarios registrados.
- `libros.txt` → contiene los libros disponibles y su stock.
- `prestamos.txt` → contiene los préstamos realizados y su estado.

---

# Requisitos

Para ejecutar el proyecto se necesita:

- Python 3.x

No requiere instalación de librerías externas.

Se utilizan módulos incluidos en Python:

- `datetime` para manejo de fechas.
- `os` para operaciones con archivos.

---

# Instrucciones de ejecución

## Opción 1: Desde consola

Ubicarse en la carpeta del proyecto y ejecutar:

```bash
python biblioteca.py
```

## Opción 2: Ejecutar mediante archivo BAT

También es posible iniciar el sistema utilizando el archivo `Biblioteca.bat`.

Para ejecutarlo:

1. Abrir la carpeta del proyecto.
2. Realizar doble clic sobre el archivo:

`Biblioteca.bat`

---

# Uso de Inteligencia Artificial

Durante el desarrollo del proyecto se utilizó la herramienta de Inteligencia Artificial como apoyo para:

- Resolver dudas sobre Python.
- Comprender el funcionamiento de funciones y estructuras utilizadas.
- Analizar errores y posibles mejoras del código.

Las sugerencias generadas fueron revisadas, adaptadas y comprendidas por los integrantes del grupo antes de incorporarlas al sistema.



