from datetime import date
import os

hoy = date.today()

def CargarUsuario():
    dni = input("Ingrese DNI: ")
    if BuscarUsuario(dni):
        print("El usuario ya existe")
        return
    nombre = input("Ingrese nombre: ")
    with open("usuarios.txt", "a") as archivo:
        archivo.write(dni + ";" + nombre + "\n")
    print("Usuario registrado correctamente")

def BuscarUsuario(dni_buscado):
    dni_buscado = str(dni_buscado).strip()
    try:
        with open("usuarios.txt", "r") as archivo:

            for linea in archivo:

                datos = linea.strip().split(";")

                if datos[0] == dni_buscado:
                    return True

        return False
    except FileNotFoundError:
        return False

def CargarLibro():
    codigo = input("Ingrese código: ")
    if BuscarLibro(codigo):
        print("El libro ya existe")
        return
    titulo = input("Ingrese título: ")
    autor = input("Ingrese autor: ")
    stock = int(input("Ingrese stock: "))
    with open("libros.txt", "a") as archivo:
        archivo.write(
            codigo + ";" +
            titulo + ";" +
            autor + ";" +
            str(stock) + "\n"
        )
    print("Libro cargado correctamente")

def BuscarLibro(codigo_buscado):
    try:
        with open("libros.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")
                if datos[0] == str(codigo_buscado):
                    stock = int(datos[3])
                    return stock > 0
        return False
    except FileNotFoundError:
        return False

def MostrarLibros():
    try:
        with open("libros.txt", "r") as archivo:
            encontrado = False
            for linea in archivo:
                datos = linea.strip().split(";")
                if int(datos[3]) > 0:
                    encontrado = True
                    print("\n===================================")
                    print("          LIBRO")
                    print("===================================")
                    print("Código :", datos[0])
                    print("Título :", datos[1])
                    print("Autor  :", datos[2])
                    print("Stock  :", datos[3])
            if not encontrado:
                print("No hay libros disponibles.")
    except FileNotFoundError:
        print("Archivo inexistente")

def ActualizarStock(codigo, cambio):
    try:
        with open("libros.txt", "r") as archivo:
            lineas = archivo.readlines()
        with open("libros.txt", "w") as archivo:
            for linea in lineas:
                datos = linea.strip().split(";")
                if datos[0] == codigo:
                    datos[3] = str(int(datos[3]) + cambio)
                archivo.write(";".join(datos) + "\n")
    except FileNotFoundError:
        print("Archivo inexistente")

def EmitirPrestamo():
    dni = input("Ingrese DNI del usuario: ")
    if not BuscarUsuario(dni):
        print("Usuario inexistente")
        return
    codigo = input("Ingrese código del libro: ")
    if not BuscarLibro(codigo):
        print("Libro sin stock")
        return
    print("\n===== INFORMACIÓN =====")
    print("Las devoluciones fuera del plazo establecido")
    print("tienen una multa de $500 por cada día de demora.\n")
    plazo = int(input("Ingrese plazo (días): "))
    with open("prestamos.txt", "a") as archivo:
        archivo.write(
            dni + ";" +
            codigo + ";" +
            str(hoy) + ";" +
            str(plazo) + ";" +
            "False\n"
        )
    ActualizarStock(codigo, -1)
    print("Préstamo registrado correctamente")

def DevolverLibro():
    dni = input("Ingrese DNI: ")
    codigo = input("Ingrese código del libro: ")
    try:
        with open("prestamos.txt", "r") as archivo:
            lineas = archivo.readlines()
        encontrado = False
        with open("prestamos.txt", "w") as archivo:
            for linea in lineas:
                datos = linea.strip().split(";")
                if datos[0] == dni and datos[1] == codigo and datos[4] == "False":
                    encontrado = True
                    fecha = date.fromisoformat(datos[2])
                    plazo = int(datos[3])
                    dias = (hoy - fecha).days
                    if dias > plazo:

                        demora = dias - plazo

                        multa = demora * 500

                        print("Multa: $", multa)
                    else:

                        print("Libro devuelto en término")
                    datos[4] = "True"
                    ActualizarStock(codigo, 1)
                archivo.write(";".join(datos) + "\n")
        if not encontrado:
            print("No existe préstamo activo")
    except FileNotFoundError:
        print("No existen préstamos")
