import time
from selenium.webdriver.common.by import By
from app.controllers import ClienteController, PetController

nome_cliente = "Marcos da Silva"
telefone = "12345678"
cpf = "08476485267"
cep = "87412369"
endereco = "Rua Que Nao Existe, 546"
email = "marcos@silva.com"

nome_pet = "Toto"
raca = "SRD"
idade = "8"
pelagem = "caramelo"

def test_registro_interface(browser):
    browser.get("http://localhost:5000/registro")
    assert browser.title == "PetStory | Registro"
    # browser.find_element(By.ID, "dog").send_keys(nome_pet)
    # browser.find_element(By.ID, "breed").send_keys(raca)
    # browser.find_element(By.ID, "fur").send_keys(pelagem)
    # browser.find_element(By.ID, "age").send_keys(idade)
    # browser.find_element(By.ID, "owner").send_keys(nome_cliente)
    # browser.find_element(By.ID, "cpf").send_keys(cpf)
    # browser.find_element(By.ID, "zip_code").send_keys(cep)
    # browser.find_element(By.ID, "address").send_keys(endereco)
    # browser.find_element(By.ID, "phone").send_keys(telefone)
    # browser.find_element(By.ID, "email").send_keys(email)
    # sub_btn = browser.find_element(By.ID, "submit")
    # browser.execute_script("arguments[0].click()", sub_btn)
    # time.sleep(1)
    # success_message = browser.find_element(By.CLASS_NAME, "alert-list-item").text
    # assert "Cadastro realizado com sucesso!" == success_message
    # c_control = ClienteController()
    # p_control = PetController()
    # marcos = c_control.get_cliente_by_nome(nome_cliente)
    # assert marcos.nome == nome_cliente