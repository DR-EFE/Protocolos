import ctypes
import os

# Constantes para los atributos de la carpeta
FILE_ATTRIBUTE_HIDDEN = 0x02

# Función para cambiar los atributos de la carpeta y ocultarla
def ocultar_carpeta(ruta):
    try:
        # Obtener los atributos actuales de la carpeta
        atributos_actuales = ctypes.windll.kernel32.GetFileAttributesW(ruta)

        # Ocultar la carpeta agregando el atributo FILE_ATTRIBUTE_HIDDEN
        ctypes.windll.kernel32.SetFileAttributesW(ruta, atributos_actuales | FILE_ATTRIBUTE_HIDDEN)
        print(f'La carpeta "{ruta}" ha sido ocultada.')
    except Exception as e:
        print(f'Error al ocultar la carpeta "{ruta}": {str(e)}')

# Ruta de la carpeta que deseas ocultar (reemplaza esta ruta con la que desees ocultar)
carpeta_a_ocultar = r'C:\Users\PC\Downloads\Amistad'

# Llamar a la función para ocultar la carpeta seleccionada
ocultar_carpeta(carpeta_a_ocultar)