def MostrarPrestamos():
    try:
        with open("prestamos.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")
                estado = "Activo"
                if datos[4] == "True":
                    estado = "Devuelto"
                print("--------------------------------")
                print("DNI:", datos[0])
                print("Código del libro:", datos[1])
                print("Fecha del préstamo:", datos[2])
                print("Plazo:", datos[3], "días")
                print("Estado:", estado)
    except FileNotFoundError:
        print("No existen préstamos")

def MostrarPrestamosActivos():
    try:
        with open("prestamos.txt", "r") as archivo:
            encontrado = False
            for linea in archivo:
                datos = linea.strip().split(";")
                if datos[4] == "False":
                    encontrado = True
                    print("\n===================================")
                    print("      PRÉSTAMO ACTIVO")
                    print("===================================")
                    print("DNI                 :", datos[0])
                    print("Código del libro    :", datos[1])
                    print("Fecha del préstamo  :", datos[2])
                    print("Plazo               :", datos[3], "días")
                    print("Estado              : Activo")
            if not encontrado:
                print("No existen préstamos activos.")
    except FileNotFoundError:
        print("No existen préstamos")

def MostrarEstadisticas():
    print("\n====== REPORTES ESTADÍSTICOS DE GESTIÓN ======")
    if not os.path.exists("prestamos.txt"):
        print("[AVISO] No hay datos de préstamos suficientes para emitir reportes.")
        return
    total_prestamos = 0          
    prestamos_activos = 0        
    total_recaudado_multas = 0   
    try:
        with open("prestamos.txt", "r") as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue
                campos = linea_limpia.split(";")              
                total_prestamos += 1                             
                if campos[4] == "False":
                    prestamos_activos += 1
                else:  
                    año, mes, dia = map(int, campos[2].split("-"))
                    fecha_p = date(año, mes, dia)
                    dif = (hoy - fecha_p).days
                    intplazo = int(campos[3])
                    if dif > intplazo:
                        dias_demora = dif - intplazo
                        monto_multa = dias_demora * 500
                        total_recaudado_multas += monto_multa 
        print(f" Cantidad total de préstamos realizados : {total_prestamos}")
        print(f" Cantidad de préstamos vigentes activos : {prestamos_activos}")
        print(f" Total acumulado por conceptos de multas : ${total_recaudado_multas}")
        print("=========================================================")
    except Exception as e:
        print(f"[ERROR] No se pudieron procesar las estadísticas: {e}")

def MenuPrincipal():
    """
    Misión: Controlar el flujo principal de la aplicación mediante consola.
    Utiliza una estructura repetitiva indefinida (while) controlada por opciones.
    """
    while True:
        print("\n==========================================")
        print("   SISTEMA DE GESTIÓN DE BIBLIOTECA UTN   ")
        print("==========================================")
        print(f" Fecha de operación: {hoy}")
        print("1. Registrar nuevo Usuario")
        print("2. Registrar nuevo Libro")
        print("3. Ver Catálogo en Stock")
        print("4. Emitir nuevo Préstamo")
        print("5. Procesar Devolución")
        print("6. Ver Historial De Prestamos")
        print("7. Ver Préstamos Activos")
        print("8. Emitir Reportes Estadísticos")
        print("9. Salir del Sistema")
        print("==========================================")            
        opcion = input("Seleccione una opción (1-9): ").strip()
        if opcion == "1":
            CargarUsuario()
        elif opcion == "2":
            CargarLibro()
        elif opcion == "3":
            MostrarLibros()
        elif opcion == "4":
            EmitirPrestamo()
        elif opcion == "5":
            DevolverLibro()
        elif opcion == "6":
            MostrarPrestamos()
        elif opcion == "7":
            MostrarPrestamosActivos()
        elif opcion == "8":
            MostrarEstadisticas()
        elif opcion == "9":
            print("\nCerrando interfaz de consola.")
            break 
        else:
            print("[ERROR] Opción inválida. Ingrese un número entero del 1 al 9.")
if __name__ == "__main__":
    MenuPrincipal()
