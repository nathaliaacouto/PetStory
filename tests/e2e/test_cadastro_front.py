import time
from selenium.webdriver.common.by import By

nome_cliente = "Marcos da Silva"
telefone = "12345678"
instagram = "marcossilva"
cep = "87412369"
endereco = "Rua Que Nao Existe, 546"
email = "marcos@silva.com"

nome_pet = "Toto"
raca = "Pug"
idade = "8"
pelagem = "caramelo"
nome_pet2 = "Mel"
raca2 = "Poodle"
idade2 = "6"
pelagem2 = "branca"

def test_registro_interface(browser, app):
    browser.get("http://localhost:5000/registro")
    assert browser.title == "PetStory | Registro"
    browser.find_element(By.ID, "pets-0-dog").send_keys(nome_pet)
    browser.find_element(By.ID, "pets-0-breed").send_keys(raca)
    browser.find_element(By.ID, "pets-0-fur").send_keys(pelagem)
    browser.find_element(By.ID, "pets-0-age").send_keys(idade)
    browser.find_element(By.ID, "owner").send_keys(nome_cliente)
    browser.find_element(By.ID, "instagram").send_keys(instagram)
    browser.find_element(By.ID, "zip_code").send_keys(cep)
    browser.find_element(By.ID, "address").send_keys(endereco)
    browser.find_element(By.ID, "phone").send_keys(telefone)
    browser.find_element(By.ID, "email").send_keys(email)
    browser.find_element(By.ID, "add_pet").click()
    browser.find_element(By.ID, "pets-1-dog").send_keys(nome_pet2)
    browser.find_element(By.ID, "pets-1-breed").send_keys(raca2)
    browser.find_element(By.ID, "pets-1-fur").send_keys(pelagem2)
    browser.find_element(By.ID, "pets-1-age").send_keys(idade2)
    sub_btn = browser.find_element(By.ID, "submit")
    browser.execute_script("arguments[0].click()", sub_btn)
    time.sleep(1)
    success_message = browser.find_element(By.CLASS_NAME, "alert-list-item").text
    assert "Cadastro realizado com sucesso!" == success_message