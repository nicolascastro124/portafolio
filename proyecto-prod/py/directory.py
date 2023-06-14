import os
#Funcion que obtiene todos los directorios del proyecto y devuelve la ruta
#
def searchDirectory(nombre_carpeta):
    directorio = os.path.abspath(os.curdir) + os.sep
    rutas_carpetas = []

    for ruta_actual, carpetas, archivos in os.walk(directorio):
        if nombre_carpeta in carpetas:
            # Almacena la ruta de la carpeta en la lista de rutas
            rutas_carpetas.append(os.path.join(ruta_actual, nombre_carpeta))

    # Se encontró una sola carpeta
    if len(rutas_carpetas) == 1:
        return rutas_carpetas[0] + os.sep
    elif len(rutas_carpetas) > 1:
        raise ValueError('Se encontraron varias carpetas con el mismo nombre')
    else:
        return None


