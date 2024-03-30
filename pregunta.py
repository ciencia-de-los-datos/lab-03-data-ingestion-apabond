"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd

def ingest_data():
    
    

    data = []

    # Leer el archivo de texto línea por línea
    with open("clusters_report.txt", "r") as file:
        current_cluster = ""
        current_cantidad = ""
        current_porcentaje = ""
        current_palabras = []
        for line in file:
            # Si la línea comienza con un número, probablemente sea parte de un nuevo registro
            if line.strip().startswith(tuple("0123456789")):
                # Procesar el registro anterior (si existe)
                if current_cluster:
                    # Combinar las palabras clave en un solo texto y eliminar el "%" al inicio de cada palabra clave
                    palabras_clave = " ".join([palabra.strip("% ") for palabra in current_palabras])

                    # Agregar el registro a la lista de datos
                    data.append([current_cluster, current_cantidad, current_porcentaje, palabras_clave])

                # Reiniciar las variables para el nuevo registro
                parts = line.strip().split()
                current_cluster = int(parts[0])
                current_cantidad = int(parts[1])
                current_porcentaje = float(parts[2].replace(",", "."))
                current_palabras = parts[3:]
            else:
                # Si no es una nueva línea de registro, agregar las palabras clave a la lista actual
                current_palabras.extend(line.strip().split())

        # Procesar el último registro
        if current_cluster:
            palabras_clave = " ".join([palabra.strip("%") for palabra in current_palabras])
            data.append([current_cluster, current_cantidad, current_porcentaje, palabras_clave])

    # Crear el DataFrame de Pandas
    df = pd.DataFrame(data, columns=["Cluster", "Cantidad de palabras clave", "Porcentaje de palabras clave", "Principales palabras clave"])



    #limpieza
    # 
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ", "_")
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace(".", "")
    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(lambda x: ' '.join(x.split()))

    return df










