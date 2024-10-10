import os
import re

def buscar_errores(directorio_base, texto_busqueda):
    resultados = []

    for root, dirs, files in os.walk(directorio_base):
        for archivo in files:
            ruta_archivo = os.path.join(root, archivo)

            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    if re.search(texto_busqueda, contenido):
                        resultados.append(ruta_archivo)
                        print(f"Encontrado en: {ruta_archivo}")
            except Exception as e:
                print(f"No se pudo abrir {ruta_archivo}: {e}")

    return resultados

# Llamar a la función
directorio = "C:/ruta/de/tu/directorio_de_clientes"
error_a_buscar = "error 3"
resultados = buscar_errores(directorio, error_a_buscar)

# Opcional: abrir los archivos encontrados
for archivo in resultados:
    os.startfile(archivo)
