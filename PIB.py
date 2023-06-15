# Cristina Monterroso
import re


# Función que devuelve un listado de años B
def get_years(linea: str) -> list:
    return linea.strip().split("\t")[1:]


# Función que carga los datos del PIB de cada País y en un diccionario el codigo del país (coinciden los indices en la lista)
def get_data(lineas: str, patron: str) -> dict:
    # Creamos un diccionario vacío como resultado
    pib_data = dict()
    # Iteramos todas las líneas para recoger los datos necesarios
    for linea in lineas:
        # Recogemos la línea donde se encuentra el país
        country_line = linea.strip().split("\t")[0]
        # Buscamos si existe una coincidencia con nuestro patrón
        match = re.search(patron, country_line)
        if match:
            # Guardamos las iniciales del país (.group- lo subdivide por grupos)
            country = match.group(1)
            # Recogemos el listado del PIB de ese país (1 hasta el final)
            pib_list = linea.strip().split("\t")[1:]
            # Añadimos al diccionario y metemos en una lista(pib_list)
            # En el diccionario tenemos su clave(country)valor(pib_list)
            pib_data[country] = pib_list
    return pib_data


def run():
    # Leemos todas las líneas del archivo .tsv
    with open("Phyton\9_de_junio\sdg_08_10.tsv") as archivo:
        lineas = archivo.readlines()

    # Listado de los años (0-código del país)
    years = get_years(lineas[0])

    # Patrón de la expresión regular
    patron = r"CLV10_EUR_HAB,B1GQ,(.+)"

    # Diccionario (pib_data)que será el resultado de los PIB de cada país(1 en adelante)
    pib_data = get_data(lineas[1:], patron)

    # Pedimos al usuario que introduzca las iniciales de un país
    user_input = input("Introduce las iniciales de un país: ")
    user_country = user_input.upper()

    # Comprobamos si el país está en el diccionario
    if user_country in pib_data:
        print(f"Producto Interior Bruto per cápita de {user_country}\nAÑO\tPIB")
        # Mostramos los resultados, pib recorre las dos listas a la vez.
        for year, pib in zip(years, pib_data[user_country]):
            print(f"{year}\t{pib}")
    else:
        print("No se encuentra el país.")


if __name__ == "__main__":
    run()
