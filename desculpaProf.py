import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service  # Importa o Service
import time

# Caminho do ChromeDriver
driver_path = r'C:\Users\riana\Desktop\chromedriver-win64\chromedriver.exe'  # Atualize para o caminho correto
moodle_url = 'https://moodle.utfpr.edu.br/course/view.php?id=26696'  # URL do Moodle
username = ''  # Seu nome de usuário
password = ''  # Sua senha

# Verifica se o ChromeDriver existe
if not os.path.isfile(driver_path):
    raise FileNotFoundError(f"ChromeDriver não encontrado no caminho: {driver_path}")

# Inicializa o Service
service = Service(driver_path)

# Loop para realizar o login 50 vezes
for i in range(300):
    print(f"Execução {i + 1} de 300")

    # Inicializa o WebDriver
    driver = webdriver.Chrome(service=service)

    try:
        # Acessa a página do Moodle
        driver.get(moodle_url)

        # Encontra os campos de entrada para nome de usuário e senha
        user_input = driver.find_element(By.NAME, 'username')  # Nome do campo de usuário
        pass_input = driver.find_element(By.NAME, 'password')  # Nome do campo de senha

        # Insere os dados de login
        user_input.send_keys(username)
        pass_input.send_keys(password)

        # Envia o formulário
        pass_input.send_keys(Keys.RETURN)

        # Aguarda alguns segundos para garantir que o login foi bem-sucedido
        time.sleep(1)  # Ajuste conforme necessário

    finally:
        # Fecha o navegador
        driver.quit()

    # Aguarda um segundo antes da próxima execução (opcional)
    time.sleep(1)  # Ajuste conforme necessário
