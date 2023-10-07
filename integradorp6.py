from functools import reduce

def convertir_a_matriz(laberinto_str):
   
    return list(map(list, laberinto_str.split('\n')))

def leer_mapa(ruta_mapa):
  
    with open(ruta_mapa, 'r') as archivo:
        lineas = archivo.readlines()

    
    laberinto_str = reduce(lambda x, y: x + y.strip(), lineas, '')

   
    return convertir_a_matriz(laberinto_str)


ruta_mapa = r'C:\Users\usuario\Desktop\mapa.txt'  

try:
    matriz_laberinto = leer_mapa(ruta_mapa)
    print(matriz_laberinto)
except FileNotFoundError:
    print(f"No se encontró el archivo en la ruta: {ruta_mapa}")
except Exception as e:
    print(f"Error al leer el mapa: {e}")
