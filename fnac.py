import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def buscar_precio_libro(isbn):
    # Inicia el navegador
    driver = webdriver.Firefox()

    # Genera la URL de FNAC con el ISBN proporcionado
    url_fnac = f"https://www.fnac.es/SearchResult/ResultList.aspx?Search={isbn}&sft=1&sa=0"
    print(f"URL generada: {url_fnac}")
    
    # Navega a la página de FNAC
    driver.get(url_fnac)
    
    # Espera explícita hasta que el elemento de los productos esté presente en la página
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.a-offscreen')))
    except Exception as e:
        print(f"Error al cargar la página de FNAC: {e}")
        driver.quit()
        return

    # Intentar encontrar el mensaje de "No hay resultados"
    try:
        mensaje_no_resultados = driver.find_element(By.XPATH, "//*[contains(text(), 'No tenemos')]")
        print("No hay resultados para la búsqueda.")
    except NoSuchElementException:
        # Si no hay mensaje de no resultados, intentar encontrar el precio
        try:
            enlace_producto = driver.find_elements(By.CSS_SELECTOR, 'span.a-offscreen')[0]
            print(f"Precio producto: {enlace_producto.get_attribute('innerHTML').replace('&nbsp;', '')}")
        except IndexError:
            print("No se pudo encontrar el precio del producto.")
    
    # Cierra el navegador después de la búsqueda
    driver.quit()

# Obtener el ISBN desde la línea de comandos
if len(sys.argv) > 1:
    isbn = sys.argv[1]
    buscar_precio_libro(isbn)
else:
    print("Por favor, pasa un ISBN como argumento al ejecutar el script.")
